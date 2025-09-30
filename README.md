# AI Development Workflow Assignment

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)

This repository contains all materials for the **AI for Software Engineering** assignment on the **AI Development Workflow**.  
It includes notebooks, scripts, sample datasets, a PDF report, and visual diagrams demonstrating the AI workflow from problem definition to deployment.

---

## Repository Structure
```
AI_Development_Workflow_Assignment/
│
├── notebooks/
│ ├── student_dropout_prediction.ipynb # Notebook for student dropout prediction case study
│ └── patient_readmission_prediction.ipynb # Notebook for patient readmission prediction case study
│
├── scripts/
│ ├── data_preprocessing.py # Script for data cleaning and preprocessing
│ ├── train_model.py # Script to train machine learning models
│ ├── evaluate_model.py # Script to evaluate model performance
│ └── api_integration_stub.py # Example API integration for model inference
│
├── data/
│ ├── student_data_sample.csv # Sample dataset for student dropout prediction
│ └── patient_data_sample.csv # Sample dataset for patient readmission prediction
│
├── PDF_Report/
│ └── AI_Workflow_Assignment.pdf # Full PDF report of the assignment
│
├── diagrams/
│ └── AI_Workflow_Flowchart.png # Flowchart of the AI development workflow
│
├── requirements.txt # Python dependencies
└── README.md # This file
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AI_Development_Workflow_Assignment.git
cd AI_Development_Workflow_Assignment
```
### 2. Install Dependencies
It is recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### Usage Instructions
### 1. Run Jupyter Notebooks
Open the notebooks and execute all cells:

- notebooks/student_dropout_prediction.ipynb – Preprocessing, model training, and evaluation for student dropout prediction.

- notebooks/patient_readmission_prediction.ipynb – Preprocessing, model training, and evaluation for patient readmission prediction.

```bash
jupyter notebook
```
### 2. Run Scripts (Optional)
You can run the scripts independently for data processing, model training, or evaluation.

Preprocess Data
```bash
python scripts/data_preprocessing.py
```
Train Models
```bash
python scripts/train_model.py
```
Evaluate Models
```bash
python scripts/evaluate_model.py
```
### 3. API Integration Testing
The api_integration_stub.py file demonstrates how to send JSON payloads to the /predict endpoint for inference:

```bash
python scripts/api_integration_stub.py
```
Note: This is a stub for demonstration; ensure the API server is running if integrating with a real endpoint.

### Project Highlights
- Student Dropout Prediction: Predict high-risk students for online learning platforms.

- Patient Readmission Prediction: Predict 30-day hospital readmission risk.

- Data Preprocessing Pipelines: Handling missing data, encoding, normalization, and feature engineering.

- Model Training & Evaluation: Random Forest and Gradient Boosted Trees with hyperparameter tuning.

- Visualization: Flowcharts and diagrams to illustrate the AI workflow.

- Documentation: Full Markdown-based PDF report included in PDF_Report/.


### License
This project is for educational purposes. Please cite appropriately if reused