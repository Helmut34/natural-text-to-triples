# Natural Text to Triples

An experimental project to evaluate LLM-based extraction of semantic triples (subject, predicate, object) from natural language text.

## Project Status: Not Viable

After comprehensive testing, this approach was deemed **not viable** for the current implementation needs due to significant accuracy limitations.

## Evaluation Results

The model achieved an overall accuracy of **31% (13/42 tests passed)**, which is insufficient for reliable triple extraction.

### Conclusion

The model struggles with nuanced language understanding required for reliable triple extraction. While it performs adequately on simple pattern-matching tasks and basic commonsense reasoning, it fails on the more complex linguistic phenomena that are essential for real-world applications:

- Cannot track entity state changes over time
- Cannot resolve references across sentences
- Cannot handle domain-specific terminology
- Cannot distinguish between stated facts and hedged/attributed claims

These limitations make the current approach unsuitable for production use cases requiring accurate knowledge graph construction or semantic information extraction.
