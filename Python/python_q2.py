import json
import re


def run_filter():
    log_file_location = "/tmp/mylogfile.log"
    result = {}
    with open(log_file_location) as log_file:
        for line in log_file:
            stripped_line = line.strip()
            data_dict = extract_log_entry_data(stripped_line)
            classes_matched,filtered_data = filter_data_by_classification(data_dict)
            if classes_matched not in result: result[classes_matched] = []
            result[classes_matched].append(filtered_data)

    json_output = json.dumps(result, indent=4)
    print(json_output)


def extract_log_entry_data(line : str):
    data_extract_pattern = re.compile(r"""
                (?P<timestamp>.*)\ {{
                .*\ remote_addr:\ (?P<remote_address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
                .*\ request:\ (?P<request_type>[^ ]+)
                \ (?P<url>/[^ ]*)\ HTTP
                .*\ status:\ (?P<status>\d{3})
                .*\ http_user_agent:\ (?P<user_agent>[^ ]*)\ }}
                .*request_time:\ (?P<request_time>.*)\ }}
                .*request_length:\ (?P<request_length>.*)\ }}
                """, flags=re.X)
    result = data_extract_pattern.search(line).groupdict()
    result["timestamp_date"] = re.match(r'(\d{4}-\d{2}-\d{2})', result["timestamp"])

    return result


def filter_data_by_classification(data : dict):
    ip_range_pattern = re.compile(r"""
        (192\.168\.(?:[1-9]|10)\.(?:[1-9][0-9]?|1\d\d|2[0-4]\d|25[0-5]))
        """, flags=re.X)
    hour_range_pattern = re.compile(r"""
    .*T(1(?:8\:\d\d\:\d\d\+\d\d\:|9:00:00\+00\:00))
    """, flags=re.X)
    res_data = {}
    is_match_case_a = data["status"] == "200" and ip_range_pattern.match(data["remote_address"])
    is_match_case_b = float(data["request_time"]) > 1.0 and data["request_type"] == "POST"
    is_match_case_c = data["timestamp_date"] == "2020-07-01" and hour_range_pattern.match(data["timestamp"])

    classes_matched = set()

    if is_match_case_a:
        classes_matched.add('A')
        res_data["time_of_request"] = data["timestamp"]
        res_data["url"] = data["url"]
        res_data["user_agent"] = data["user_agent"]

    if is_match_case_b:
        classes_matched.add('B')
        res_data["remote_address"] = data["remote_address"]
        if "url" not in res_data: res_data["url"] = data["url"]
        res_data["request_length"] = data["request_length"]

    if is_match_case_c:
        classes_matched.add('C')
        res_data["request_time"] = data["request_time"]
        if "request_length" not in res_data: res_data["request_length"] = data["request_length"]
        if "remote_address" not in res_data: res_data["remote_address"] = data["remote_address"]

    result = (','.join(classes_matched), res_data)
    return result


if __name__ == '__main__':
    run_filter()





    # ip_range_re_pattern = re.compile(r'.*remote_addr: (192\.168\.(:[1-9]|10)\.(:[1-9][0-9]?|1\d\d|2[0-4]\d|25[0-5])).* status: (d{3})', flags=re.X | re.M)
    # ip_range_re_pattern = re.compile(r'.*remote_addr: (192\.168\.(:?[1-9]|10)\.(:?[1-9][0-9]?|1\d\d|2[0-4]\d|25[0-5]))')

    # ip_range_re_pattern = re.compile(
    #     r'''
    #     .*remote_addr: (192\.168\.(?:[1-9]|10)\.(?:[1-9][0-9]?|1\d\d|2[0-4]\d|25[0-5])) # get ip-address in range
    #     .* status: (d{3})   # get HTTP response code
    #     ''', flags=re.X | re.M)

    # data_extract_regex = re.compile(r'(.*) {{.*remote_addr: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).* request:.* (/[^ ]*) HTTP.* http_user_agent: ([^ ]*) }}.*request_time: (.*) }}.*request_length: (.*) }}')

    # data_extract_regex = re.compile(r"""
    #     (.*)\ {{
    #     .*\ remote_addr:\ (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
    #     .*\ request:.*\ (/[^ ]*)\ HTTP
    #     .*\ http_user_agent:\ ([^ ]*)\ }}
    #     .*request_time:\ (.*)\ }}
    #     .*request_length:\ (.*)\ }}
    #     """, flags=re.X)

    # time_of_request,remote_address,url,user_agent,request_time,request_length = data_extract_regex.search(line)

    # data_extract_pattern = re.compile(r"""
    #         (?P<timestamp>.*)\ {{
    #         .*\ remote_addr:\ (?P<remote_address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
    #         .*\ request:\ (?P<request_type>[^ ]+)
    #         \ (?P<url>/[^ ]*)\ HTTP
    #         .*\ status:\ (?P<status>\d{3})
    #         .*\ http_user_agent:\ (?P<user_agent>[^ ]*)\ }}
    #         .*request_time:\ (?P<request_time>.*)\ }}
    #         .*request_length:\ (?P<request_length>.*)\ }}
    #         """, flags=re.X)
    #
    # data = extract_log_entry_data(line)
    # data["timestamp_date"] = re.match(r'(\d{4}-\d{2}-\d{2})', data["timestamp"])