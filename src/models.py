"""
models.py

Functions for training machine learning models.
"""

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor


def train_linear_regression(X_train, y_train):
    """
    Train a Linear Regression model.
    """

    model = LinearRegression()

    model.fit(X_train, y_train)

    return model


def train_random_forest(
    X_train,
    y_train,
    n_estimators=300,
    random_state=42,
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1
):
    """
    Train a Random Forest Regressor.
    """

    model = RandomForestRegressor(
        n_estimators=n_estimators,
        random_state=random_state,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf
    )

    model.fit(X_train, y_train)

    return model

def train_xgboost(
    X_train,
    y_train,
    n_estimators=300,
    learning_rate=0.05,
    max_depth=6,
    random_state=42
):
    """
    Train an XGBoost Regressor.
    """

    model = XGBRegressor(
        n_estimators=n_estimators,
        learning_rate=learning_rate,
        max_depth=max_depth,
        random_state=random_state
    )

    model.fit(X_train, y_train)

    return model