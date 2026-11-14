# Healthcare ML DevOps POE Project

## Problem statement
Build a small healthcare machine-learning application that classifies a breast tumour as benign or malignant from numerical measurements. This is an educational demonstration, not a medical diagnostic tool.

## Dataset
Scikit-learn's built-in Wisconsin Breast Cancer dataset:
- 569 samples
- 30 numerical input features
- Target: malignant (0) or benign (1)
- No separate dataset download is required.

## Tools and purpose
- Python: programming language.
- Pandas: data handling.
- Scikit-learn: preprocessing, training and evaluation.
- MLflow: experiment tracking (parameters, metrics and model).
- FastAPI: creates REST API endpoints.
- Uvicorn: runs the FastAPI application.
- Pytest: runs automated tests.
- HTTPX: HTTP client dependency used by FastAPI TestClient.
- Evidently: compares reference and current data and creates a drift report.
- Git/GitHub: version control and code hosting.
- Jenkins: automates install, training, testing and monitoring stages.
- VS Code, Python Extension Pack, Pylance and GitLens: development support.
- Java JDK: required to run Jenkins.

## Run on Windows
Open a terminal in this project folder.

```powershell
py -3.11 -m venv .venv
.venv\\Scripts\\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python train.py
python -m pytest -v
python scripts/monitor.py
uvicorn app.main:app --reload
```

Open these URLs in a browser:
- API home: http://127.0.0.1:8000/
- Health check: http://127.0.0.1:8000/health
- Interactive API docs: http://127.0.0.1:8000/docs

## Try a prediction
1. Open http://127.0.0.1:8000/docs
2. Expand POST `/predict`.
3. Use a sample with all 30 features. The easiest way to obtain a valid sample is to run this in a separate Python terminal:

```python
from sklearn.datasets import load_breast_cancer
import json
d = load_breast_cancer(as_frame=True)
print(json.dumps({"features": d.data.iloc[0].to_dict()}, indent=2))
```

4. Copy the printed JSON into the request body and click Execute.

## Git and GitHub
```powershell
git init
git add .
git commit -m "Initial healthcare MLOps project"
```
Create an empty GitHub repository, then use the repository URL shown by GitHub:
```powershell
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## Jenkins
This project includes a Jenkinsfile for a Windows Jenkins agent. Configure Jenkins with a Windows agent that has Python installed, connect the GitHub repository, and create a Pipeline job that uses the repository's Jenkinsfile. Jenkins runs dependency installation, training, pytest and Evidently monitoring in sequence.

## Project flow
Dataset -> Pandas -> train/test split -> StandardScaler + Logistic Regression -> MLflow tracking
                                                    |
                                                    v
                                      FastAPI + Uvicorn -> prediction API
                                                    |
                                                    v
                                         Pytest + HTTPX tests
                                                    |
                                                    v
                              Evidently reference/current data drift report
                                                    |
                                                    v
                                     GitHub source control + Jenkins CI

## Important notes
- Run `python train.py` before starting the API or tests.
- The test suite trains the model once at the start of the test session.
- The Evidently report compares the saved training data with the held-out test data as a demonstration. In a real deployment, current production data should be collected responsibly and compared with a reference dataset.
- MLflow output is stored locally in the `mlruns` folder. Start the UI with `mlflow ui` and open http://127.0.0.1:5000.
- This project uses pinned package versions to make the lab setup more reproducible. Use Python 3.11 for the prepared environment.
