from agents.orchestrator import Orchestrator

if __name__ == '__main__':
    out = Orchestrator().run()
    print('=== FINAL REPORT ===')
    print(out)
