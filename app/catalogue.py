"""Curated demo catalogue based on publicly described Cynbit service/product areas."""
CATALOGUE = [
    {
        "id": "ai_agents",
        "name": "AI Agents & Workflow Automation",
        "category": "AI automation",
        "description": (
            "Build AI agents and assistants for lead handling, coordination, repetitive "
            "knowledge work, document processing, and LLM-powered workflow automation."
        ),
        "fit": "Best when a team spends time on repetitive text-heavy tasks or needs a guided assistant.",
        "discovery_questions": [
            "Which steps are repetitive today, and how often do they occur?",
            "Which systems must the workflow connect to?",
            "What decisions must remain with a human?"
        ],
    },
    {
        "id": "document_ai",
        "name": "Document Extraction & Processing",
        "category": "AI automation",
        "description": (
            "Extract, classify, summarize, and route information from forms, PDFs, "
            "emails, and business documents with validation and human review."
        ),
        "fit": "Best when teams re-key information from documents or manually route requests.",
        "discovery_questions": [
            "What document types and approximate monthly volume are involved?",
            "Which fields need extraction and what accuracy is acceptable?",
            "What happens when the system is uncertain?"
        ],
    },
    {
        "id": "custom_software",
        "name": "Custom Web / Mobile & Backend Systems",
        "category": "Custom software",
        "description": (
            "Design and build web or mobile applications, APIs, backend systems, "
            "integrations, and scalable digital platforms."
        ),
        "fit": "Best when the main need is a new workflow, customer portal, or integration.",
        "discovery_questions": [
            "Who are the primary user groups?",
            "Which core workflows and integrations are in scope?",
            "What security, availability, and deployment constraints apply?"
        ],
    },
    {
        "id": "cloud_modernization",
        "name": "Cloud Infrastructure & Legacy Modernization",
        "category": "Cloud and infrastructure",
        "description": (
            "Cloud deployment on AWS or Azure, infrastructure automation, secure "
            "environments, and migration from legacy or monolithic applications."
        ),
        "fit": "Best when reliability, deployment, scalability, or legacy maintenance is the concern.",
        "discovery_questions": [
            "What is the current hosting and deployment setup?",
            "What availability, recovery, or compliance requirements apply?",
            "Are there dependencies or downtime windows that constrain migration?"
        ],
    },
    {
        "id": "crm_automation",
        "name": "CRM & Lead Nurturing Automation",
        "category": "Marketing automation",
        "description": (
            "Automate lead capture, qualification, follow-up workflows, CRM updates, "
            "and campaign handoffs with clear ownership and measurable funnel stages."
        ),
        "fit": "Best when inquiries are missed, follow-up is inconsistent, or CRM data is fragmented.",
        "discovery_questions": [
            "Which CRM and lead sources are currently used?",
            "What response-time target and qualification criteria matter?",
            "Which messages require human approval?"
        ],
    },
    {
        "id": "seo_funnel",
        "name": "Technical SEO & Funnel Optimization",
        "category": "Digital growth",
        "description": (
            "Improve technical SEO, landing-page conversion, performance marketing "
            "measurement, and funnel visibility using data-driven experiments."
        ),
        "fit": "Best when traffic, discovery, or conversion from web visits is the bottleneck.",
        "discovery_questions": [
            "What are the current traffic and conversion baselines?",
            "Which analytics and attribution tools are installed?",
            "What conversion event should an experiment optimize?"
        ],
    },
    {
        "id": "cynbit_studio",
        "name": "Cynbit Studio — Learning & Career Intelligence",
        "category": "Product: education and careers",
        "description": (
            "Adaptive coding paths, AI code evaluation, coding missions, mock interviews, "
            "resume tools, job matching, and career preparation for learners and institutions."
        ),
        "fit": "Best for education, training, coding practice, employability, or institutional career tools.",
        "discovery_questions": [
            "Is the primary user an individual learner or an institution?",
            "Which skill or employability outcome should improve?",
            "What evidence should be used to evaluate learner progress?"
        ],
    },
    {
        "id": "tenantease",
        "name": "TenantEase — Property & Tenant Operations",
        "category": "Product: property management",
        "description": (
            "Centralize property units, tenant profiles, rent/payment tracking, reminders, "
            "occupancy visibility, and property-management workflows."
        ),
        "fit": "Best for landlords or property teams managing units, tenants, dues, or occupancy.",
        "discovery_questions": [
            "How many properties, units, and tenants are managed?",
            "How are rent payments and arrears tracked today?",
            "Which users need access and what data must be protected?"
        ],
    },
    {
        "id": "revio",
        "name": "Revio — Review & Reputation Intelligence",
        "category": "Product: reputation management",
        "description": (
            "Monitor customer reviews, classify sentiment, detect reputation risks, "
            "draft responses, and compare feedback across locations or channels."
        ),
        "fit": "Best for brands with many reviews, locations, or time-consuming customer feedback handling.",
        "discovery_questions": [
            "Which review channels and locations matter most?",
            "What response approval policy should be followed?",
            "How should urgent complaints or safety concerns be escalated?"
        ],
    },
]
