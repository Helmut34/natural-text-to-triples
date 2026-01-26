from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("pat-jj/text2triple-flan-t5")
model = AutoModelForSeq2SeqLM.from_pretrained("pat-jj/text2triple-flan-t5")

def text_to_triples(input_text):

    inputs = tokenizer(input_text, return_tensors="pt")

    outputs = model.generate(**inputs)

    triples = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    return triples


triples = text_to_triples(paragraph)
print(triples)


import os

def run_context_tests(data_dir="data"):
    for i in range(1, 6):
        file_path = os.path.join(data_dir, f"p{i}.md")
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read().strip()
        print(f"---\nInput from p{i}.md:\n{text}\n")
        triples = text_to_triples(text)
        print(f"Extracted triples:\n{triples}\n")

run_context_tests()