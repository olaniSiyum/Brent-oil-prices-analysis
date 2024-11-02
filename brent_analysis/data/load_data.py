# load_data.py
import pandas as pd
import logging

def load_brent_data(filepath):
    """Load and preprocess the Brent oil prices data."""
    df = pd.read_csv(filepath)
    try:
        data = pd.read_csv(filepath, parse_dates=['Date'], dayfirst=True)
        logging.info("Data loaded successfully.")
        return data
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise
