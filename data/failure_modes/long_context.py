"""Long-Range Context Consistency - Tests maintaining coherence across paragraphs"""

TESTS = {
    "context_01_contradictory_roles": {
        "text": """Alice is Bob's manager at TechCorp. She oversees his quarterly reviews.

Several months later, the company restructured. Bob now handles all personnel decisions for the engineering department, including performance evaluations for Alice.""",
        "extract": [
            ("alice", "was manager of", "bob"),
            ("bob", "handles personnel decisions for", "alice"),
        ],
        "reject": [("alice", "is manager of", "bob")],
    },
    "context_02_changing_state": {
        "text": """The startup was founded in 2018 with $50,000 in seed funding. By 2020, they had raised Series A funding of $2 million. In 2023, after the acquisition by MegaCorp, the company no longer exists as an independent entity.""",
        "extract": [
            ("startup", "founded in", "2018"),
            ("startup", "raised series a", "2020"),
            ("startup", "acquired by", "megacorp"),
        ],
        "reject": [("startup", "exists as", "independent entity")],
    },
    "context_03_definition_contradiction": {
        "text": """For this document, "active user" means someone who logged in within 30 days. We have 10,000 active users.

Note: Above metrics use a 7-day window for "active user" calculations.""",
        "extract": [],
        "reject": [],
    },
}
