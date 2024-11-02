# test_load_data.py
import pytest
from brent_analysis.data.load_data import load_brent_data

def test_load_data():
    df = load_brent_data('data/Copy of BrentOilPrices.csv')
    assert not df.empty, "Dataframe is empty"
    assert 'Price' in df.columns, "Price column is missing"
