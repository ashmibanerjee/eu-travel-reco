import os, json, csv
from collections import defaultdict

DATA_PATH = os.getcwd() + "/../../data/europeancities-wikivoyage-tripadvisor/wikivoyage/q_a/"


def merge_city_data(base_dir: str):
    """
    Merges JSON files for each city into a single JSON file for each city.
    """
    merged_data = defaultdict(list)

    for subdir, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.json'):
                city_name = file[:-5]  # Remove '.json' from the filename to get the city name
                file_path = os.path.join(subdir, file)

                with open(file_path, 'r') as f:
                    data = json.load(f)
                    merged_data[city_name].append(data)

    # Create a directory to store the merged files
    merged_dir = os.path.join(base_dir, 'merged')
    os.makedirs(merged_dir, exist_ok=True)

    # Write merged data to new JSON files
    for city, data_list in merged_data.items():
        merged_file_path = os.path.join(merged_dir, f'{city}.json')
        with open(merged_file_path, 'w') as f:
            json.dump(data_list, f, indent=4)


def merge_json_files(directory):
    """
    Merges all JSON files in a directory into a single JSON file.
    """
    merged_data = []

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                merged_data.append(data)

    merged_file_path = os.path.join(directory + "../", 'cities_qa_merged.json')
    with open(merged_file_path, 'w') as merged_file:
        json.dump(merged_data, merged_file, indent=4)
    print(f'Merged data written to {merged_file_path}')


def json_to_csv():
    data_file = DATA_PATH + "cities_qa_merged.json"
    with open(data_file, 'r') as file:
        json_data = json.load(file)

    csv_file_path = DATA_PATH + "cities_qa_merged.csv"
    # Open the CSV file for writing
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header row
        csv_writer.writerow(['city', 'prompt', 'answer'])

        # Iterate through the JSON data and write rows to the CSV file
        for city_data in json_data:
            try:
                city = city_data[0]['city']
                print(f'Writing data for {city}')
                for idx in range(0,2):
                    for qa in city_data[idx]['q_a']:
                        question = qa['q']
                        answer = qa['a']
                        csv_writer.writerow([city, question, answer])

            except:
                continue
    print(f'CSV file written to {csv_file_path}')


if __name__ == "__main__":
    # Make sure you run this only once to avoid creating duplicate merged files
    # merge_city_data(DATA_PATH)
    # merge_json_files(DATA_PATH + "merged/")
    json_to_csv()