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

Data Description

The dataset consists of ICU patient records with hourly measurements of vital signs, lab results, and demographic details.

Key columns include:
Demographics: Age, Gender, Unit1 (CCU admission), Unit2 (CSRU admission), HospAdmTime (hospital admission time), ICULOS (ICU length of stay in hours).
Vital Signs: HR (Heart Rate), O2Sat (Oxygen Saturation), Temp (Temperature), SBP, MAP, DBP (blood pressures), Resp (Respiratory rate), EtCO2.
Lab Results: BaseExcess, HCO3, FiO2, pH, PaCO2, SaO2, AST, BUN, Alkalinephos, Calcium, Chloride, Creatinine, Bilirubin_direct, Glucose, Lactate, Magnesium, Phosphate, Potassium, Bilirubin_total, TroponinI, Hct, Hgb, PTT, WBC, Fibrinogen, Platelets.
Target Variable: SepsisLabel (0 = No Sepsis, 1 = Sepsis).
Identifiers: Patient_ID, Hour.


:

Preprocessing

Data Cleaning:
Removed duplicate/unnecessary columns (Unnamed: 0).
Handled missing values via imputation strategies.
Aggregated time-series patient records into meaningful summary statistics (mean, min, max, std, etc.).

Feature Engineering:
Added clinically relevant derived features (e.g., HR variability, SpO2 drop rates, etc.).
Incorporated temporal information such as ICU Length of Stay (ICULOS).

Class Balancing:
Addressed class imbalance using RandomUnderSampler to balance septic vs. non-septic cases.

Feature Selection:
Applied SelectFromModel with RandomForestClassifier to retain the most informative predictors.

Scaling (Not Applied):
No feature scaling (StandardScaler, MinMaxScaler, etc.) was applied.
Reason: The final model uses RandomForestClassifier, which is tree-based and invariant to feature scaling (it splits on thresholds of individual features rather than distance metrics).
Scaling would have been necessary for algorithms like Logistic Regression, SVM, or KNN, but it is unnecessary (and redundant) for RandomForest.

Model Selection Rationale

During experimentation, multiple approaches were tested, including:
Class weight balancing: class_weight = balanced with Random Forest (RF), XGBoost (XG), and Stacking Classifiers.
SMOTE (Synthetic Minority Oversampling): applied with RF, XG, and Stacking Classifiers.
Random Undersampling: applied with RF, XG, and Stacking Classifiers.

Observations:
Some methods (e.g., SMOTE, class weights, stacking) gave higher overall accuracy, but they also resulted in a high number of false negatives (missed sepsis cases).
In a medical setting, false negatives are far more dangerous than false positives, since missing a sepsis diagnosis can be life-threatening.

Final Choice:
Random Forest with Random Undersampling was selected because it struck the best balance between accuracy and minimizing false negatives.
The model was further tuned (hyperparameter optimization) and refined with feature selection to maximize clinical reliability and performance.

Model: Random Forest with Random Undersampling
Accuracy: 91.6%

Confusion Matrix:

[[10231  990]]  → True Negatives, False Positives  
[[ 183   697]]  → False Negatives, True Positives


Class-wise Metrics:

Non-Sepsis (0): Precision = 0.98, Recall = 0.91, F1-score = 0.94

Sepsis (1): Precision = 0.41, Recall = 0.79, F1-score = 0.54

Interpretation:
The model correctly identified 697 out of 880 sepsis cases (recall = 79%), with only 183 false negatives.
Precision for sepsis detection is moderate (41%), but this trade-off is clinically acceptable because minimizing missed sepsis cases is more important than reducing false alarms.
Overall, the model achieves a strong balance of accuracy and clinical reliability.


Deployment

The Early Sepsis Prediction app is deployed using Streamlit, allowing real-time predictions through an interactive web interface. Users can input patient vitals and instantly see the likelihood of sepsis.

The application can be run locally using Python and Streamlit, making it easy to use without complex server setups. All dependencies are listed in requirements.txt for quick installation.

Link

## Live Demo
Try the app here: [Early Sepsis Prediction]: https://early-sepsis-detection-z8ounzmxphwfvftctywpae.streamlit.app/

