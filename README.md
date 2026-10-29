# Cynbit AI Solution Advisor
**AI/ML Engineer Intern assessment — Cynbit Technologies**

A small, runnable proof of concept that helps a prospective customer translate a business problem into relevant Cynbit service/product areas and a structured discovery brief.

## Why this opportunity?
Cynbit publicly describes AI agents and LLM automation, custom software/cloud services, CRM automation, technical SEO, and products including Cynbit Studio, TenantEase, and Revio. The website's inquiry flow asks customers to explain what they are building so the team can prepare a tailored overview. A guided, explainable advisor could make that first step more structured: better requirement capture, faster routing, and more consistent discovery notes.

This prototype is a **decision-support demo**, not a production lead-scoring model. It does not claim to predict conversion or use private customer data.

## Features
- Streamlit UI for a business challenge, sector, goals, constraints, and timeline.
- TF-IDF + cosine similarity ranks a curated service/product knowledge catalogue.
- Shows matched terms and short explanations so recommendations are inspectable.
- Produces a downloadable discovery brief in Markdown.
- No paid API key, external LLM, or customer dataset required.
- Tests for ranking and brief generation.

## Quick start
Python 3.10+ recommended.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

Open the local URL Streamlit prints.

## Run tests
```bash
pytest -q
```

## Repository layout
```text
app/
  advisor.py          TF-IDF matching and brief generation
  streamlit_app.py    user-facing demo
  catalogue.py        curated public-facing service/product descriptions
reports/
  01_ai_opportunity_report.md
  02_technical_approach.md
tests/
  test_advisor.py
requirements.txt
```

## How it works
1. A small curated catalogue is built from public Cynbit website descriptions.
2. User input is combined into a query string.
3. `TfidfVectorizer` encodes the query and catalogue descriptions.
4. Cosine similarity ranks catalogue entries.
5. The top recommendations and scores are shown with matched vocabulary for human review.

The score is a **text similarity score, not a probability, quality guarantee, or predicted business outcome**. Catalogue content is intentionally compact and should be reviewed by Cynbit before real use.

## Evaluation checklist
- Try different problem descriptions and compare the top recommendations.
- Verify that explanations and matches are sensible, not just the numeric score.
- Try empty/very short inputs and broad requests.
- Confirm that the brief contains the entered constraints and clear follow-up questions.
- Review any generated recommendations with a human before sending them to a prospect.

## Limitations and responsible use
- The catalogue is manually curated from public website content; it is not an official internal service taxonomy.
- No customer history, CRM records, conversion labels, or private information were available, so supervised learning and ROI claims would be unjustified.
- TF-IDF is a lightweight baseline. It may miss synonyms and intent; embeddings or a domain-tuned model could be evaluated later against a human-labelled test set.
- Do not enter confidential, personal, health, financial, or sensitive customer data.
- A production system should include consent and retention controls, access logging, prompt-injection protections if retrieval/LLMs are added, and a human review step.

## Suggested next steps
1. Ask sales/engineering to validate catalogue descriptions and routing rules.
2. Collect a consented set of anonymized historical inquiries with final service category labels.
3. Have two reviewers label a holdout set; measure Precision@3, top-1 accuracy, and reviewer agreement.
4. Compare TF-IDF against sentence embeddings and a retrieval-augmented LLM; evaluate cost, latency, hallucinations, and privacy.
5. Integrate with CRM only after security review and approval; keep human approval before external communication.

## Public references
- Cynbit homepage: https://www.cynbit.in/
- Services: https://www.cynbit.in/services
- Products: https://www.cynbit.in/products
- Case studies: https://www.cynbit.in/case-studies
- Contact / inquiry flow: https://www.cynbit.in/contact
- AI/ML Engineer Intern role: https://www.cynbit.in/careers/ai-ml-engineer-intern

Prepared as an assessment prototype. Public website descriptions are summarized for demonstration; no affiliation or endorsement is implied.
