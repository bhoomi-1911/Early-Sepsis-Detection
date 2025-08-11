# Early-Sepsis-Detection
This project aims to predict the onset of sepsis in ICU patients using clinical data such as vital signs, laboratory results, and demographic information. Sepsis is a life-threatening condition caused by the body’s extreme response to infection, and early detection can significantly improve patient outcomes.

Early Sepsis Detection from ICU Data

Overview

Sepsis is a life-threatening condition that arises when the body’s response to infection causes tissue damage and organ failure. Early detection is critical — each hour of delay in diagnosis can increase mortality risk.
This project predicts the onset of sepsis in ICU patients using vital signs, lab test results, and demographic data. It applies data preprocessing, feature engineering, and machine learning to classify patients as at risk or not. The final model is deployed as an interactive Streamlit application for real-time predictions.

Dataset

This project uses the PhysioNet Computing in Cardiology Challenge 2019 dataset, originally sourced from:
eICU Collaborative Research Database
MIMIC-III Clinical Database

Features:

44 clinical variables recorded hourly (vital signs, labs, demographics)
Target variable: SepsisLabel (0 = No Sepsis, 1 = Sepsis)
~more than 1.5 million rows from ICU stays of multiple patients

Tech Stack

Python: pandas, numpy, scikit-learn, matplotlib, seaborn
Machine Learning: Logistic Regression, Random Forest, SK Learn
Streamlit: For interactive UI
Google Colab: For development and analysis
GitHub: For version control and project sharing

