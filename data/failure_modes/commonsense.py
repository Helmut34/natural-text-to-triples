"""Commonsense & World Knowledge - Tests common sense reasoning"""

TESTS = {
    "commonsense_01_physical": {
        "text": "John put the elephant in his pocket.",
        "extract": [],
        "reject": [("john", "put", "elephant in pocket")],
    },
    "commonsense_02_social": {
        "text": "The job candidate insulted the interviewer and got hired immediately.",
        "extract": [],
        "reject": [],
    },
    "commonsense_03_causal_nonsense": {
        "text": "The ice cream melted because it was placed in the freezer.",
        "extract": [],
        "reject": [("freezer", "caused", "ice cream melted")],
    },
    "commonsense_04_scale": {
        "text": "The ant carried the car to the garage.",
        "extract": [],
        "reject": [("ant", "carried", "car")],
    },
    "commonsense_05_valid_control": {
        "text": "The glass shattered when it hit the concrete floor.",
        "extract": [("glass", "shattered", ""), ("glass", "hit", "concrete floor")],
        "reject": [],
    },
    "commonsense_06_context_dependent": {
        "text": "The bank was full of fish.",
        "extract": [("bank", "full of", "fish")],
        "reject": [],
    },
}
