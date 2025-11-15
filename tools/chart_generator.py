import os
import matplotlib.pyplot as plt

class ChartGenerator:
    def make_charts(self, features, bottlenecks, forecast, outdir):
        charts = []
        # duration bar
        plt.figure(figsize=(8,4))
        plt.bar(features['step'], features['avg_duration'])
        plt.xticks(rotation=45)
        plt.title('Average duration per step')
        p1 = os.path.join(outdir, 'avg_duration.png')
        plt.tight_layout()
        plt.savefig(p1)
        charts.append(p1)
        plt.close()

        # bottleneck highlights
        steps = [b['step'] for b in bottlenecks]
        scores = [b['score'] for b in bottlenecks]
        plt.figure(figsize=(8,4))
        plt.bar(steps, scores)
        plt.title('Bottleneck scores')
        p2 = os.path.join(outdir, 'bottleneck_scores.png')
        plt.tight_layout()
        plt.savefig(p2)
        charts.append(p2)
        plt.close()

        # forecast simple
        plt.figure(figsize=(8,4))
        labels = [f['step'] for f in forecast]
        values = [f.get('expected_duration_reduction_pct', f.get('expected_success_increase_pct', 0)) for f in forecast]
        plt.bar(labels, values)
        plt.title('Expected impact')
        p3 = os.path.join(outdir, 'forecast_impact.png')
        plt.tight_layout()
        plt.savefig(p3)
        charts.append(p3)
        plt.close()

        return charts
