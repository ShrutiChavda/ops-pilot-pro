class ReviewerAgent:
    def run(self, trace_id, memory):
        bottlenecks = memory.load(f'{trace_id}_bottlenecks')
        suggestions = []
        for b in bottlenecks:
            suggestions.append({
                'step': b['step'],
                'expected_duration_reduction_pct': round(b['score'] * 10, 2),
                'expected_success_increase_pct': round(100 / b['score'], 2)
            })
        memory.save(f'{trace_id}_suggestions', suggestions)
        return {'suggestions': suggestions}
