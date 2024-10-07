import os
import re

DATA_PATH = os.getcwd() + "/../../../data/europeancities-wikivoyage-tripadvisor/wikivoyage/"


def get_files(data_path: str):
    city_files = []
    for file in os.listdir(data_path):
        city_files.append(file)
    return city_files


def clean_up_wiki_data():
    city_files = get_files(DATA_PATH + "original")
    # Regular expression to find the portions for removal
    pattern = r"\{\{pagebanner\|.*?\}\}|\[\[File:.*?\]\]|\{\{see also.*?\}\}|\{\{mapframe.*?\}\}|\{\{" \
              r"mapshapes.*?\}\}|\[\[Image:.*?\]\]|\{\{routebox.*?\}\}|\{\{guidecity.*?\}\}|\{\{geo.*?\}\}|\{\{" \
              r"IsPartOf.*?\}\} "
    for city_file in city_files:
        with open(f"{DATA_PATH}/original/{city_file}", 'r') as file:
            data = file.read()
        city_name = city_file.split('_')[1].split(".")[0]
        cleaned_text = re.sub(pattern, "", data, flags=re.DOTALL).strip()
        with open(f"{DATA_PATH}/cleaned/{city_name}.txt", "w") as text_file:
            text_file.write(cleaned_text)


if __name__ == "__main__":
    clean_up_wiki_data()
    print("Wiki data cleaned up!")
