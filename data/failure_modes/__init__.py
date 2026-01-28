"""Failure Mode Test Data"""

from .pattern_matching import TESTS as PATTERN_MATCHING
from .long_context import TESTS as LONG_CONTEXT
from .coreference import TESTS as COREFERENCE
from .implicit import TESTS as IMPLICIT
from .negation import TESTS as NEGATION
from .temporal import TESTS as TEMPORAL
from .commonsense import TESTS as COMMONSENSE
from .domain import TESTS as DOMAIN
from .faithfulness import TESTS as FAITHFULNESS

CATEGORIES = {
    "pattern_matching": ("Pattern Matching vs Understanding", PATTERN_MATCHING),
    "long_context": ("Long-Range Context Consistency", LONG_CONTEXT),
    "coreference": ("Coreference & Entity Resolution", COREFERENCE),
    "implicit": ("Implicit / Unstated Information", IMPLICIT),
    "negation": ("Negation, Modality & Scope", NEGATION),
    "temporal": ("Temporal Reasoning", TEMPORAL),
    "commonsense": ("Commonsense & World Knowledge", COMMONSENSE),
    "domain": ("Domain-Specific Language", DOMAIN),
    "faithfulness": ("Faithfulness to Source", FAITHFULNESS),
}

# Combined tests dict
ALL_TESTS = {}
for cat_key, (_, tests) in CATEGORIES.items():
    for test_id, test_data in tests.items():
        ALL_TESTS[test_id] = {**test_data, "category": cat_key}
