import json
import requests
from flask import request, jsonify


def inject_config_content():
    config_file_location = "/data/python/config.json"
    try:
        with open(config_file_location, "r") as config_file:
            config_data = json.load(config_file)
    except FileNotFoundError:
        print("ERROR - couldn't find the file: " + config_file_location)
    except IOError:
        print("ERROR - couldn't read the file: " + config_file_location)
    req_url = config_data["url"]
    content_value = get_content_value_by_url(req_url)
    config_data["content"] = content_value
    try:
        with open(config_file_location, "w") as config_file:
            json.dump(config_data, config_file)
    except FileNotFoundError:
        print("ERROR - couldn't find the file: " + config_file_location)
    except IOError:
        print("ERROR - couldn't write to file: " + config_file_location)


def get_content_value_by_url(content_url):
    # # req_params = {}
    content_length = 15
    response = requests.get(url=content_url)
    # req_params = {'lastdays': 30}
    # response = requests.get(url=content_url, params=req_params)
    # TEST:
    # print("TYPE: " + str(type(response.text)))
    # print(str(response.text))

    return response.text[:content_length]


if __name__ == '__main__':
    inject_config_content()
