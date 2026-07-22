# Predicting Superconducting Critical Temperature Using Machine Learning

## Project Overview

This project applies machine learning techniques to predict the superconducting critical temperature (Tc) of materials using experimentally measured material descriptors from the UCI Superconductivity Dataset.

Multiple regression algorithms were developed and compared, including Linear Regression, Random Forest, Tuned Random Forest, and XGBoost. Model predictions were further interpreted using SHAP (SHapley Additive exPlanations) to improve transparency and understand the influence of different material properties on the predicted critical temperature.

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
- Build a baseline Linear Regression model
- Train Random Forest and XGBoost regression models
- Optimize model performance using hyperparameter tuning
- Evaluate models using MAE, RMSE, and R² score
- Compare multiple machine learning algorithms
- Interpret predictions using SHAP explainability
- Save trained models for future deployment

---

## Machine Learning Workflow

1. Data Loading
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Train-Test Split
6. Linear Regression
7. Random Forest Regression
8. Hyperparameter Tuning
9. XGBoost Regression
10. Model Evaluation
11. SHAP Explainability
12. Save Models and Results

---

## Model Performance

| Model | MAE | RMSE | R² Score |
|--------|----:|------:|---------:|
| Linear Regression | 13.2105 | 17.3784 | 0.7376 |
| Random Forest | 5.1621 | 9.1423 | 0.9274 |
| Tuned Random Forest | **5.1732** | **9.0468** | **0.9289** |
| XGBoost | 5.8431 | 9.3378 | 0.9242 |

The Tuned Random Forest achieved the best predictive performance, explaining approximately 92.9% of the variance in the superconducting critical temperature. XGBoost also demonstrated strong performance, while Linear Regression served as an effective baseline model.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Jupyter Notebook
- XGBoost
- SHAP
- Git
- GitHub

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

- Develop a Streamlit web application for prediction
- Refactor notebook code into reusable Python modules
- Investigate deep learning approaches for superconductivity prediction
- Explore physics-informed machine learning methods
- Improve feature engineering and model optimization

---

## Author

Kaveri Yadav

M.Sc. Physics

Interested in Computational Materials Science, Machine Learning, AI Research, and Quantitative Modeling.