# Custom LLM

Build, deploy, and govern **domain-specific LLMs** that are reliable, safe, and cost-effective.
This accelerator packages **RAG**, **parameter-efficient fine-tuning (LoRA/QLoRA)**, **evaluation**, and **guardrails** into reproducible patterns that align with your Data Governance program.

<div class="grid cards" markdown>

- :material-puzzle-check: **What you get**
  - RAG blueprints (chunking, embeddings, vector search, prompt templates)
  - LoRA/QLoRA training recipes + experiment tracking
  - Test sets & evaluation harness (accuracy, faithfulness, toxicity, PII)
  - Safety guardrails (input filtering, prompt-injection defense, output redaction)
  - Serving patterns (OpenAI-compatible, vLLM/TGI, autoscale)
  - Cost/latency playbook & caching

- :material-account-cog: **Roles**
  - AI/ML Engineer, Data Engineer  
  - Data Steward / Compliance  
  - Product Owner / SME

</div>

---

## Reference patterns

### 1) **RAG-only (baseline)**
Use when knowledge changes frequently or compliance requires using curated sources.
- Ingest → normalize → chunk → embed → vector store
- Retrieval (hybrid lexical + vector optional), prompt template, answer synthesis
- Pros: Lower training cost, easier governance.  
- Cons: May need careful prompt design for style/format.

### 2) **RAG + LoRA**
Use when the model must adopt **tone, structure, or domain terminology** more naturally.
- Lightweight LoRA adapters trained on high-quality, governed examples
- Keep RAG for freshness + citations
- Pros: Big quality lift for small cost; adapters are small and easily governed.  
- Cons: Requires curation of small but clean fine-tuning sets.

### 3) **Domain fine-tune (full)**
Use when strict latency, specialty reasoning, or offline deployment is required.
- Full finetune or continued pretraining in a secure environment
- Pros: Highest control/perf; Cons: more cost and governance surface area.

---

## Build it

### A) Data preparation & governance
- Pull **approved, cataloged** sources; attach **lineage** and **privacy class**.
- Strip/obfuscate PII where policy requires; keep a **data card** with provenance and license.
- Create two sets:
  - **Knowledge set** for RAG (chunked + embedded)
  - **Supervision set** for LoRA (instruction–response or Q&A), reviewed by SMEs

### B) RAG quick start (Python)

```python
# RAG skeleton with sentence-transformers + FAISS (local, vendor-neutral)
from sentence_transformers import SentenceTransformer
from datasets import Dataset
import faiss, numpy as np

embed = SentenceTransformer("all-MiniLM-L6-v2")
docs  = [{"id": i, "text": t} for i, t in enumerate(load_your_texts())]
ds    = Dataset.from_list(docs)

embs = embed.encode([d["text"] for d in docs], normalize_embeddings=True)
index = faiss.IndexFlatIP(embs.shape[1]); index.add(np.array(embs, dtype="float32"))

def retrieve(query, k=5):
    q = embed.encode([query], normalize_embeddings=True).astype("float32")
    scores, idxs = index.search(q, k)
    return [docs[i]["text"] for i in idxs[0]]

def answer(query, llm):
    context = "\n\n".join(retrieve(query))
    prompt  = f"Use only the CONTEXT to answer.\nCONTEXT:\n{context}\n\nQ: {query}\nA:"
    return llm.generate(prompt)  # swap in your client (OpenAI, vLLM, TGI, etc.)
