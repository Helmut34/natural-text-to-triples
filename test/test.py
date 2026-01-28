from model.txt2triples import text_to_triples
from gold_triples import GOLD

for filename, gold_triples in GOLD.items():
    text = open(f"data/{filename}").read()
    predicted = text_to_triples(text)
    p, r, f1 = compute_metrics(predicted, set(gold_triples))
    print(f"{filename}: P={p:.2f}, R={r:.2f}, F1={f1:.2f}")
