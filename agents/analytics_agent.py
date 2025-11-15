import pandas as pd

class AnalyticsAgent:
    def run(self, trace_id, memory):
        raw = memory.load(f'{trace_id}_raw_logs')
        df = pd.DataFrame(raw)

        features = df.groupby('step')['end_time'].count().reset_index()
        duration = df.copy()
        duration['dur'] = pd.to_datetime(duration['end_time']) - pd.to_datetime(duration['start_time'])
        f2 = duration.groupby('step')['dur'].mean().reset_index()
        f2['avg_duration'] = f2['dur'].dt.total_seconds()

        bottlenecks = []
        for _, row in f2.iterrows():
            score = row['avg_duration'] / f2['avg_duration'].mean()
            if score > 1.2:
                bottlenecks.append({'step': row['step'], 'score': float(score)})

        memory.save(f'{trace_id}_features', f2.to_dict())
        memory.save(f'{trace_id}_bottlenecks', bottlenecks)
        return {'bottlenecks_found': len(bottlenecks)}
