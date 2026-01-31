import sys
from datetime import datetime

sys.path.insert(0, '/home/helmut/natural-text-to-triples')

from data.failure_modes import CATEGORIES, ALL_TESTS
from model.txt2triples_granite import text_to_triples


def normalize(t):
    """Normalize triple for comparison."""
    return tuple(str(x).strip().lower() for x in t)


def parse_output(output):
    """Parse model output to set of triples."""
    triples = set()
    if not output:
        return triples

    if isinstance(output, list):
        output_str = output[0] if output else ""
    else:
        output_str = output

    if not output_str or not output_str.strip():
        return triples

    output_str = output_str.strip().lower()

    # Handle "none" or empty responses
    if output_str in ("none", "[]", "n/a", "no triples"):
        return triples

    # Remove any leading explanation text before first (
    if '(' in output_str:
        output_str = output_str[output_str.index('('):]

    # Remove trailing explanation text after last )
    if ')' in output_str:
        output_str = output_str[:output_str.rindex(')') + 1]

    # Handle numbered lists like "1. (s; p; o)"
    import re
    output_str = re.sub(r'\d+\.\s*', '', output_str)

    # Split on ), ( pattern with flexible whitespace
    for t in re.split(r'\)\s*,\s*\(', output_str):
        t = t.strip('() \n\t')
        # Try semicolon first, then comma
        if ';' in t:
            parts = [p.strip().strip('"\'').lower() for p in t.split(';')]
        else:
            parts = [p.strip().strip('"\'').lower() for p in t.split(',')]
        if len(parts) == 3 and all(parts):
            triples.add(tuple(parts))

    return triples


def evaluate_test(test_id, test_data):
    """Evaluate single test case."""
    output = text_to_triples(test_data["text"])
    predicted = parse_output(output)

    expected = set(normalize(t) for t in test_data.get("extract", []))
    rejected = set(normalize(t) for t in test_data.get("reject", []))

    missed = expected - predicted
    hallucinations = predicted & rejected

    return {
        "test_id": test_id,
        "category": test_data.get("category", "unknown"),
        "input_text": test_data["text"],
        "raw_output": output,
        "missed": missed,
        "hallucinations": hallucinations,
        "passed": len(hallucinations) == 0 and len(missed) == 0,
    }


def run_all():
    """Run all tests and print results."""
    print("=" * 60)
    print("FAILURE MODE TEST SUITE - GRANITE 4")
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
            if r["missed"]:
                print(f"  - Missed: {r['missed']}")
            if r["hallucinations"]:
                print(f"  ! HALLUCINATION: {r['hallucinations']}")

        print(f"\nCategory: {passed}/{total} ({100*passed/total:.0f}%)")

    print(f"\n{'='*60}")
    print(f"TOTAL: {total_passed}/{total_tests} ({100*total_passed/total_tests:.0f}%)")
    print("=" * 60)

    # Save results for manual verification
    output_file = f"/home/helmut/natural-text-to-triples/test/results_granite_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(output_file, 'w') as f:
        for cat_key in CATEGORIES:
            if cat_key not in results_by_category:
                continue
            for r in results_by_category[cat_key]:
                f.write(f"{r['test_id']}\n")
                f.write(f"Input: {r['input_text']}\n")
                f.write(f"Output: {r['raw_output']}\n\n")
    print(f"\nResults saved to: {output_file}")


if __name__ == "__main__":
    run_all()
