# Project 02: Wine Quality Prediction

**DecodeLabs Internship — Project 02**
**Author:** Rayyan Aamir

## Description

A machine learning classification pipeline that analyzes the physicochemical properties of red wine (acidity, sugar, alcohol content, etc.) to predict whether its quality is **Good** or **Bad/Average**. The project trains and compares three classification models: **Logistic Regression**, **K-Nearest Neighbors (KNN)**, and **Decision Tree**.

## Dataset

- **Source:** [UCI Machine Learning Repository — Wine Quality Data Set](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv)
- **Samples:** 1,599 red wine entries
- **Features:** 11 numerical physicochemical properties (fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free/total sulfur dioxide, density, pH, sulphates, alcohol)
- **Target:** Original `quality` score (3–8) is converted into a binary label:
  - `1` (Good) if `quality >= 6`
  - `0` (Bad/Average) otherwise

## Pipeline Overview

1. **Data Loading** — Reads the dataset directly from the UCI repository via URL.
2. **Exploratory Data Analysis (EDA)** — Generates a correlation heatmap to visualize relationships between features.
3. **Preprocessing** — Splits data into 80% training / 20% testing (stratified), then scales features using `StandardScaler`.
4. **Model Training & Evaluation** — Trains three classifiers and evaluates each using:
   - Accuracy score
   - Classification report (precision, recall, F1-score)
   - Confusion matrix (visualized as a heatmap)
5. **Model Comparison** — Produces a bar chart comparing the accuracy of all three models.

## Models Used

| Model | Configuration |
|---|---|
| Logistic Regression | `max_iter=1000` |
| K-Nearest Neighbors | `n_neighbors=7` |
| Decision Tree | `max_depth=5`, `random_state=42` |

## Requirements

```
pandas>=2.2.0
numpy>=1.26.0
scikit-learn>=1.4.0
matplotlib>=3.8.0
seaborn>=0.13.0
```

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run the script (requires an internet connection to fetch the dataset):

```bash
python wine-quality-prediction.py
```

Or open and run the notebook version:

```
Wine-Quality-Prediction.ipynb
```

## Results

Each model's accuracy and classification metrics are printed to the console, along with confusion matrix visualizations. A final bar chart summarizes and compares the accuracy of all three models side by side, based on the current run:

| Model | Accuracy |
|---|---|
| Logistic Regression | ~74% |
| K-Nearest Neighbors (KNN) | ~75% |
| Decision Tree | ~73% |

## Project Structure

```
Project-02/
├── Wine-Quality-Prediction.ipynb
├── wine-quality-prediction.py
└── requirements.txt
```

## Possible Improvements

- Hyperparameter tuning (e.g. `GridSearchCV`) for each model
- Try ensemble methods (Random Forest, Gradient Boosting)
- Address class imbalance with techniques like SMOTE
- Feature engineering / selection to improve predictive performance