"""Negation, Modality & Scope - Tests handling of negation and uncertainty"""

TESTS = {
    "negation_01_simple": {
        "text": "Smoking does not improve health.",
        "extract": [("smoking", "does not improve", "health")],
        "reject": [("smoking", "improves", "health")],
    },
    "negation_02_double": {
        "text": "It is not uncommon for startups to fail.",
        "extract": [],
        "reject": [("startups", "uncommon", "fail")],
    },
    "negation_03_possibility": {
        "text": "Coffee may reduce the risk of diabetes.",
        "extract": [("coffee", "may reduce", "risk of diabetes")],
        "reject": [("coffee", "reduces", "risk of diabetes")],
    },
    "negation_04_hypothetical": {
        "text": "If the experiment had succeeded, we would have proven the hypothesis.",
        "extract": [],
        "reject": [("experiment", "succeeded", ""), ("hypothesis", "proven", "")],
    },
    "negation_05_nonexistence": {
        "text": "There is no evidence that vaccines cause autism.",
        "extract": [("evidence", "does not exist", "vaccines cause autism")],
        "reject": [("vaccines", "cause", "autism")],
    },
    "negation_06_conditional": {
        "text": "Unless properly stored, the medicine will not remain effective.",
        "extract": [],
        "reject": [("medicine", "remains", "effective")],
    },
}
