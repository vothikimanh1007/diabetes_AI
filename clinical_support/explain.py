import shap
import lightgbm as lgb
import numpy as np

model = lgb.Booster(model_file='lightgbm_model.txt')

X_example = np.array([[120, 25, 45]])  # Example features: glucose, bmi, age

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_example)

print("SHAP values:", shap_values)
