"""BottleneckAgent: analyzes features to identify slow or failing steps."""
import numpy as np

class BottleneckAgent:
    def __init__(self, session):
        self.session = session

    def find_bottlenecks(self, features, trace_id):
        f = features.copy()
        dur_ptp = float(f['avg_duration'].ptp()) if f['avg_duration'].ptp() != 0 else 1.0
        f['dur_norm'] = (f['avg_duration'] - f['avg_duration'].min()) / (dur_ptp + 1e-6)
        f['fail_norm'] = 1 - f['success_rate']
        f['score'] = 0.6 * f['dur_norm'] + 0.4 * f['fail_norm']
        candidates = f.sort_values('score', ascending=False).head(5)[['step', 'avg_duration', 'success_rate', 'score']]
        results = candidates.to_dict(orient='records')
        self.session.log_event(trace_id, 'bottleneck_agent.results', {'count': len(results)})
        return results
