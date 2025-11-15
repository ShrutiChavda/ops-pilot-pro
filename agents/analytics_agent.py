import pandas as pd

class AnalyticsAgent:
    def run(self, trace_id, memory):

        # Load raw logs from memory
        raw = memory.load(f"{trace_id}_raw_logs")
        df = pd.DataFrame(raw)

        # Count steps
        features = df.groupby("step")["end_time"].count().reset_index()
        features.rename(columns={"end_time": "count"}, inplace=True)

        # Compute durations
        duration = df.copy()
        duration["start_time"] = pd.to_datetime(duration["start_time"])
        duration["end_time"] = pd.to_datetime(duration["end_time"])
        duration["dur"] = (duration["end_time"] - duration["start_time"]).dt.total_seconds()

        # Average duration per step (in seconds)
        f2 = duration.groupby("step")["dur"].mean().reset_index()
        f2.rename(columns={"dur": "avg_duration"}, inplace=True)

        # Detect bottlenecks
        mean_dur = f2["avg_duration"].mean()
        bottlenecks = []

        for _, row in f2.iterrows():
            score = row["avg_duration"] / mean_dur
            if score > 1.2:
                bottlenecks.append({
                    "step": str(row["step"]),
                    "score": float(score),
                    "avg_duration": float(row["avg_duration"])
                })

        # ==== FIX: Convert all values to JSON-safe types ====
        features_json = features.to_dict(orient="records")
        f2_json = f2.to_dict(orient="records")

        # Save to memory (JSON safe)
        memory.save(f"{trace_id}_features", f2_json)
        memory.save(f"{trace_id}_steps", features_json)
        memory.save(f"{trace_id}_bottlenecks", bottlenecks)

        return {
            "bottlenecks_found": len(bottlenecks),
            "mean_duration": float(mean_dur)
        }
