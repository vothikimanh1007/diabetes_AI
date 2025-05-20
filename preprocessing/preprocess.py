import pandas as pd
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTE

df = pd.read_csv('data.csv')  # Your dataset

imputer = SimpleImputer(strategy='median')
X_imputed = imputer.fit_transform(df.drop('diabetes', axis=1))
y = df['diabetes']

smote = SMOTE()
X_res, y_res = smote.fit_resample(X_imputed, y)

print("Resampled class counts:", pd.Series(y_res).value_counts())
