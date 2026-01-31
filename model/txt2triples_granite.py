from ollama import chat

MODEL = "granite4"

PROMPT = """Extract semantic triples from the text below.

Rules:
1. Output ONLY triples in this exact format: (subject; predicate; object)
2. Multiple triples separated by commas: (s1; p1; o1), (s2; p2; o2)
3. If no valid triples can be extracted, output: NONE
4. Only extract facts explicitly stated in the text
5. Do not add external knowledge not present in the text
6. Resolve pronouns only when the referent is unambiguous
7. Preserve negation and modality (e.g., "might not", "did not")
8. Use lowercase for all text

Examples:

# Basic extraction
Text: Einstein developed the theory of relativity.
Output: (einstein; developed; theory of relativity)

# Coreference - resolve only when unambiguous
Text: The Transformer architecture was introduced by Vaswani et al. It revolutionized NLP.
Output: (transformer; introduced by; vaswani et al), (transformer; revolutionized; nlp)

# Coreference - ambiguous pronoun, cannot resolve
Text: John told Mike that he was promoted.
Output: NONE

# Pattern matching - physically impossible, reject
Text: The mountain climbed the hiker.
Output: NONE

# Pattern matching - nonsensical scale
Text: The ant carried the car to the garage.
Output: NONE

# Commonsense - physically impossible
Text: John put the elephant in his pocket.
Output: NONE

# Negation - preserve modality
Text: The doctor said the patient might not require surgery.
Output: (doctor; said; patient might not require surgery)

# Negation - preserve negation
Text: Smoking does not improve health.
Output: (smoking; does not improve; health)

# Faithfulness - do not add external knowledge
Text: Marie Curie conducted research on radioactivity.
Output: (marie curie; conducted research on; radioactivity)

# Faithfulness - attributed claim, keep attribution
Text: John claimed that the project was a success.
Output: (john; claimed; project was success)

# Temporal - preserve tense and time context
Text: Steve Jobs was the former CEO of Apple.
Output: (steve jobs; was former ceo of; apple)

# Temporal - future plans, not facts
Text: SpaceX plans to send humans to Mars by 2030.
Output: (spacex; plans to send; humans to mars)

# Hypothetical - do not extract as fact
Text: If the experiment had succeeded, we would have proven the hypothesis.
Output: NONE

# Valid factual statement
Text: Mount Everest is taller than Mount Fuji.
Output: (mount everest; taller than; mount fuji)

Text: {text}
Output:"""


def text_to_triples(input_text):
    prompt = PROMPT.format(text=input_text)

    response = chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={
            "temperature": 0,
            "num_predict": 256,
        }
    )

    return response.message.content.strip()
