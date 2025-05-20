import React, { useState } from 'react';

function App() {
  const [risk, setRisk] = useState(null);

  const getPrediction = async () => {
    const response = await fetch('http://localhost:8000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ glucose: 120, bmi: 25, age: 45 })
    });
    const data = await response.json();
    setRisk(data.risk_score);
  };

  return (
    <div>
      <h1>Diabetes Risk Prediction</h1>
      <button onClick={getPrediction}>Get Risk Score</button>
      {risk && <p>Risk Score: {risk.toFixed(2)}</p>}
    </div>
  );
}

export default App;
