🔬 Task 1: Machine Learning Model Development - Binary Classification for Cancer Prediction

This document presents the detailed execution of the Machine Learning Model Building task within the AI/ML Intern Assessment. The project demonstrates core competency in the end-to-end classification workflow utilizing the Scikit-learn library.

Project Deliverables

File Name

Description

Breast_cancer.py

Contains the complete Python script for the ML pipeline, including data handling, feature scaling, model training (Logistic Regression), and performance evaluation.

breast_cancer.csv

The input data source: the Breast Cancer Wisconsin (Diagnostic) Dataset.

Dataset Overview

Title: Breast Cancer Wisconsin (Diagnostic) Dataset

Description:
Breast cancer represents a significant global health challenge, accounting for approximately 25% of all cancer cases worldwide. The critical diagnostic task is the accurate binary classification of tumors as either Malignant (M - cancerous) or Benign (B - non-cancerous). This project leverages the dataset's 30 computed features, derived from digitized cell nucleus images, to develop a reliable predictive model.

Acknowledgements:
This dataset is sourced from the Kaggle repository.

Project Objectives

Data Preprocessing and Validation: To meticulously load, clean, and validate the dataset, ensuring appropriate encoding of the target variable and removal of non-contributory features.

Model Implementation: To construct robust classification models capable of predicting the tumor class (Malignant or Benign).

Hyperparameter Optimization and Comparison: To systematically fine-tune model hyperparameters and conduct a comparative analysis of evaluation metrics across multiple classification algorithms to determine the optimal diagnostic predictor.

Methodology and Current Status (Logistic Regression Baseline)

The initial implementation in Breast_cancer.py establishes a high-performance baseline utilizing the Logistic Regression classifier.

Step

Implementation Detail

Rationale

Data Preparation

Feature Scaling (StandardScaler), Stratified Train/Test Split (80/20)

Feature standardization is essential for ensuring all inputs contribute equitably to the model's optimization, particularly for gradient-based solvers. Stratification maintains the original class distribution across subsets.

Current Model

Logistic Regression

Employed as an interpretable and computationally efficient baseline, providing a clear reference point for subsequent advanced models.

Key Result

Accuracy $\approx 97.37\%$ and Malignant Precision $\approx 1.00$

The achievement of near-perfect precision in the Malignant class is highly significant, indicating robust performance in minimizing false-positive predictions within a crucial diagnostic context.

Future Development and Advanced Modeling

To fully achieve the project objectives and demonstrate comprehensive analytical capability, the following advanced steps are planned:

Support Vector Machine (SVM) Integration: The introduction of the Support Vector Machine (SVM) classifier will assess the benefit of non-linear decision boundaries on the dataset.

Systematic Optimization: Utilization of methods such as Grid Search in conjunction with K-Fold Cross-Validation to rigorously optimize all model hyperparameters (e.g., regularization parameters, kernel gamma). The primary focus of optimization will be maximizing the Recall score for the Malignant class to minimize False Negatives.

Performance Documentation: A final comparative report detailing the F1-score, Recall, and AUC-ROC curves for the final, tuned models will be generated for conclusive model selection.