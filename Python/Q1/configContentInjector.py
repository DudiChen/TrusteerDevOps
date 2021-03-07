import json
from flask import request, jsonify


def inject_config_content():
    config_file_location = "/data/python/config.json"
    with open(config_file_location, "r+") as config_file:
        config_data = json.load(config_file)
        # config_data = {}
        url = config_data["url"]
        content_value = get_content_value_by_url(url)
        config_data["content"] = content_value
        json.dump(config_data, config_file)


def get_content_value_by_url(content_url):
    # req_params = {}
    content_length = 15
    response = request.get(url=content_url)
    return response[:content_length]


if __name__ == '__main__':
    inject_config_content()
