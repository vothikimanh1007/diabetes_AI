from fastapi import FastAPI
import lightgbm as lgb
import numpy as np

app = FastAPI()
model = lgb.Booster(model_file='lightgbm_model.txt')  # load your trained model

@app.post("/predict")
async def predict(features: dict):
    X = np.array([features[k] for k in sorted(features.keys())]).reshape(1, -1)
    pred = model.predict(X)[0]
    return {"risk_score": float(pred)}
