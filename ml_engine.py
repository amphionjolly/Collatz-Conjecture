import numpy as np
from sklearn.ensemble import IsolationForest

def detect_anomalies(n_val, steps_val, peaks_val):
    # Combine features: starting number, steps, and log of the peak
    features = np.column_stack((n_val, steps_val, np.log1p(peaks_val)))
    
    # Train the Machine Learning model to find outliers
    # contamination=0.01 means we are looking for the top 1% weirdest numbers
    model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
    model.fit(features)
    
    # Predict (-1 is an anomaly, 1 is normal)
    predictions = model.predict(features)
    
    # Extract the anomalous numbers
    anomalies = n_val[predictions == -1]
    
    return anomalies.tolist()
