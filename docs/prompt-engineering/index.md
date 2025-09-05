# Prompt Engineering

Design prompts and context pipelines that are **accurate, safe, and testable**—so conversational and generative features behave like products, not demos.

## What it covers
- **Structured prompts & templates** – roles, constraints, step-by-step formats.
- **Grounding & retrieval (RAG)** – cite sources, control drift, reduce hallucination.
- **Guardrails** – instruction hierarchy, input/output validation, red-team prompts.
- **Evaluation** – golden sets, rubric scoring, regression tests in CI.
- **Observability** – prompt/version tracking, cost/latency metrics, feedback loops.

## Quickstart (placeholders)
```bash
# Run an eval suite against a prompt template + golden set
python -m prompts eval \
  --template prompts/qa.jinja \
  --dataset evals/governance_qa.jsonl \
  --metrics exact_match,bleu,judge

# Batch-generate with retrieval and citations
python -m prompts generate \
  --template prompts/rag_cited.jinja \
  --kb ./knowledge \
  --questions data/questions.csv \
  --out out/answers.csv
