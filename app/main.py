from pathlib import Path
import json
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

ROOT = Path(__file__).resolve().parent.parent
ARTIFACTS = ROOT / "artifacts"
MODEL_PATH = ARTIFACTS / "model.joblib"
FEATURES_PATH = ARTIFACTS / "feature_names.json"

app = FastAPI(title="Healthcare Tumour Classification API")

class PredictionRequest(BaseModel):
    features: dict[str, float]

def load_model_and_features():
    if not MODEL_PATH.exists() or not FEATURES_PATH.exists():
        raise RuntimeError("Model files not found. Run: python train.py")
    model = joblib.load(MODEL_PATH)
    feature_names = json.loads(FEATURES_PATH.read_text(encoding="utf-8"))
    return model, feature_names

@app.get("/")
def home():
    return {"message": "Healthcare ML API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(request: PredictionRequest):
    try:
        model, feature_names = load_model_and_features()
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc))

    missing = [name for name in feature_names if name not in request.features]
    if missing:
        raise HTTPException(
            status_code=400,
            detail=f"Missing features. Expected {len(feature_names)} features."
        )

    row = {name: request.features[name] for name in feature_names}
    input_df = pd.DataFrame([row], columns=feature_names)
    prediction = int(model.predict(input_df)[0])
    label = "malignant" if prediction == 0 else "benign"
    return {"prediction": prediction, "class_name": label}
