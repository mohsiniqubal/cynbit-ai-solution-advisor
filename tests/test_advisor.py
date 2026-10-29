from app.advisor import recommend, create_brief

def test_review_problem_ranks_revio():
    results = recommend("We need sentiment analysis for customer reviews and reputation monitoring across locations", top_k=3)
    assert results
    assert results[0]["id"] == "revio"

def test_rent_problem_ranks_tenantease():
    results = recommend("Track tenants, rent payments, property units, and overdue dues", top_k=3)
    assert results[0]["id"] == "tenantease"

def test_empty_problem_returns_no_results():
    assert recommend("   ") == []

def test_brief_has_human_review_warning():
    recs = recommend("automate document processing from PDFs")
    brief = create_brief("Demo Co", "Technology", "Automate PDFs", "Reduce manual entry", "Existing spreadsheet", "1–3 months", recs)
    assert "Human review checklist" in brief
    assert "not a probability" in brief
