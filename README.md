# Predicting Superconducting Critical Temperature Using Machine Learning

## Project Overview

This project develops and compares multiple machine learning regression models to predict the superconducting critical temperature (Tc) of materials using experimentally measured material descriptors from the UCI Superconductivity Dataset.

The predictive performance of Linear Regression, Random Forest, Tuned Random Forest, and XGBoost is evaluated using standard regression metrics. The best-performing model is further interpreted using SHAP (SHapley Additive exPlanations) to identify the most influential material descriptors and improve model transparency.

---

## Dataset

**Dataset:** Superconductivity Dataset (UCI Machine Learning Repository)

**Target Variable**
- Critical Temperature (Tc)

**Number of Samples**
- 21,263 superconducting materials

**Number of Features**
- 81 material descriptors

---

## Objectives

- Perform Exploratory Data Analysis (EDA)
- Develop a baseline Linear Regression model
- Train Random Forest and XGBoost regression models
- Improve model performance through hyperparameter optimization
- Evaluate models using MAE, RMSE, and R² score
- Compare the predictive performance of multiple machine learning models
- Interpret model predictions using SHAP explainability
- Save trained models for future deployment

---

## Machine Learning Workflow

1. Import Libraries
2. Load Dataset
3. Dataset Overview
4. Exploratory Data Analysis (EDA)
5. Data Preprocessing
6. Model Training
   - Linear Regression
   - Random Forest Regression
   - Hyperparameter Optimization
   - XGBoost Regression
7. Model Comparison
8. Model Explainability (SHAP)
9. Conclusions

---

## Model Performance

| Model | MAE | RMSE | R² Score |
|--------|----:|------:|---------:|
| Linear Regression | 13.2105 | 17.3784 | 0.7376 |
| Random Forest | 5.1621 | 9.1423 | 0.9274 |
| Tuned Random Forest | **5.1732** | **9.0468** | **0.9289** |
| XGBoost | 5.8431 | 9.3378 | 0.9242 |

The optimized Random Forest model achieved the best predictive performance with an **R² score of 0.9289**, demonstrating its ability to accurately model the nonlinear relationships between material descriptors and the superconducting critical temperature. XGBoost also produced strong results, while Linear Regression served as an effective baseline model.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- XGBoost
- SHAP
- Joblib
- Jupyter Notebook
- Git
- GitHub

---

## Repository Structure

```text
Predict-Physical-Quantities-Using-Machine-Learning/
│
├── data/
├── figures/
├── models/
├── notebooks/
├── src/
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Future Work

- Develop a Streamlit web application for interactive predictions
- Investigate deep learning approaches for superconductivity prediction
- Explore physics-informed machine learning methods
- Improve feature engineering and hyperparameter optimization
- Extend the framework to predict other material properties

---

## Author

**Kaveri Yadav**

**M.Sc. Physics**

**Research Interests**

- Computational Materials Science
- Machine Learning
- Explainable AI (XAI)
- AI Research
- Quantitative Modeling