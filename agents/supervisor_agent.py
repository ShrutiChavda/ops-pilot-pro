from tools.chart_generator import ChartGenerator
import os

class SupervisorAgent:
    def run(self, trace_id, memory):
        feats = memory.load(f'{trace_id}_features')
        feats_df = __import__('pandas').DataFrame(feats)

        bns = memory.load(f'{trace_id}_bottlenecks')
        sug = memory.load(f'{trace_id}_suggestions')

        OUT = os.path.join(os.getcwd(), 'outputs')
        os.makedirs(OUT, exist_ok=True)

        charts = ChartGenerator().make_charts(feats_df, bns, sug, OUT)

        summary = {
            'total_steps': len(feats_df),
            'bottlenecks': bns,
            'suggestions': sug,
            'charts': charts
        }
        memory.save(f'{trace_id}_final_report', summary)
        return summary
