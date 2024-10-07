from transformers import AutoTokenizer, AutoModelForCausalLM
from ..utils.loaders import load_data

def load_model():
    output_dir = "../../models/gemma-2b-travel-qa"
    tokenizer = AutoTokenizer.from_pretrained(output_dir)
    finetuned_model = AutoModelForCausalLM.from_pretrained(output_dir, load_in_4bit=True, device_map="auto")
    return tokenizer, finetuned_model

def load_test_data():
    repo_name = "ashmib/wikivoyage-eu-cities-qa"
    test_data = load_data(repo_name, data_files=None, is_public=True, split_name="test")
    return test_data

def generate_answers(query, tokenizer, finetuned_model):
    inputs = tokenizer(query, return_tensors="pt")
    response = finetuned_model.generate(**inputs, max_new_tokens=1024)
    return response


def main():
    test_data = load_test_data()
    print("Test data loaded")

