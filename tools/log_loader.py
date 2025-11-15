import pandas as pd
import os

DEFAULT_SAMPLE = os.path.join(os.path.dirname(__file__), '..', 'examples', 'sample_logs.csv')

def load_logs(path=None):
    if path is None:
        path = DEFAULT_SAMPLE
    df = pd.read_csv(path)
    return df
