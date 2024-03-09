import argparse
import json
import csv


def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def process_json(data):
    result = []
    for item in data:
        result.append('_'.join([item['station'], item['name']]))
    return result


def update_csv(json_data, csv_file, start, end):
    start_col, start_row = start.split(':')
    end_col, end_row = end.split(':')

    start_col_index = ord(start_col.upper()) - 65
    start_row_index = int(start_row) - 1
    end_col_index = ord(end_col.upper()) - 65
    end_row_index = int(end_row) - 1

    if start_col_index > end_col_index or start_row_index > end_row_index:
        print("Error: Start and end positions are not in the correct order.")
        return

    with open(csv_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
        for col_index in range(start_col_index, end_col_index + 1):
            station = data[0][col_index]
            for row_index in range(start_row_index, end_row_index + 1):
                name = data[row_index][1]
                combined = "_".join([station, name])
                if combined in json_data:
                    data[row_index][col_index] = '✓'

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def main():
    parser = argparse.ArgumentParser(description='Process JSON data and map to CSV')
    parser.add_argument('-f', '--json_file', help='Input JSON file', required=True)
    parser.add_argument('-csv', '--csv_file', help='Output CSV file', required=True)
    parser.add_argument('--start', help='Start position (e.g., A:1)', required=True)
    parser.add_argument('--end', help='End position (e.g., E:5)', required=True)
    args = parser.parse_args()

    json_data = load_json(args.json_file)
    processed_json = process_json(json_data)
    update_csv(processed_json, args.csv_file, args.start, args.end)


if __name__ == "__main__":
    main()
