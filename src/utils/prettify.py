import json
import os
import sys

sys.path.append("../")

from src.q_a_gen.preproc.clean_up_wiki import get_files

DATA_PATH = os.getcwd() + "/../../data/europeancities-wikivoyage-tripadvisor/wikivoyage"

import pprint
def prettify_json(model_name: str):
    city_files = get_files(DATA_PATH + f"/q_a/{model_name}")
    for city_file in city_files:
        print(f"\t{city_file}")
        with open(f"{DATA_PATH}/q_a/{model_name}/{city_file}", 'r') as file:
            data = file.read()
        data = json.loads(data)
        # print json to screen with human-friendly formatting
        updated_data = pprint.pformat(data)

        with open(f"{DATA_PATH}/q_a/{model_name}/{city_file}", "w") as f:
            json.dump(updated_data, f, ensure_ascii=True, indent=4, sort_keys=False)


if __name__ == "__main__":
    prettify_json("gemini-1.5-flash")
