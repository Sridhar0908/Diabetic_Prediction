# Diabetic Prediction Project

## Overview
Binary classification to predict diabetes outcome using the Pima Indians Diabetes dataset.

## Folder structure
(see top of message)

## Setup
1. Create virtualenv:


2. Place the dataset `diabetes.csv` into `data/` OR run:


(If your environment has no internet, place `diabetes.csv` manually. Sample will be created otherwise.)

3. Preprocess data:


4. Train model:

python src/train_model.py --data_dir data/processed --out_dir models


5. Evaluate:


python src/evaluate.py --data_dir data/processed --model_dir models --out_dir reports/figures


6. Single-sample inference:


python src/inference.py --model_dir models --data_dir data/processed --sample "Pregnancies=2,Glucose=120,..."


## Deliverables
- code (this repo)
- report/report.pdf (convert report/project_report.md to PDF)
- slides/ (paste slides_content.txt into PowerPoint)

Email: admin@gmail.com
Password: admin