from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

MODEL_PATH = "pat-jj/text2triple-flan-t5"

tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)
model = T5ForConditionalGeneration.from_pretrained(
    MODEL_PATH,
    device_map="auto",
    torch_dtype=torch.bfloat16
)


def text_to_triples(input_text):
    inputs = tokenizer(
        input_text,
        max_length=512,
        padding='max_length',
        truncation=True,
        return_tensors="pt"
    )

    input_ids = inputs['input_ids'].to(model.device)
    attention_mask = inputs['attention_mask'].to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_length=512,
            num_beams=4,
            early_stopping=True,
            length_penalty=0.6,
            use_cache=True
        )

    triples = tokenizer.decode(outputs[0], skip_special_tokens=True)
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