"""Run simple automated evaluation against golden tests."""
import json
import os
from agents.orchestrator import Orchestrator

def run():
    orch = Orchestrator()
    orch.run_demo()
    outdir = os.path.join(os.path.dirname(__file__), '..', 'outputs')
    files = [f for f in os.listdir(outdir) if f.startswith('report_') and f.endswith('.json')]
    if not files:
        print('No reports found')
        return
    latest = sorted(files)[-1]
    rpt = json.load(open(os.path.join(outdir, latest)))

    # run checks
    tests = json.load(open(os.path.join(os.path.dirname(__file__), 'golden_tests.json')))
    score = 0
    for t in tests:
        expected = t['expected_bottlenecks'][0]
        found = any(
            expected in (s.get('step') if isinstance(s.get('step'), str) else '')
            for s in rpt.get('bottlenecks', [])
        )
        if found:
            score += 1
    print('Evaluation score:', score, 'of', len(tests))

if __name__ == '__main__':
    run()
