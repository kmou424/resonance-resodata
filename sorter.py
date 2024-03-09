import argparse
import json

from collections import defaultdict
from pypinyin import pinyin, Style


def main():
    parser = argparse.ArgumentParser(description='Process JSON data with comments')
    parser.add_argument('-f', '--file', type=str, help='Input file path')
    parser.add_argument('-s', '--sort_key', type=str, default='name', help='Key to sort the data')
    parser.add_argument('-g', '--group_key', type=str, default='station', help='Key to group the data')
    parser.add_argument('-o', '--output', type=str, help='Output file name')

    args = parser.parse_args()

    with open(args.file, "r", encoding='utf-8') as file:
        json_data_str = file.read()
    parsed_json_data = json.loads(json_data_str)

    existed_keys = []
    json_data = []
    for ele in parsed_json_data:
        if isinstance(ele, dict):
            if ele['id'] in existed_keys:
                continue
            json_data.append(ele)
            existed_keys.append(ele['id'])

    sorted_data = sorted(json_data, key=lambda x: pinyin(x.get(args.sort_key), style=Style.NORMAL))

    grouped_data = defaultdict(list)
    for item in sorted_data:
        grouped_data[item[args.group_key]].append(item)

    sorted_grouped_data = dict(sorted(grouped_data.items(), key=lambda x: x[0]))

    output_json = []

    for group_key, group in sorted_grouped_data.items():
        output_json.append("-" * 15 + group_key + "-" * 14 + ">")
        output_json.extend(group)
        output_json.append("<" + "-" * 14 + group_key + "-" * 15)

    output_json_str = json.dumps(output_json, ensure_ascii=False, indent=2, separators=(',', ': '))

    if args.output:
        output_file = args.output
    else:
        output_file = args.file.replace('.json', '_out.json')

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(output_json_str)


if __name__ == "__main__":
    main()
