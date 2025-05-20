from fhir.resources.observation import Observation
from fhir.resources.fhirdate import FHIRDate

obs = Observation(
    status="final",
    category=[{"coding": [{"system": "http://terminology.hl7.org/CodeSystem/observation-category",
                           "code": "vital-signs"}]}],
    code={"coding": [{"system": "http://loinc.org", "code": "15074-8", "display": "Glucose"}]},
    subject={"reference": "Patient/123"},
    effectiveDateTime=FHIRDate("2025-05-20T12:00:00Z"),
    valueQuantity={"value": 120, "unit": "mg/dL", "system": "http://unitsofmeasure.org", "code": "mg/dL"}
)

print(obs.json(indent=2))
