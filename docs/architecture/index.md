# Data Architecture

**Data Governance** is the **overarching framework** that defines how data is **owned, managed, accessed, protected, and measured**.  
**Data Architecture** is the **technical foundation** that implements those policies in practice—defining how platforms, integrations, and patterns are structured so the organization can deliver **reusable, scalable, repeatable, and future-proof** solutions.

<div class="grid cards" markdown>

- :material-shield-crown: **Governance sets the rules**
  - Ownership & stewardship (RACI)
  - Policies (privacy, retention, classification)
  - SLAs/SLOs (quality, timeliness)
  - Compliance & audit evidence

- :material-domain: **Architecture makes them real**
  - Platform & storage layout (raw → curated → analytic)
  - Integration patterns (batch, CDC, streaming, sidecar)
  - Cross-cutting controls (security, lineage, observability)
  - Interfaces & contracts (schemas, APIs, data products)

</div>

---

## Architecture principles for great governance

- **Policy-first design** — technical choices must enforce classification, access, retention, and quality objectives.  
- **Separation of concerns** — ingest, process, serve, and govern are modular and independently scalable.  
- **Standard patterns** — a small set of approved blueprints (below) to speed delivery and reduce drift.  
- **Product mindset** — datasets are **products** with clear contracts, SLAs, and owners.  
- **Evidence by default** — every job emits lineage, metrics, and artifacts suitable for audit.  
- **Cloud-agnostic where possible** — abstractions (contracts, templates) outlive any one tool.

---

## Layers & responsibilities

- **Ingestion** – file drops, APIs, streaming, and CDC.  
- **Storage & refinement** – Raw/Bronze → Conformed/Silver → Curated/Gold → Analytic/Platinum.  
- **Serving** – SQL engines/semantic layers, BI, reverse ETL.  
- **Cross-cutting** – identity & access, encryption, metadata catalog, lineage, data quality, monitoring, cost controls.

> Tip: make **governance controls** (classification, masking, DQ thresholds, retention) declarative and versioned so they can be applied consistently across layers.

---

## Standard patterns & accelerators

Use these patterns to bake governance into delivery while staying fast:

- **Sidecar application** — connect to an existing source, perform an action, and publish results without new pipelines.  
  [:octicons-arrow-right-16: Learn more](../sidecar-applications/index.md)

- **Data Buddy** — profiling, **Data Quality** rules, **Cataloging**, anomalies, compliance evidence, conversational AI.  
  [:octicons-arrow-right-16: Learn more](../data-buddy/index.md)

- **MDM Hub** — match/merge to **Golden Records**; redistribute to sources and curated zones.  
  [:octicons-arrow-right-16: Learn more](../mdm/index.md)

- **Code Converter** — modernize SQL logic consistently (e.g., PL/SQL → Spark SQL).  
  [:octicons-arrow-right-16: Learn more](../code-converter/index.md)

- **Synthetic Data Generator** — privacy-preserving test data for repeatable pipelines and QA.  
  [:octicons-arrow-right-16: Learn more](../synthetic-data-generator/index.md)

---

## Standards & interfaces

- **Data product contract** – name, domain, schema, semantics, SLAs, lineage, owners, access policy.  
- **Schema & API conventions** – naming, versioning, deprecation, backward compatibility.  
- **Security** – classification → policy (masking, row filters), KMS encryption, least privilege.  
- **Quality** – rule packs per dimension (completeness, validity, uniqueness, timeliness, accuracy, consistency).  
- **Observability** – metrics (freshness, volume, schema change), logs, alerts, and SLOs.  
- **CI/CD for data** – tests, policy checks, and contract validation in every change.

---

## Reference integrations (tool-agnostic)

- **Connectors**: file/object, JDBC, message/stream, REST.  
- **Processing**: ELT/ETL engines, notebooks, batch & streaming frameworks.  
- **Catalog & lineage**: central metadata with APIs for write-back from jobs.  
- **Orchestration**: schedules, dependencies, approvals, and evidence bundle publishing.  
- **Serving**: query engines/semantic layers and BI tools with row/column-level security.

---

## Readiness checklist

- Architecture document includes **domain, data products, contracts, SLAs**, and **controls**.  
- **Lineage** and **DQ rule packs** defined and stored with the product.  
- **Access policies** (classification → masking/filters) codified and tested.  
- **Monitoring** and **alerts** wired to SLAs/SLOs; cost guardrails in place.  
- Evidence (profiles, scorecards, catalogs, policies) **exportable** for audit.

---

### Where to go next

- See the **Data Governance overview** for principles and capability map.  
  [:octicons-arrow-right-16: Data Governance](../data-governance/index.md)

- Browse the **accelerators** to apply these patterns quickly.  
  [:octicons-arrow-right-16: Explore accelerators](../index.md#accelerators)
