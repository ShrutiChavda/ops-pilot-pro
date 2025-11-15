class SimulationEngine:
    def simulate_parallelize(self, features, step, reduction_pct=40):
        f = features.copy()
        mask = f['step'] == step
        f.loc[mask, 'avg_duration'] = f.loc[mask, 'avg_duration'] * (1 - reduction_pct/100.0)
        return f
