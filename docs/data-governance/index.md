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

- :material-sitemap: **Data Architecture**  
  The technical blueprint—zones, models, integrations (batch/stream/event), APIs, and IAM—that
  implements governance principles and enables reusable, scalable delivery.

- :material-source-branch: **Data Lineage**  
  End-to-end traceability of data from source to consumption (technical + business lineage) for
  impact analysis, troubleshooting, and auditability.

</div>

---



## Capability matrix

<!-- Scoped styling just for this table -->
<style>
/* Capability Matrix – Pellera banner look + compact, readable layout */

/* Match the banner/header gradient (deep indigo → Pellera purple → electric purple) */
:root {
  --cap-header-gradient: linear-gradient(
    90deg,
    rgba(12,10,43,.92) 0%,
    rgba(78,49,191,.85) 58%,
    rgba(123,44,255,.65) 100%
  );
}

.cap-table {                     /* shrink overall font a bit */
  font-size: .92rem;
}

@media (max-width: 900px) {      /* a touch smaller on narrow screens */
  .cap-table { font-size: .88rem; }
}

.cap-table table {
  width: 100%;
  table-layout: fixed;           /* prevents overflow; respects widths below */
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 6px 18px rgba(0,0,0,.06);
}

.cap-table thead th {
  background: var(--cap-header-gradient);  /* banner-matching header */
  color: #fff;
  font-weight: 600;
}

.cap-table td,
.cap-table th {
  vertical-align: top;
  padding: .60rem .75rem;        /* slightly tighter to fit more content */
}

/* Balanced column widths (will be honored because of table-layout: fixed) */
.cap-table thead th:nth-child(1) { width: 22%; }  /* Capability / Offerings   */
.cap-table thead th:nth-child(2) { width: 36%; }  /* What It Means            */
.cap-table thead th:nth-child(3) { width: 20%; }  /* Who’s Involved           */
.cap-table thead th:nth-child(4) { width: 22%; }  /* Why It Matters           */

.cap-table td {                  /* wrap long words/URLs to avoid scrolling */
  word-break: break-word;
}

.cap-table tbody tr:nth-child(odd) td {
  background: rgba(112,84,255,.03);
}
</style>

<div class="cap-table" markdown>

| Capability / Offerings | What It Means | Who’s Involved | Why It Matters |
|---|---|---|---|
| **Metadata Management** | Create, update, and maintain metadata (data about data); build & operate the data catalog, including policies and lineage links. | Data Steward / Catalog Manager | Enables users to find & understand data; drives self-service analytics. |
| **Data Profiling** | Sample analysis to surface structure, patterns, outliers; full-dataset assessment across dimensions (completeness, accuracy, uniqueness, validity, timeliness); custom rule definition. | Data Analyst / Steward | Quick health check; guides deeper quality efforts. |
| **Data Quality** | Dimensions, rules, thresholds/SLAs; continuous monitoring, exceptions, and scorecards. | Data Quality Lead / Engineer | Ensures analytics & ML models use reliable data; reduces risk of bad decisions. |
| **Data Compliance** | Policies & controls by geography/domain (e.g., GDPR, CCPA, GLBA). Evidence collection and attestation workflows. | Legal & Compliance Team | Avoids fines & lawsuits; supports rights to know/share/port/delete. |
| **Data Retention** | Lifecycle policies for archiving/disposing data; defensible deletion; “right-to-erase” requests. | Records Manager / IT | Meets legal mandates; simplifies audits and e-discovery. |
| **Master Data Management (MDM)** | Centralize & reconcile critical entity data (customers, products, suppliers). Golden record creation and survivorship rules. | MDM Lead / Architect | Single source of truth; improves cross-system consistency. |
| **Data Architecture** | Technical blueprint: domain boundaries, data zones, canonical models, integration patterns (batch/stream/event), APIs, storage, compute, and IAM guardrails that implement governance. | Data / Platform Architect, Data Engineering Lead | Provides reusable patterns and platform guardrails for **scalable, secure, cost-effective** delivery; turns policy into practice. |
| **Data Lineage** | End-to-end traceability of data (system, table, column). Technical + business lineage, change-impact analysis, and code-level drill-downs. | Data Engineer, Steward, Audit / Compliance | Builds trust and speeds issue resolution; supports audits and safe change management. |
<!-- Inject a direct download link into the right-hand Table of contents -->
<script>
  // Runs after each page render (incl. SPA navigations) in MkDocs Material
  function addDownloadToToc() {
    const tocList = document.querySelector('.md-nav--secondary .md-nav__list');
    if (!tocList || document.getElementById('toc-download-link')) return;

    const li = document.createElement('li');
    li.className = 'md-nav__item';

    const a = document.createElement('a');
    a.id = 'toc-download-link';
    a.className = 'md-nav__link';
    a.href = '../_assets/data-governance-deck.pptx';  // file lives in docs/_assets
    a.setAttribute('download', '');
    a.textContent = 'Download PPT deck';

    li.appendChild(a);
    tocList.appendChild(li); // appends beneath your last ToC item (desired spot)
  }

  // MkDocs Material SPA hook
  (window.document$ || { subscribe: fn => document.addEventListener('DOMContentLoaded', fn) })
    .subscribe(addDownloadToToc);
</script>

<style>
  /* Optional: make it stand out slightly in the ToC */
  #toc-download-link { font-weight: 600; }
  #toc-download-link::before { content: "⬇️ "; }
</style>

</div>

> Looking to evaluate maturity? See **[Assessment Questions](assessment.md)**.



[⬇️ Download the PowerPoint deck](../_assets/data-governance-deck.pptx){ .md-button .md-button--primary download }