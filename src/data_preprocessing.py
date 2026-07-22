"""
data_preprocessing.py

Functions for loading and preprocessing data.
"""

import pandas as pd


def load_data(file_path):
    """
    Load dataset from a CSV file.

    Parameters
    ----------
    file_path : str
        Path to the CSV file.

    Returns
    -------
    pandas.DataFrame
    """

    return pd.read_csv(file_path)
def split_features_target(df, target_column):
    """
    Split the dataset into features (X) and target (y).

    Parameters
    ----------
    df : pandas.DataFrame
    target_column : str

    Returns
    -------
    X : pandas.DataFrame
    y : pandas.Series
    """

    X = df.drop(columns=[target_column])
    y = df[target_column]

    return X, y
from sklearn.model_selection import train_test_split


def split_data(
    X,
    y,
    test_size=0.20,
    random_state=42
):
    """
    Split the data into training and testing sets.
    """

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state
    )