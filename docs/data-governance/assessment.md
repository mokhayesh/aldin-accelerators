# Assessment Questions

Use these questions in discovery workshops to baseline governance maturity.  
Capture evidence/links and score **0â€“3** for each area.

## Quick-score rubric

| Score | Description |
|---:|---|
| 0 | Not in place |
| 1 | Ad hoc / informal |
| 2 | Defined / documented |
| 3 | Managed / automated & measured |

## The questions

??? info "1) Metadata enrichment"
    **Ask:** How is metadata enriched today (classifications, sensitivity/privacy tags, policies)? Who owns and maintains it?  
    **Evidence:** catalog enrichments; stewards by domain; update cadence; policy mapping.  
    **Score:** 0=no enrichment â€¢ 1=manual/spotty â€¢ 2=stewarded & repeatable â€¢ 3=policy-driven & automated.

??? info "2) Source prioritization & CDEs"
    **Ask:** Do you have a prioritized inventory of data sources and defined **Critical Data Elements (CDEs)**? What criteria are used?  
    **Evidence:** source list; ranking criteria (risk, value, usage); approved CDE list per domain.  
    **Score:** 0=none â€¢ 1=informal â€¢ 2=defined + criteria â€¢ 3=governed with periodic review.

??? info "3) Knowledge capture"
    **Ask:** Where is tacit/tribal knowledge documented today, and should it be formalized in the data catalog?  
    **Evidence:** links to Confluence/Notion/SharePoint; business definitions; gaps.  
    **Score:** 0=nowhere â€¢ 1=wiki scattered â€¢ 2=catalog integrated â€¢ 3=workflow to curate & approve.

??? info "4) Lineage"
    **Ask:** How is lineage captured (technical & business)? Whatâ€™s the coverage, depth, and refresh cadence?  
    **Evidence:** tool outputs; % coverage; refresh schedule; impact analysis examples.  
    **Score:** 0=none â€¢ 1=partial/manual â€¢ 2=tool-based with coverage targets â€¢ 3=automated w/ CI/CD harvesting.

??? info "5) Data quality"
    **Ask:** Are DQ rules configurable and mapped to dimensions (accuracy, completeness, timeliness, consistency, validity, uniqueness)? How are thresholds, exceptions, and monitoring handled?  
    **Evidence:** rule repo; SLA thresholds; exception workflow; alerts/dashboards.  
    **Score:** 0=none â€¢ 1=ad hoc â€¢ 2=standardized dimensions & SLAs â€¢ 3=continuous monitoring + breach escalation.

??? info "6) Stewardship & ownership"
    **Ask:** Are data owners/stewards defined and assigned with clear RACI and capacity to act?  
    **Evidence:** steward registry; RACI by domain/product; time allocation.  
    **Score:** 0=unknown â€¢ 1=names only â€¢ 2=RACI formalized â€¢ 3=accountabilities measured (SLOs).

??? info "7) Governance operating model"
    **Ask:** Are councils/committees, roles/responsibilities, decision rights, and change processes established? How are policies approved and enforced?  
    **Evidence:** charters; decision logs; policy lifecycle; enforcement tooling.  
    **Score:** 0=none â€¢ 1=informal â€¢ 2=documented & running â€¢ 3=audited with KPIs.

??? info "8) AI readiness"
    **Ask:** What is the organizationâ€™s AI readiness/maturity (data availability, governance controls, risk/compliance guardrails, model oversight)?  
    **Evidence:** approved datasets for AI; PII handling; usage policies; model review gates; red-teaming.  
    **Score:** 0=unknown â€¢ 1=pilot-only guardrails â€¢ 2=enterprise controls â€¢ 3=governed lifecycle (dataâ†’model).

??? info "9) Compliance & risk"
    **Ask:** Which regulations and internal policies drive governance requirements? How are controls evidenced and audited?  
    **Evidence:** control library mapped to regs; evidence collection; audit cadence; exceptions register.  
    **Score:** 0=unmapped â€¢ 1=manual audits â€¢ 2=mapped with evidence â€¢ 3=continuous assurance & attestations.

??? info "10) Metrics & value"
    **Ask:** What KPIs are tracked (policy coverage, DQ scores, issue MTTR, adoption)? How is value realized and reported?  
    **Evidence:** KPI list; dashboards; executive reporting; value stories.  
    **Score:** 0=none â€¢ 1=lagging only â€¢ 2=standard KPI set â€¢ 3=targets with actions & ROI.

??? info "11) Access & security"
    **Ask:** How are classification-driven access controls, segregation of duties, and retention/disposition managed?  
    **Evidence:** RBAC/ABAC; masking/row-level security; SoD rules; retention schedules.  
    **Score:** 0=local rules â€¢ 1=policy but uneven â€¢ 2=centralized enforcement â€¢ 3=auto-provisioning + recert.

??? info "12) Enablement & adoption"
    **Ask:** How are stakeholders trained and supported (playbooks, office hours, communities of practice)? How is feedback incorporated?  
    **Evidence:** training plans; playbooks/templates; engagement metrics; feedback backlog â†’ policy updates.  
    **Score:** 0=none â€¢ 1=one-off sessions â€¢ 2=programmatic enablement â€¢ 3=measured adoption & improvement.

---

### Quick worksheet (copy/paste)

- [ ] 1. Metadata enrichment â€” Score: `0/1/2/3` â€” Notes:  
- [ ] 2. Source prioritization & CDEs â€” Score: `0/1/2/3` â€” Notes:  
- [ ] 3. Knowledge capture â€” Score: `0/1/2/3` â€” Notes:  
- [ ] 4. Lineage â€” Score: `0/1/2/3` â€” Notes:  
- [ ] 5. Data quality â€” Score: `0/1/2/3` â€” Notes:  
- [ ] 6. Stewardship & ownership â€” Score: `0/1/2/3` â€” Notes:  
- [ ] 7. Operating model â€” Score: `0/1/2/3` â€” Notes:  
- [ ] 8. AI readiness â€” Score: `0/1/2/3` â€” Notes:  
- [ ] 9. Compliance & risk â€” Score: `0/1/2/3` â€” Notes:  
- [ ] 10. Metrics & value â€” Score: `0/1/2/3` â€” Notes:  
- [ ] 11. Access & security â€” Score: `0/1/2/3` â€” Notes:  
- [ ] 12. Enablement & adoption â€” Score: `0/1/2/3` â€” Notes:  

!!! tip "Jump to accelerators"
    - **Architecture** â†’ ../architecture/index.md  
    - **Data Buddy** â†’ ../data-buddy/index.md  
    - **Synthetic Data Generator** â†’ ../synthetic-data-generator/index.md  
    - **MDM** â†’ ../mdm/index.md



