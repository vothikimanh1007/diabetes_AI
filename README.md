# Diabetes AI Integration Project

This repository contains a modular prototype for integrating AI-driven early diabetes detection into clinical workflows.

Modules:

- ingestion: Receives wearable data (e.g., Dexcom CGM)
- fhir_server: Create and manage FHIR resources
- data_storage: PostgreSQL DB schema for FHIR
- preprocessing: Data cleaning, SMOTE, feature selection
- model_serving: Serve Transformer + LightGBM prediction API
- clinical_support: SHAP explanations, alerts
- frontend: React app UI for clinicians and patients

Instructions:

Each module has its own requirements.txt. Install with pip or npm.

Start backend servers (FastAPI) and frontend separately for full integration.

