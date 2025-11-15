"""ForecastingAgent: quick impact forecast simulation (rule-based)."""
class ForecastingAgent:
    def __init__(self, session):
        self.session = session

    def forecast_impact(self, suggestions, trace_id):
        forecast = []
        for s in suggestions:
            if s.get('type') == 'parallelize':
                forecast.append({
                    'step': s.get('step'),
                    'expected_duration_reduction_pct': 40
                })
            elif s.get('type') == 'validate':
                forecast.append({
                    'step': s.get('step'),
                    'expected_success_increase_pct': 12
                })
            else:
                forecast.append({
                    'step': s.get('step'),
                    'expected_detection_improvement_pct': 5
                })
        self.session.log_event(trace_id, 'forecasting_agent.results', {'count': len(forecast)})
        return forecast
