"""
explainability.py

Functions for SHAP explainability.
"""

import shap
import matplotlib.pyplot as plt


def compute_shap_values(model, X):
    """
    Compute SHAP values for a trained tree-based model.
    """

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)

    return explainer, shap_values


def plot_shap_summary(shap_values, X):
    """
    Display SHAP summary plot.
    """

    shap.summary_plot(shap_values, X)


def plot_feature_importance(shap_values, X):
    """
    Display SHAP bar plot.
    """

    shap.summary_plot(
        shap_values,
        X,
        plot_type="bar"
    )