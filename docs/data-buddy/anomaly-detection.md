# Anomaly Detection

![Anomaly Detection](_assets/anomaly-detection.png)

The **Anomaly Detection** module analyzes connected or uploaded datasets to identify irregularities, inconsistencies, or suspicious patterns that may indicate errors, compliance issues, or risks. Beyond simply flagging anomalies, it also prescribes actionable recommendations for remediation, empowering teams to quickly address issues, maintain trust in their data, and continuously improve processes.



## Tasks
- Z-score/IQR outliers  
- Seasonal/level shifts  
- Drift vs. baseline  

## Example
```bash
python -m databuddy anomalies detect --metric dq_score --window 30 --method zscore
