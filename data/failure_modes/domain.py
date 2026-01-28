"""Domain-Specific Language - Tests handling of specialized terminology"""

TESTS = {
    "domain_01_legal": {
        "text": "The plaintiff hereby moves for summary judgment pursuant to Rule 56, arguing that no genuine dispute of material fact exists.",
        "extract": [("plaintiff", "moves for", "summary judgment")],
        "reject": [],
    },
    "domain_02_medical": {
        "text": "Pt presents w/ SOB, tachycardia. Hx of CHF. BP 140/90, HR 110. Rx: Lasix 40mg PO BID.",
        "extract": [
            ("patient", "presents with", "shortness of breath"),
            ("patient", "presents with", "tachycardia"),
            ("patient", "history of", "congestive heart failure"),
        ],
        "reject": [],
    },
    "domain_03_math": {
        "text": "Let f(x) = x² + 2x + 1. The derivative f'(x) = 2x + 2.",
        "extract": [("f(x)", "equals", "x² + 2x + 1"), ("f'(x)", "equals", "2x + 2")],
        "reject": [],
    },
    "domain_04_programming": {
        "text": "The function implements a recursive binary search with O(log n) time complexity.",
        "extract": [
            ("function", "implements", "recursive binary search"),
            ("function", "has", "o(log n) time complexity"),
        ],
        "reject": [],
    },
}
