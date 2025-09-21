# fastapi/app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc
import pandas as pd
import os

# Esquema de entrada con las features de Penguins
class Input(BaseModel):
    bill_length_mm: float
    bill_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float

app = FastAPI(title="Penguins RF Inference API")
_model = None

def get_model():
    global _model
    if _model is None:
        # Cargar el modelo desde elx Registry
        model_uri = os.getenv("MODEL_URI", "models:/penguins_rf/Production")
        _model = mlflow.pyfunc.load_model(model_uri)
    return _model

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/predict")
def predict(payload: Input):
    model = get_model()
    df = pd.DataFrame([payload.dict()])
    preds = model.predict(df)
    return {"prediction": preds.tolist()}
