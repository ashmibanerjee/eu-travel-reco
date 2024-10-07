from transformers import AutoTokenizer, AutoModelForCausalLM
import sys

sys.path.append("../../")
from src.utils.loaders import load_data


def load_model():
    output_dir = "../../models/gemma-2b-travel-qa"
    tokenizer = AutoTokenizer.from_pretrained(output_dir)
    finetuned_model = AutoModelForCausalLM.from_pretrained(output_dir, load_in_4bit=True, device_map="auto")
    return tokenizer, finetuned_model


def load_test_data():
    repo_name = "ashmib/wikivoyage-eu-cities-qa"
    test_data = load_data(repo_name, data_files=None, is_public=True, split_name="test")
    test_data.format(type="pandas")
    return test_data


def generate_answers(query, tokenizer, finetuned_model):
    inputs = tokenizer(query, return_tensors="pt")
    response = finetuned_model.generate(**inputs, max_new_tokens=1024)
    return response


def main():
    test_data = load_test_data()
    print("Test data loaded")
    tokenizer, finetuned_model = load_model()
    responses = []
    for i in range(len(test_data)[:2]):
        query = test_data[i]["prompt"]
        response = generate_answers(query, tokenizer, finetuned_model)
        response.append(response)
    test_data["llm_response"] = responses
    test_data.save_to_disk("../../data/eval/gemma-2b-travel-qa-answers.csv")


if __name__ == "__main__":
    main()
