# Technical Approach Report: Cynbit AI Solution Advisor
**Candidate:** Mohsin Iqubal  
**Assessment role:** AI/ML Engineer Intern  
**Prototype status:** Runnable local Streamlit application

## 1. Objective
Convert a prospective customer's free-text business challenge into a ranked shortlist of relevant Cynbit service/product areas and a discovery brief for human review. The system is designed for intake assistance, not autonomous sales decisions.

## 2. Architecture
```text
User inputs
  ├─ business challenge
  ├─ sector / desired outcome
  └─ constraints / timeline
          |
          v
Input validation and query assembly
          |
          v
Curated service/product catalogue
          |
          v
TF-IDF vectorization (unigrams + bigrams)
          |
          v
Cosine similarity ranking
          |
          v
Top recommendations + shared terms + discovery questions
          |
          v
Markdown discovery brief (download)
          |
          v
Human review before any external action
```

## 3. Model choice
### Baseline: TF-IDF + cosine similarity
TF-IDF is a lightweight information-retrieval baseline that emphasizes terms that distinguish catalogue entries. Bigrams can capture phrases such as “rent payments” or “review management.” Cosine similarity ranks entries based on vector direction.

**Why this model:** no labelled training data was provided; it is inexpensive, fast, deterministic for a fixed catalogue, easy to inspect, and runs without external API credentials. A supervised classifier would be premature without reviewed examples and stable category labels.

**Important interpretation:** the score is lexical similarity, not confidence, probability of success, or an estimate of ROI. Similar wording can outrank semantically relevant wording that uses different vocabulary.

## 4. Data pipeline
1. **Catalogue source:** manually curated summaries of public Cynbit service/product pages.
2. **Input:** user-provided business problem plus optional sector, goal, and constraints.
3. **Validation:** the UI asks for a minimally descriptive challenge and does not require personal contact data.
4. **Normalization:** text is joined and tokenized by scikit-learn's TF-IDF vectorizer; English stop words are removed.
5. **Ranking:** cosine similarity between query and catalogue vectors.
6. **Output:** top three catalogue entries, similarity scores, shared terms, discovery questions, and a downloadable Markdown brief.

The demo has no persistent database and sends no input to a remote model. Inputs exist in the active app session and generated download only. Do not enter confidential information.

## 5. Prompt engineering / LLM strategy
The current implementation intentionally does not call an LLM. This avoids making claims about prompt quality or requiring an API key, while preserving a functional PoC.

A future LLM-assisted version should use retrieval-augmented generation over approved service documentation:
- System instruction: recommend only from retrieved, approved service entries; explicitly say when evidence is insufficient.
- Input separation: place user content in a clearly delimited untrusted section.
- Output schema: `recommendations[]`, `evidence[]`, `questions[]`, `assumptions[]`, and `needs_human_review`.
- Evidence: each recommendation should cite the internal catalogue entry ID and a short supporting passage.
- Safety: no external tools or CRM writes by default; human approval for outbound messages.
- Evaluation: test for unsupported claims, prompt injection, omissions, and inconsistent category selection.
- Privacy: minimize input, redact sensitive content, define retention, and obtain approval before using third-party APIs.

## 6. API and deployment plan
The current deliverable is a Streamlit app. For a production service:
- Wrap recommendation logic in a FastAPI endpoint such as `POST /recommend`.
- Validate payloads with Pydantic and cap text lengths.
- Add structured logging without recording raw sensitive content.
- Package with Docker and deploy behind authentication and HTTPS.
- Add rate limiting, monitoring, versioned catalogue, and health checks.
- Store approved analytics only, with retention and access policies.
- Integrate CRM only after access control, audit logging, and approval workflows are agreed.

## 7. Evaluation plan
No labelled dataset was available, so no model accuracy is reported.

Create a consented, anonymized dataset with inquiry text and expert-assigned service categories. Use a held-out set and compare:
- Keyword baseline.
- TF-IDF cosine similarity.
- Sentence embedding retrieval.
- Optional RAG/LLM reranking.

Metrics:
- Top-1 accuracy.
- Precision@3 / Recall@3.
- Coverage: percentage of queries with at least one useful recommendation.
- Per-category precision and error review.
- Reviewer acceptance rate and time-to-triage during shadow mode.
- Hallucination / unsupported-claim rate if an LLM is introduced.

Define acceptance criteria with business owners before testing; do not choose thresholds after seeing results.

## 8. Failure modes and mitigations

| Failure mode | Mitigation |
|---|---|
| Vocabulary mismatch / synonyms | Expand catalogue; test embeddings on labelled examples |
| Generic input produces weak matches | Ask clarifying questions; show limitations |
| Similarity interpreted as confidence | Label it consistently as text similarity |
| Catalogue becomes stale | Version it and assign a content owner |
| Incorrect or risky recommendation | Human review and easy rejection |
| Prompt injection in future RAG version | Treat user/retrieved text as untrusted; restrict tools |
| Sensitive data in inquiry | Minimize collection, warn users, redact and define retention |
| Bias toward longer descriptions | Normalize and review catalogue content; evaluate per category |

## 9. Execution plan
- Week 1: stakeholder review, catalogue approval, data and privacy review.
- Week 2: label initial sample and run offline evaluation.
- Weeks 3–4: shadow mode and reviewer feedback.
- After evidence: pilot with agreed success criteria, monitoring, and rollback plan.

## 10. Files in this prototype
- `app/catalogue.py`: curated service/product entries.
- `app/advisor.py`: recommendation and brief logic.
- `app/streamlit_app.py`: UI.
- `tests/test_advisor.py`: basic unit tests.
- `README.md`: setup, testing, limitations, and references.

## References
- https://www.cynbit.in/services
- https://www.cynbit.in/products
- https://www.cynbit.in/contact
- https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting
- https://scikit-learn.org/stable/modules/metrics.html#cosine-similarity
