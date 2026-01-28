"""Implicit / Unstated Information - Tests inference capabilities"""

TESTS = {
    "implicit_01_causal": {
        "text": "John resigned after the scandal broke.",
        "extract": [("john", "resigned", "")],
        "reject": [],
        "inferred_ok": [("scandal", "caused", "resignation")],
    },
    "implicit_02_temporal": {
        "text": "Sarah finished her PhD before joining Google.",
        "extract": [("sarah", "finished", "phd"), ("sarah", "joined", "google")],
        "reject": [],
        "inferred_ok": [("sarah finishing phd", "before", "joining google")],
    },
    "implicit_03_possession": {
        "text": "The doctor reached for her stethoscope.",
        "extract": [("doctor", "reached for", "stethoscope")],
        "reject": [],
        "inferred_ok": [("doctor", "owns", "stethoscope")],
    },
    "implicit_04_consequence": {
        "text": "The company missed three consecutive earnings targets. The CEO was replaced the following month.",
        "extract": [
            ("company", "missed", "earnings targets"),
            ("ceo", "was replaced", ""),
        ],
        "reject": [],
        "inferred_ok": [("missed earnings", "caused", "ceo replacement")],
    },
}
