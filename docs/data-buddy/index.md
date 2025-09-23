# Data Buddy
## Data Buddy - Advanced Data Governance Application

Data Buddy integrates intelligent assistance directly into daily work — **recommending improvements, automating task sequences, and optimizing outputs** without exposing sensitive code or requiring external AI services.

Data Buddy is a Python–AI hybrid that uses the right engine for the job - Python for precision, AI for insight. Deterministic workloads (profiling, data-quality rules) run in Python; probabilistic tasks (catalog enrichment, insight discovery, anomaly detection) run in AI.

![AI Everyday Tasks](../_assets/ai-everyday.png)

---
A collection of utilities that speed up day-to-day data work across **profiling, quality, cataloging, anomalies, compliance, automation, conversational AI**, and **knowledge files**.

---

## Data Buddy Overview

**Data Buddy** is more than a toolkit — it’s a smart, AI-enhanced data companion.  
It performs profiling, quality checks, cataloging, anomaly detection, compliance validation, workflow automation, and more.  
It also **understands its own capabilities** and keeps a **log of actions**. Thanks to an embedded **kernel** that persists features used and interactions at each run, Data Buddy can **suggest relevant enhancements** to its functionality over time and adapt to evolving team needs — optimizing workflows and reducing manual effort.

---

## User Interface

Below is a screenshot of the **Data Buddy UI**, showing compliance checks, knowledge file integration, and the “Little Buddy” assistant:

![Data Buddy UI](../_assets/dbui.png)

---



## Quick links

- [:material-chart-bar: Data Profiling](data-profiling.md)
- [:material-shield-check: Data Quality](data-quality.md)
- [:material-book-open-variant: Data Cataloging](data-cataloging.md)
- [:material-alert-decagram: Anomaly Detection](anomaly-detection.md)
- [:material-scale-balance: Compliance](compliance.md)
- [:material-cog-sync: Workflow Automation](workflow-automation.md)
- [:material-robot-excited: Conversational AI](conversational-ai.md)
- [:material-file-document: Knowledge Files](knowledge-files.md)

---

## Quickstart

```bash
# examples – replace with your real CLI/module names when ready
python -m databuddy --help
python -m databuddy profile data/customers.parquet
