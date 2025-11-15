import uuid
from memory.session_store import SessionStore
from memory.memory_bank import MemoryBank
from agents.ingestion_agent import IngestionAgent
from agents.analytics_agent import AnalyticsAgent
from agents.reviewer_agent import ReviewerAgent
from agents.supervisor_agent import SupervisorAgent

class Orchestrator:
    def __init__(self):
        self.memory = MemoryBank()
        self.session = SessionStore()
        self.ingest = IngestionAgent()
        self.analyze = AnalyticsAgent()
        self.review = ReviewerAgent()
        self.supervisor = SupervisorAgent()

    def run(self):
        trace = str(uuid.uuid4())
        self.session.log_event(trace, 'start', {})

        r1 = self.ingest.run(trace, self.memory)
        self.session.log_event(trace, 'ingestion', r1)

        r2 = self.analyze.run(trace, self.memory)
        self.session.log_event(trace, 'analytics', r2)

        r3 = self.review.run(trace, self.memory)
        self.session.log_event(trace, 'reviewer', r3)

        r4 = self.supervisor.run(trace, self.memory)
        self.session.log_event(trace, 'supervisor', r4)

        self.session.log_event(trace, 'end', {})
        return r4
