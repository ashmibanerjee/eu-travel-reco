import sys, os
import json

sys.path.append("../../../../")
from src.q_a_gen.preproc.clean_up_wiki import get_files
from src.q_a_gen.setup.prompts import GENERIC_PROMPT, LLAMA_PROMPT
from src.q_a_gen.models.gemini import get_multimodal_response
from src.q_a_gen.models.ollama import get_ollama_response, get_token_count
from src.utils.write import write_data

DATA_PATH = os.getcwd() + "/../../../data/europeancities-wikivoyage-tripadvisor/wikivoyage"
MODELS = ["gemini-1.5-flash", "gemini-1.0-pro", "phi3:medium"]


def generate_qa_pairs(model_name):
    city_files = get_files(DATA_PATH + "/cleaned")
    city_files.sort()
    print(f"Generating QA pairs for all cities using {model_name}...")
    if not os.path.exists(f"{DATA_PATH}/q_a/{model_name}"):
        os.makedirs(f"{DATA_PATH}/q_a/{model_name}")
    for city_file in city_files:
        print(f"\t{city_file}")
        city_name = city_file.split('.')[0]
        if f"{city_name}.json" in get_files(f"{DATA_PATH}/q_a/{model_name}"):
            print("\t\t QA pairs already generated!")
            continue
        else:
            with open(f"{DATA_PATH}/cleaned/{city_file}", 'r') as file:
                data = file.read()
            try:
                qa_pairs = get_model_response(model_name, data)
            except ValueError:
                print(f"\t\t Skipping city...{city_name}")
                continue
            file_path = f"{DATA_PATH}/q_a/{model_name}"
            write_data(city_name, qa_pairs, file_path)
            print("\t\t QA pairs generated!")


def get_model_response(model_name: str, data: str):
    match model_name:
        case "gemini-1.5-flash" | "gemini-1.0=5-pro":
            content = [GENERIC_PROMPT, data]
            model_response = get_multimodal_response(content, model_name)
        case "phi3:medium":
            content = GENERIC_PROMPT + data
            # token_count = get_token_count(content, "meta-llama/Meta-Llama-3-8B")
            model_response = get_ollama_response(model_name, content)
        case _:
            raise ValueError("Invalid model name")
    return model_response


if __name__ == "__main__":
    generate_qa_pairs(MODELS[2])
