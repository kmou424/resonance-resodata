import argparse
import csv
import json
import os

def process_csv_to_json(input_file, output_file, start, end, padding):
    data_dict = {}
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

        start_col, start_row = start.split(':')
        end_col, end_row = end.split(':')

        start_col_index = ord(start_col.upper()) - 65
        start_row_index = int(start_row) - 1
        end_col_index = ord(end_col.upper()) - 65
        end_row_index = int(end_row) - 1

        if start_col_index > end_col_index or start_row_index > end_row_index:
            print("Error: Start and end positions are not in the correct order.")
            return

        for col_index in range(start_col_index, end_col_index + 1):
            station = data[0][col_index]
            for row_index in range(start_row_index, end_row_index + 1):
                cell_value = data[row_index][col_index].strip()
                if len(cell_value) == 12:
                    id_value = cell_value
                    name = data[row_index][1]
                    if id_value not in data_dict:
                        data_dict[id_value] = {"id": id_value, "name": name, "station": station}
                        data[row_index][col_index] = padding

    json_data = list(data_dict.values())
    with open(output_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile, ensure_ascii=False, indent=4)

    with open(input_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def main():
    parser = argparse.ArgumentParser(description='Process CSV to JSON')
    parser.add_argument('-f', '--input_file', type=str, help='Input CSV file')
    parser.add_argument('-o', '--output_file', type=str, help='Output JSON file')
    parser.add_argument('--start', type=str, help='Start position (e.g., A:1)')
    parser.add_argument('--end', type=str, help='End position (e.g., E:5)')
    parser.add_argument('--padding', type=str, default='✓', help='Padding value to replace cell content')
    args = parser.parse_args()

    if not all([args.input_file, args.output_file, args.start, args.end]):
        parser.error("Please provide input_file, output_file, start, and end arguments.")

    if not os.path.isfile(args.input_file):
        print("Error: Input file does not exist.")
        return

    process_csv_to_json(args.input_file, args.output_file, args.start, args.end, args.padding)

if __name__ == "__main__":
    main()

