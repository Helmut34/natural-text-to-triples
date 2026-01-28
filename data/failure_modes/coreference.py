"""Coreference & Entity Resolution - Tests pronoun/alias resolution"""

TESTS = {
    "coref_01_pronoun": {
        "text": "The Transformer architecture was introduced by Vaswani et al. in 2017. It revolutionized natural language processing. The model uses self-attention mechanisms.",
        "extract": [
            ("transformer", "introduced by", "vaswani et al"),
            ("transformer", "introduced in", "2017"),
            ("transformer", "revolutionized", "natural language processing"),
            ("transformer", "uses", "self-attention mechanisms"),
        ],
        "reject": [("it", "revolutionized", "nlp")],
    },
    "coref_02_alias": {
        "text": "Dr. Robert Smith published the study. Bob, as his colleagues call him, spent three years on the research. Smith's findings were groundbreaking.",
        "extract": [
            ("robert smith", "published", "study"),
            ("robert smith", "spent", "three years on research"),
            ("robert smith", "findings were", "groundbreaking"),
        ],
        "reject": [],
    },
    "coref_03_implicit": {
        "text": "Einstein developed the theory of relativity. The German-born physicist later moved to America. His work on photoelectric effect won the Nobel Prize.",
        "extract": [
            ("einstein", "developed", "theory of relativity"),
            ("einstein", "moved to", "america"),
            ("einstein", "won", "nobel prize"),
        ],
        "reject": [],
    },
    "coref_04_ambiguous": {
        "text": "John told Mike that he was promoted. He was very happy about it.",
        "extract": [],
        "reject": [("john", "was promoted", ""), ("mike", "was promoted", "")],
    },
}
