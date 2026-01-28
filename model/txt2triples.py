import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained("pat-jj/text2triple-flan-t5")
model = AutoModelForSeq2SeqLM.from_pretrained("pat-jj/text2triple-flan-t5").to(device)

def text_to_triples(input_text):

    inputs = tokenizer(input_text, return_tensors="pt").to(device)

    outputs = model.generate(**inputs)

    triples = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    return triples



import os

def load_examples(file_path):
    examples = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    input_text, gold_triples = parts
                    examples.append((input_text, gold_triples))
    return examples