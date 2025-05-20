CREATE TABLE fhir_resources (
    id SERIAL PRIMARY KEY,
    resource_type TEXT NOT NULL,
    resource JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
