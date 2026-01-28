"""Pattern Matching vs Understanding - Tests semantic validity"""

TESTS = {
    "pattern_01_nonsensical": {
        "text": "Paris is larger than France.",
        "extract": [],
        "reject": [("paris", "larger than", "france")],
    },
    "pattern_02_reversed_causality": {
        "text": "The fire was caused by the water.",
        "extract": [],
        "reject": [("water", "caused", "fire"), ("fire", "caused by", "water")],
    },
    "pattern_03_impossible_physical": {
        "text": "The shadow lifted the boulder.",
        "extract": [],
        "reject": [("shadow", "lifted", "boulder")],
    },
    "pattern_04_category_error": {
        "text": "The number seven tastes blue.",
        "extract": [],
        "reject": [("number seven", "tastes", "blue")],
    },
    "pattern_05_valid_control": {
        "text": "Mount Everest is taller than Mount Fuji.",
        "extract": [("mount everest", "taller than", "mount fuji")],
        "reject": [],
    },
}
