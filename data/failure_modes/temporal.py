"""Temporal Reasoning - Tests understanding of time and state changes"""

TESTS = {
    "temporal_01_former": {
        "text": "Steve Jobs was the former CEO of Apple.",
        "extract": [("steve jobs", "was former ceo of", "apple")],
        "reject": [("steve jobs", "is ceo of", "apple")],
    },
    "temporal_02_timebound": {
        "text": "As of 2022, Elon Musk owned Twitter.",
        "extract": [("elon musk", "owned", "twitter")],
        "reject": [("elon musk", "owns", "twitter")],
    },
    "temporal_03_sequence": {
        "text": "Before the merger, Company A operated independently. After 2019, it became a subsidiary of MegaCorp.",
        "extract": [
            ("company a", "operated independently", "before merger"),
            ("company a", "became subsidiary of", "megacorp"),
        ],
        "reject": [],
    },
    "temporal_04_future": {
        "text": "SpaceX plans to send humans to Mars by 2030.",
        "extract": [("spacex", "plans to send", "humans to mars")],
        "reject": [("spacex", "sent", "humans to mars")],
    },
    "temporal_05_historical": {
        "text": "Constantinople was the capital of the Byzantine Empire. Istanbul is now a major city in Turkey.",
        "extract": [
            ("constantinople", "was capital of", "byzantine empire"),
            ("istanbul", "is", "major city in turkey"),
        ],
        "reject": [("constantinople", "is capital of", "byzantine empire")],
    },
}
