import os, json


def convert_to_json(qa_pairs: str):
    qa_pairs = qa_pairs.replace("```", '')
    qa_pairs = qa_pairs.replace("json\n", "")
    try:
        qa_pairs = json.loads(qa_pairs)
        return qa_pairs
    except:
        return None


def write_data(city_name: str, qa_pairs: str, file_path: str = None):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    qa_pairs = convert_to_json(qa_pairs)
    with open(f"{file_path}/{city_name}.json", "w") as f:
        json.dump(qa_pairs, f, indent=4)
