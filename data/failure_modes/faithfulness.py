"""Faithfulness to Source - Tests strict extraction vs hallucination"""

TESTS = {
    "faithful_01_resist_knowledge": {
        "text": "Marie Curie conducted research on radioactivity.",
        "extract": [("marie curie", "conducted research on", "radioactivity")],
        "reject": [("marie curie", "won", "nobel prize")],
    },
    "faithful_02_resist_completion": {
        "text": "The company was founded in Silicon Valley.",
        "extract": [("company", "founded in", "silicon valley")],
        "reject": [("company", "founded in", "california")],
    },
    "faithful_03_hedged": {
        "text": "Studies suggest a correlation between sleep and productivity.",
        "extract": [("studies", "suggest correlation", "sleep and productivity")],
        "reject": [("sleep", "causes", "productivity")],
    },
    "faithful_04_attributed": {
        "text": "Some researchers believe that meditation reduces stress.",
        "extract": [("some researchers", "believe", "meditation reduces stress")],
        "reject": [("meditation", "reduces", "stress")],
    },
    "faithful_05_quoted": {
        "text": "John claimed that the project was a success.",
        "extract": [("john", "claimed", "project was success")],
        "reject": [("project", "was", "success")],
    },
}
