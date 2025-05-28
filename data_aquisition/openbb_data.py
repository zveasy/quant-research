# openbb_data.py
# This module contains utility functions to acquire financial data using the OpenBB platform and pandas_datareader

from openbb import obb  # Import OpenBB SDK
import pandas as pd
import pandas_datareader as pdr  # Used to get factor models like Fama-French

# Set global preference to return data as pandas DataFrames
obb.user.preferences.output_type = "dataframe"

def get_stock_data(ticker, provider="yfinance"):
    """
    Fetch historical stock data for a given ticker symbol.

    Parameters:
        ticker (str): The stock ticker symbol (e.g., "AAPL", "SPY")
        provider (str): Data provider (default is 'yfinance')

    Returns:
        pd.DataFrame: Historical price data
    """
    return obb.equity.price.historical(ticker, provider=provider)


def get_futures_curve(symbol="VX"):
    """
    Fetch the current futures curve for a given futures symbol.

    Parameters:
        symbol (str): Futures symbol (default is "VX" for VIX futures)

    Returns:
        pd.DataFrame: Futures curve data
    """
    return obb.derivatives.futures.curve(symbol=symbol)


def get_options_chain(symbol="SPY"):
    """
    Fetch the options chain for a given stock symbol.

    Parameters:
        symbol (str): Stock ticker (default is "SPY")

    Returns:
        pd.DataFrame: Options chain data
    """
    return obb.derivatives.options.chains(symbol=symbol)


def get_fama_french_factors():
    """
    Download Fama-French 3-factor monthly and annual data.

    Returns:
        dict: Contains multiple pandas DataFrames for monthly, annual, and descriptive info
    """
    return pdr.get_data_famaf
