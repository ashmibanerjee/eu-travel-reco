from transformers import AutoTokenizer
import os
from dotenv import load_dotenv
import ollama
load_dotenv()
HF_TOKEN = os.environ["HF_TOKEN"]
import torch


def check_backend():
    if (torch.backends.mps.is_available()) and (torch.backends.mps.is_built()):
        torch.set_default_device("mps")
        print("setting default to mps")
    else:
        torch.set_default_device("cuda")
        print("setting default to cuda")


def get_ollama_response(model_name: str, content: str):
    check_backend()
    response = ollama.generate(model=model_name, prompt=content)
    return response["message"]["content"]


def get_token_count(prompt: str, model_name: str):
    tokenizer = AutoTokenizer.from_pretrained(model_name, token=HF_TOKEN)
    tokens = tokenizer.tokenize(prompt)
    num_tokens = len(tokens)
    print(f"Number of tokens in your text: {num_tokens}")
    return num_tokens
