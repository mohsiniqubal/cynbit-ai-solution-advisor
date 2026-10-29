import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import streamlit as st
from app.advisor import recommend, create_brief

st.set_page_config(page_title="Cynbit AI Solution Advisor", page_icon="🧭", layout="wide")
st.title("Cynbit AI Solution Advisor")
st.caption("Assessment proof of concept • Explainable service discovery • Human-in-the-loop")

with st.sidebar:
    st.subheader("About this demo")
    st.write("A lightweight TF-IDF baseline that maps a business challenge to relevant service and product areas.")
    st.info("Similarity scores are not probabilities. Validate recommendations with a person.")
    st.markdown("[Cynbit website](https://www.cynbit.in/) · [Services](https://www.cynbit.in/services) · [Products](https://www.cynbit.in/products)")

st.markdown("### Describe the business challenge")
st.write("Use a non-confidential example. More context usually leads to more useful matches.")
with st.form("discovery_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Organization or contact (optional)", placeholder="Example Co.")
        sector = st.selectbox("Industry / context", [
            "Choose one", "Retail / e-commerce", "Education / training", "Property management",
            "Healthcare", "Professional services", "SaaS / technology", "Other"
        ])
        timeline = st.selectbox("Desired timeline", ["Not decided", "2–4 weeks", "1–3 months", "3+ months"])
    with col2:
        goals = st.text_area("Desired outcome", placeholder="Reduce manual work, improve response time, increase conversion…", height=100)
        constraints = st.text_area("Current tools / constraints", placeholder="CRM, spreadsheets, existing website, privacy, budget…", height=100)
    problem = st.text_area("What problem are you trying to solve? *",
        placeholder="Example: Our team manually reads customer reviews across several locations and struggles to spot urgent complaints.",
        height=150)
    submitted = st.form_submit_button("Find relevant solution areas", type="primary")

if submitted:
    if len(problem.strip()) < 12:
        st.warning("Please describe the challenge in a little more detail (at least 12 characters).")
    else:
        context_sector = "" if sector == "Choose one" else sector
        results = recommend(problem, context_sector, goals, constraints, top_k=3)
        st.session_state["advisor_inputs"] = {
            "name": name, "sector": context_sector, "problem": problem,
            "goals": goals, "constraints": constraints, "timeline": timeline
        }
        st.session_state["advisor_results"] = results

if "advisor_results" in st.session_state:
    inputs = st.session_state["advisor_inputs"]
    results = st.session_state["advisor_results"]
    st.divider()
    st.subheader("Recommended areas to explore")
    st.caption("Ranked by text similarity against a small, manually curated catalogue—not by business success probability.")
    for rank, rec in enumerate(results, 1):
        with st.container(border=True):
            left, right = st.columns([4, 1])
            with left:
                st.markdown(f"**{rank}. {rec['name']}**")
                st.caption(rec["category"])
                st.write(rec["fit"])
                st.write("**Shared terms:** " + (", ".join(rec["matched_terms"]) if rec["matched_terms"] else "No direct shared terms"))
                with st.expander("Discovery questions"):
                    for q in rec["discovery_questions"]:
                        st.write("• " + q)
            with right:
                st.metric("Similarity", f"{rec['score']:.3f}")
    brief = create_brief(inputs["name"], inputs["sector"], inputs["problem"], inputs["goals"],
                         inputs["constraints"], inputs["timeline"], results)
    st.download_button("Download discovery brief (.md)", brief, file_name="cynbit_discovery_brief.md",
                       mime="text/markdown", type="primary")
    with st.expander("Preview generated brief"):
        st.markdown(brief)
else:
    st.markdown("### Try an example")
    st.write("“We manage several rental properties and want to track units, tenants, rent dues, and reminders in one place.”")
    st.write("“Our multi-location brand needs to classify online reviews, flag urgent complaints, and draft responses for approval.”")
    st.write("“Our team copies details from incoming PDFs into spreadsheets and wants to reduce repetitive data entry.”")

st.divider()
st.caption("Prototype only. Do not enter sensitive or confidential information. Recommendations must be reviewed by Cynbit staff.")
