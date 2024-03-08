import argparse
import json
from urllib.parse import urlparse, parse_qs

import requests

URL = "https://reso-data.kmou424.moe/api/fetch/full_goods_info?show=unknown"


def parse_json_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    need_check_stations_map = {}
    for item in data:
        station = item.get('station')
        if station not in need_check_stations_map:
            need_check_stations_map[station] = []
        need_check_stations_map[station].append(item)
    return need_check_stations_map


def parse_response(station, token):
    parsed_url = urlparse(URL)
    query_params = parse_qs(parsed_url.query)
    query_params['station'] = station
    if token:
        query_params['token'] = token
    # parsed_url = parsed_url._replace(query=urlencode(query_params, doseq=True))
    # actual_url = urlunparse(parsed_url)
    # print(f"fetching json data as standard data: {actual_url}")
    response = requests.get(URL, params=query_params)
    data = response.json()
    remote_stations_id_map = {}
    for item in data:
        remote_stations_id_map[item['id']] = item
    return remote_stations_id_map


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", help="JSON file name")
    parser.add_argument("--token", help="Token for authentication", default=None)
    args = parser.parse_args()

    need_check_stations_map = parse_json_file(args.f)
    for station, items in need_check_stations_map.items():
        remote_stations_id_map = parse_response(station, args.token)
        for item in items:
            if item['id'] in remote_stations_id_map:
                print(f"{item['id']} - {item['name']} - {item['station']} -> price:{remote_stations_id_map[item['id']]['price']}")
            else:
                print(f"{item['id']} - {item['name']} - {item['station']} -> not found")


if __name__ == "__main__":
    main()
