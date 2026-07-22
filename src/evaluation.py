"""
evaluation.py

Utility functions for evaluating regression models.
"""

from sklearn.metrics import (
    mean_absolute_error,
    root_mean_squared_error,
    r2_score
)


def evaluate_model(model, X_test, y_test):
    """
    Evaluate a regression model.

    Parameters
    ----------
    model : trained regression model
    X_test : pandas DataFrame
    y_test : pandas Series

    Returns
    -------
    dict
        Dictionary containing MAE, RMSE and R² score.
    """

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = root_mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    return {
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }


def print_results(model_name, results):
    """
    Print evaluation metrics in a readable format.
    """

    print(f"\n{model_name}")
    print("-" * len(model_name))
    print(f"MAE : {results['MAE']:.4f}")
    print(f"RMSE: {results['RMSE']:.4f}")
    print(f"R²  : {results['R2']:.4f}")
    