
## `docs/data-buddy/data-quality.md`
```markdown
# Data Quality

Define and monitor rules mapped to dimensions (accuracy, completeness, timeliness, consistency, validity, uniqueness).

## Tasks
- Rule definitions & thresholds
- SLA & breach alerts
- Exceptions workflow

## Example (placeholder)
```yaml
# dq/customers.yml
rules:
  - name: email_valid
    dimension: validity
    expr: "email ~ '^[^@]+@[^@]+\\.[^@]+$'"
    threshold: 0.99
