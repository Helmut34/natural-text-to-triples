"""
Failure Mode Test Runner
Evaluates triple extraction models across 9 failure categories.

Usage:
    python test/failure_mode_runner.py              # Run all tests
    python test/failure_mode_runner.py negation     # Run single category
"""

import sys
sys.path.insert(0, '/home/helmut/natural-text-to-triples')

from data.failure_modes import CATEGORIES, ALL_TESTS
from model.txt2triples import text_to_triples


def normalize(t):
    """Normalize triple for comparison."""
    return tuple(str(x).strip().lower() for x in t)


def parse_output(output):
    """Parse model output to set of triples."""
    triples = set()
    if not output:
        return triples

    # Handle list output from batch_decode
    if isinstance(output, list):
        output_str = output[0] if output else ""
    else:
        output_str = output

    if not output_str or not output_str.strip():
        return triples

    output_str = output_str.strip()
    if output_str.startswith('('):
        output_str = output_str[1:]
    if output_str.endswith(')'):
        output_str = output_str[:-1]

    for t in output_str.split('), ('):
        t = t.strip('()')
        parts = [p.strip().lower() for p in t.split(';')]
        if len(parts) == 3:
            triples.add(tuple(parts))

    return triples


def evaluate_test(test_id, test_data):
    """Evaluate single test case."""
    output = text_to_triples(test_data["text"])
    predicted = parse_output(output)

    expected = set(normalize(t) for t in test_data.get("extract", []))
    rejected = set(normalize(t) for t in test_data.get("reject", []))
    inferred = set(normalize(t) for t in test_data.get("inferred_ok", []))

    correct = predicted & expected
    missed = expected - predicted
    hallucinations = predicted & rejected
    bonus = predicted & inferred

    return {
        "test_id": test_id,
        "category": test_data.get("category", "unknown"),
        "predicted": predicted,
        "correct": correct,
        "missed": missed,
        "hallucinations": hallucinations,
        "bonus_inferences": bonus,
        "passed": len(hallucinations) == 0 and missed == set(),
    }


def run_all():
    """Run all tests and print results."""
    print("=" * 60)
    print("FAILURE MODE TEST SUITE")
    print("=" * 60)

    results_by_category = {}

    for test_id, test_data in ALL_TESTS.items():
        result = evaluate_test(test_id, test_data)
        cat = result["category"]
        if cat not in results_by_category:
            results_by_category[cat] = []
        results_by_category[cat].append(result)

    total_passed = 0
    total_tests = 0

    for cat_key, (cat_name, _) in CATEGORIES.items():
        if cat_key not in results_by_category:
            continue

        results = results_by_category[cat_key]
        passed = sum(1 for r in results if r["passed"])
        total = len(results)
        total_passed += passed
        total_tests += total

        print(f"\n{'='*60}")
        print(f"{cat_name}")
        print(f"{'='*60}")

        for r in results:
            status = "PASS" if r["passed"] else "FAIL"
            print(f"\n[{status}] {r['test_id']}")
            if r["correct"]:
                print(f"  + Correct: {len(r['correct'])}")
            if r["missed"]:
                print(f"  - Missed: {r['missed']}")
            if r["hallucinations"]:
                print(f"  ! HALLUCINATION: {r['hallucinations']}")
            if r["bonus_inferences"]:
                print(f"  * Bonus inference: {r['bonus_inferences']}")

        print(f"\nCategory: {passed}/{total} ({100*passed/total:.0f}%)")

    print(f"\n{'='*60}")
    print(f"TOTAL: {total_passed}/{total_tests} ({100*total_passed/total_tests:.0f}%)")
    print("=" * 60)


def run_category(category):
    """Run tests for a single category."""
    if category not in CATEGORIES:
        print(f"Unknown category: {category}")
        print(f"Available: {list(CATEGORIES.keys())}")
        return

    cat_name, tests = CATEGORIES[category]
    print(f"Testing: {cat_name}")
    print("-" * 40)

    for test_id, test_data in tests.items():
        test_with_cat = {**test_data, "category": category}
        result = evaluate_test(test_id, test_with_cat)
        status = "PASS" if result["passed"] else "FAIL"
        print(f"[{status}] {test_id}")
        if result["hallucinations"]:
            print(f"   HALLUCINATION: {result['hallucinations']}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_category(sys.argv[1])
    else:
        run_all()
