"""OptimizationAgent: suggests operational changes and action plans."""
class OptimizationAgent:
    def __init__(self, session):
        self.session = session

    def suggest_improvements(self, bottlenecks, trace_id):
        suggestions = []
        for b in bottlenecks:
            step = b.get('step', 'unknown')
            avg_duration = b.get('avg_duration', 0)
            success_rate = b.get('success_rate', 1.0)
            if avg_duration > 60:
                suggestions.append({
                    'step': step,
                    'type': 'parallelize',
                    'desc': f'Parallelize {step} to reduce avg duration'
                })
            elif success_rate < 0.8:
                suggestions.append({
                    'step': step,
                    'type': 'validate',
                    'desc': f'Add validation and retries for {step} to reduce failure'
                })
            else:
                suggestions.append({
                    'step': step,
                    'type': 'monitor',
                    'desc': f'Add enhanced monitoring for {step}'
                })
        self.session.log_event(trace_id, 'optimization_agent.suggestions', {'count': len(suggestions)})
        return suggestions
