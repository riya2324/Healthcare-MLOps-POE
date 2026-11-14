from pathlib import Path
import json
import joblib
import mlflow
import mlflow.sklearn
import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

ROOT = Path(__file__).resolve().parent
ARTIFACTS = ROOT / "artifacts"
ARTIFACTS.mkdir(exist_ok=True)

def train_model():
    # Load the built-in Wisconsin Breast Cancer dataset.
    dataset = load_breast_cancer(as_frame=True)
    X = dataset.data
    y = dataset.target
    feature_names = list(X.columns)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=2000))
    ])
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    metrics = {
        "accuracy": float(accuracy_score(y_test, predictions)),
        "precision_malignant": float(precision_score(y_test, predictions, pos_label=0)),
        "recall_malignant": float(recall_score(y_test, predictions, pos_label=0))
    }

    joblib.dump(model, ARTIFACTS / "model.joblib")
    X_train.to_csv(ARTIFACTS / "reference_data.csv", index=False)
    X_test.to_csv(ARTIFACTS / "current_data.csv", index=False)
    (ARTIFACTS / "feature_names.json").write_text(
        json.dumps(feature_names, indent=2), encoding="utf-8"
    )

    # MLflow records parameters, metrics and the trained model.
    mlflow.set_tracking_uri((ROOT / "mlruns").as_uri())
    mlflow.set_experiment("Healthcare-Breast-Cancer-Classification")
    with mlflow.start_run():
        mlflow.log_param("model", "LogisticRegression")
        mlflow.log_param("test_size", 0.2)
        mlflow.log_param("random_state", 42)
        mlflow.log_metrics(metrics)
        mlflow.sklearn.log_model(model, artifact_path="model")

    print("Training completed.")
    print("Metrics:", metrics)
    print("Saved model and data in the artifacts folder.")
    return metrics

if __name__ == "__main__":
    train_model()
