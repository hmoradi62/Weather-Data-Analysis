cat > import pandas as pd
import numpy as np

def load_data(filepath):
    """Load and return dataset"""
    return pd.read_csv(filepath)

def basic_stats(df):
    """Calculate basic statistics"""
    return df.describe()
