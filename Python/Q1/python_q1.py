import json
import requests
from flask import request, jsonify


def inject_config_content():
    config_file_location = "/data/python/config.json"
    with open(config_file_location, "r+") as config_file:
        config_data = json.load(config_file)
        # req_url = config_data["url"]
        # -------------------v
        country = "Israel"
        server_url = "https://corona.lmao.ninja/v2/"
        historical_request_suffix = "historical/"
        req_url = server_url + historical_request_suffix + country
        # -------------------^
        content_value = get_content_value_by_url(req_url)
        print("TEST: " + content_value)
        config_data["content"] = content_value
        json.dump(config_data, config_file)


def get_content_value_by_url(content_url):
    # # req_params = {}
    content_length = 15
    # response = request.get(url=content_url)
    req_params = {'lastdays': 30}
    response = requests.get(url=content_url, params=req_params)
    # TEST:
    print("TYPE: " + type(response))
    print(response)

    return response[:content_length]


if __name__ == '__main__':
    inject_config_content()
