import pandas as pd
import numpy as np

def load_data(weather):
    """Load and return dataset"""
    return pd.read_csv(weather)

def basic_stats(df):
    """Calculate basic statistics"""
    return df.describe()
