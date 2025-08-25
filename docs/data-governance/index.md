# Data Governance

Data Governance aligns people, process, and technology so data is **discoverable, trustworthy, compliant, and usable**.  
Use this page as a quick brief for stakeholders and a map to the related accelerators.

## At a glance

<div class="grid cards" markdown>

- :material-book-open-variant: **Metadata Management**  
  Build and maintain your catalog: capture technical + business metadata, lineage, and policies.

- :material-chart-bar: **Data Profiling**  
  Rapidly analyze datasets to surface structure, patterns, and outliers; inform rule design.

- :material-shield-check: **Data Quality**  
  Dimensions, rules, SLAs, monitoring, and scorecards to keep data reliable.

- :material-scale-balance: **Data Compliance**  
  Controls and policies by geography/domain (e.g., GDPR, CCPA, GLBA); automate evidence.

- :material-archive-lock: **Data Retention**  
  Lifecycle policies for archiving/disposing data; support “right-to-erase” requests.

- :material-account-multiple-check: **Master Data Management (MDM)**  
  Golden records for key entities; survivorship rules; improved cross-system consistency.

</div>

---

## Capability matrix

| Capability / Offerings | What It Means | Who’s Involved | Why It Matters |
|---|---|---|---|
| **Metadata Management** | Create, update, delete metadata (data about data); build & maintain a data catalog. | Data Steward / Catalog Manager | Enables users to find & understand data; drives self-service analytics. |
| **Data Profiling** | Sample analysis to surface structure, patterns, outliers; full-dataset assessment across dimensions (completeness, accuracy, uniqueness, validity, timeliness); custom rule definition. | Data Analyst / Steward | Quick health check; guides deeper quality efforts. |
| **Data Quality** | Dimensions, rules, SLAs; continuous monitoring and scorecards. | Data Quality Lead / Engineer | Ensures analytics & ML models use reliable data; reduces risk of bad decisions. |
| **Data Compliance** | Policies & controls by geography/domain (e.g., CCPA, GDPR, GLBA). | Legal & Compliance Team | Avoids fines & lawsuits; supports rights to know/share/port/delete. |
| **Data Retention** | Lifecycle policies for archiving/disposing data, often under compliance. | Records Manager / IT | Meets legal mandates; simplifies “right-to-erase” requests. |
| **Master Data Management (MDM)** | Centralize & reconcile critical entity data; golden record creation. | MDM Lead / Architect | Single source of truth; improves cross-system consistency. |

---

## Assessment questions (use in discovery workshops)

**How to use.** Ask each question, capture evidence/links, and score **0-3** for a quick maturity snapshot.

**Quick-score rubric**

| Score | Description |
|---:|---|
| 0 | Not in place |
| 1 | Ad hoc / informal |
| 2 | Defined / documented |
| 3 | Managed / automated & measured |

### The questions

??? info "1) Metadata enrichment"
    **Ask:** How is metadata enriched today (classifications, sensitivity/privacy tags, policies)? Who owns and maintains it?  
    **Evidence to collect:** screenshots or APIs of catalog enrichments; stewards by domain; update cadence; policy mapping.  
    **Score guide:** 0=no enrichment • 1=manual/spotty • 2=stewarded & repeatable • 3=policy-driven & automated.

??? info "2) Source prioritization & CDEs"
    **Ask:** Do you have a prioritized inventory of data sources and defined **Critical Data Elements (CDEs)**? What criteria are used?  
    **Evidence:** source list, ranking criteria (risk, value, usage), approved CDE list per domain.  
    **Score:** 0=none • 1=informal • 2=defined + criteria • 3=governed with periodic review.

??? info "3) Knowledge capture"
    **Ask:** Where is tacit/tribal knowledge documented today, and should it be formalized in the catalog?  
    **Evidence:** links to Confluence/Notion/SharePoint; example business definitions; gaps.  
    **Score:** 0=nowhere • 1=wiki scattered • 2=catalog integrated • 3=workflow to curate & approve.

??? info "4) Lineage"
    **Ask:** How is lineage captured (technical & business)? What’s the coverage, depth, and refresh cadence?  
    **Evidence:** tool outputs, % coverage for key platforms, refresh schedule, impact analysis examples.  
    **Score:** 0=none • 1=partial/manual • 2=tool-based with coverage targets • 3=automated w/ CI/CD harvesting.

??? info "5) Data quality"
    **Ask:** Are DQ rules configurable and mapped to dimensions (accuracy, completeness, timeliness, consistency, validity, uniqueness)? How are thresholds, exceptions, and monitoring handled?  
    **Evidence:** rule repo, SLA thresholds, exception workflow, alerts/dashboards.  
    **Score:** 0=none • 1=ad hoc • 2=standardized dimensions & SLAs • 3=continuous monitoring + breach escalation.

??? info "6) Stewardship & ownership"
    **Ask:** Are data owners/stewards defined and assigned with clear RACI and capacity to act?  
    **Evidence:** steward registry, RACI by domain/product, time allocation.  
    **Score:** 0=unknown • 1=names only • 2=RACI formalized • 3=accountabilities measured (SLOs).

??? info "7) Governance operating model"
    **Ask:** Are councils/committees, roles/responsibilities, decision rights, and change processes established? How are policies approved and enforced?  
    **Evidence:** charters, decision logs, policy lifecycle, tooling for enforcement.  
    **Score:** 0=none • 1=informal • 2=documented & running • 3=audited with KPIs.

??? info "8) AI readiness"
    **Ask:** What is the organization’s AI readiness/maturity (data availability, governance controls, risk/compliance guardrails, model oversight)?  
    **Evidence:** approved datasets for AI, PII handling, usage policies, model review gates, red-teaming practices.  
    **Score:** 0=unknown • 1=pilot-only guardrails • 2=enterprise controls • 3=governed lifecycle (from data to model).

??? info "9) Compliance & risk"
    **Ask:** Which regulations and internal policies drive governance requirements? How are controls evidenced and audited?  
    **Evidence:** control library mapped to regs, evidence collection, audit cadence, exceptions register.  
    **Score:** 0=unmapped • 1=manual audits • 2=mapped with evidence • 3=continuous assurance & attestations.

??? info "10) Metrics & value"
    **Ask:** What KPIs are tracked (policy coverage, DQ scores, issue MTTR, adoption)? How is value realized and reported?  
    **Evidence:** KPI list, dashboards, executive reporting, value stories.  
    **Score:** 0=none • 1=lagging only • 2=standard KPI set • 3=targets with actions & ROI.

??? info "11) Access & security"
    **Ask:** How are classification-driven access controls, segregation of duties, and retention/disposition managed?  
    **Evidence:** RBAC/ABAC policies, masking/row-level security, SoD rules, retention schedules.  
    **Score:** 0=local rules • 1=policy but uneven • 2=centralized enforcement • 3=auto-provisioning + periodic recert.

??? info "12) Enablement & adoption"
    **Ask:** How are stakeholders trained and supported (playbooks, office hours, communities of practice)? How is feedback incorporated?  
    **Evidence:** training plans, playbooks/templates, engagement metrics, feedback backlog → policy updates.  
    **Score:** 0=none • 1=one-off sessions • 2=programmatic enablement • 3=measured adoption with continuous improvement.

---

### Quick worksheet (copy/paste)

- [ ] 1. Metadata enrichment — Score: `0/1/2/3` — Notes:  
- [ ] 2. Source prioritization & CDEs — Score: `0/1/2/3` — Notes:  
- [ ] 3. Knowledge capture — Score: `0/1/2/3` — Notes:  
- [ ] 4. Lineage — Score: `0/1/2/3` — Notes:  
- [ ] 5. Data quality — Score: `0/1/2/3` — Notes:  
- [ ] 6. Stewardship & ownership — Score: `0/1/2/3` — Notes:  
- [ ] 7. Operating model — Score: `0/1/2/3` — Notes:  
- [ ] 8. AI readiness — Score: `0/1/2/3` — Notes:  
- [ ] 9. Compliance & risk — Score: `0/1/2/3` — Notes:  
- [ ] 10. Metrics & value — Score: `0/1/2/3` — Notes:  
- [ ] 11. Access & security — Score: `0/1/2/3` — Notes:  
- [ ] 12. Enablement & adoption — Score: `0/1/2/3` — Notes:  

!!! tip "Next steps"
    Use the scores to pick **top 2–3 gaps** and jump to the matching accelerator:
    * **Architecture** for policy-as-code, security baselines, platform guardrails  
    * **Data Buddy** for profiling & quick evidence gathering  
    * **Synthetic Data Generator** for rule seeding & quality experiments  
    * **MDM** for entity governance and survivorship
