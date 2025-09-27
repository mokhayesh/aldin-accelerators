# Sidecar Applications

> A **sidecar application** connects to an existing data source (data lake / warehouse / data mart), **collects data**, **performs an action**, and **redistributes the results** to another location or layer — **without** needing a heavy framework, pipeline, or config files.

## Why sidecar?
- :material-flash: **Fast to stand up** — point to a source, run an action, publish results.
- :material-swap-horizontal: **Decoupled** — doesn’t change the source system or require new ETL.
- :material-shield-check: **Governable** — results can be cataloged, quality-checked, and monitored.
- :material-docker: **Portable** — run locally, in a container, or as a scheduled job.

## High-level architecture

<figure markdown>
  ![](../_assets/sidecar-architecture.png){ .screenshot }
  <figcaption>Sidecar Applications / Accelerators — read from the production lake, perform an action, push curated results, catalog, and query.</figcaption>
</figure>

### How it works (typical flow)
1. **Source loads** data to the production lake / warehouse.
2. **Sidecar** connects and **collects** a working set (query, sample, partition).
3. **Action performed** (see examples below).
4. **Results are written** to a curated / golden layer or another target.
5. **Catalog & lineage** updated; results are queryable for BI/analytics and monitored by governance tools.

### Common actions
- **Data Profiling** · **Data Quality** · **Data Cataloging** · **Anomaly Detection**  
- **Compliance** · **Workflow Automation** · **Conversational AI / RAG** · **Knowledge Files**

## Implementation notes
- **Inputs:** table or file path(s) (CSV/Parquet), optional filters/partitions.  
- **Outputs:** curated tables/files, metrics, logs/evidence; registered in the catalog.  
- **Security:** least-privilege creds; classification-driven access on outputs.  
- **Ops:** schedule with a job runner or CI; emit metrics for health and value tracking.



