"""DataAgent: loads and prepares logs into analysis-ready tabular data."""
import pandas as pd
import numpy as np
from dateutil import parser

class DataAgent:
    def __init__(self, session):
        self.session = session

    def ingest_and_clean(self, logs, trace_id):
        df = logs.copy()
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
        else:
            if 'start_time' in df.columns:
                df['timestamp'] = pd.to_datetime(df['start_time'])
            else:
                df['timestamp'] = pd.to_datetime(pd.Series(pd.Timestamp.now(), index=df.index))

        if 'success' in df.columns:
            df['success'] = pd.to_numeric(df['success'], errors='coerce').fillna(0).astype(int)

        if 'start_time' in df.columns and 'end_time' in df.columns:
            df['start_time'] = pd.to_datetime(df['start_time'])
            df['end_time'] = pd.to_datetime(df['end_time'])
            df['duration'] = (df['end_time'] - df['start_time']).dt.total_seconds()
        else:
            df['duration'] = df.get('duration', pd.Series(np.random.rand(len(df)) * 30))

        if 'case_id' not in df.columns:
            df['case_id'] = range(1, len(df) + 1)
        if 'step' not in df.columns and 'task' in df.columns:
            df = df.rename(columns={'task': 'step'})

        self.session.log_event(trace_id, 'data_agent.cleaning', {'rows': len(df)})
        return df

    def extract_features(self, df, trace_id):
        features = df.groupby('step').agg({
            'duration': 'mean',
            'success': 'mean',
            'case_id': 'nunique'
        }).reset_index()

        features.columns = ['step', 'avg_duration', 'success_rate', 'unique_cases']
        self.session.log_event(trace_id, 'data_agent.features', {'steps': len(features)})
        return features
