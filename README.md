# Predict Physical Quantities Using Machine Learning

## Project Overview

This project applies Machine Learning techniques to predict the superconducting critical temperature (Tc) of materials using experimentally measured material descriptors.

The objective is to investigate how computational methods can assist materials science research by learning relationships between physical properties and superconductivity.

---

## Dataset

Dataset: Superconductivity Dataset (UCI Machine Learning Repository)

Target Variable:
- Critical Temperature (Tc)

Number of Samples:
- 21,263 superconducting materials

Number of Features:
- 81 material descriptors

---

## Objectives

- Perform Exploratory Data Analysis (EDA)
- Build baseline Linear Regression model
- Develop Random Forest Regression model
- Compare model performance
- Perform Feature Importance Analysis
- Apply Cross Validation
- Perform Hyperparameter Tuning
- Analyze prediction residuals

---

## Machine Learning Workflow

1. Data Loading
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Selection
5. Train-Test Split
6. Linear Regression
7. Random Forest Regression
8. Model Evaluation
9. Cross Validation
10. Hyperparameter Optimization
11. Residual Analysis

---

## Results

| Model | R² Score |
|--------|----------|
| Linear Regression | 0.738 |
| Random Forest | 0.927 |
| Tuned Random Forest | 0.929 |

The Random Forest model significantly outperformed Linear Regression, demonstrating the ability of nonlinear ensemble methods to model complex relationships between material descriptors and superconducting critical temperature.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Jupyter Notebook

---

## Repository Structure

Predict-Physical-Quantities-Using-Machine-Learning/

data/

figures/

models/

notebooks/

src/

README.md

requirements.txt

LICENSE

---

## Future Work

- XGBoost Regression
- Neural Networks
- SHAP Explainability
- Materials Discovery Applications

---

## Author

Kaveri Yadav

M.Sc. Physics

Interested in Computational Materials Science, Machine Learning, AI Research, and Quantitative Modeling.