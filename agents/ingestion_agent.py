from tools.log_loader import load_logs

class IngestionAgent:
    def run(self, trace_id, memory):
        df = load_logs()
        memory.save(f'{trace_id}_raw_logs', df.to_dict())
        return {'status': 'ok', 'rows': len(df)}
