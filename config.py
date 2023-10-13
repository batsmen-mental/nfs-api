

def format_json_response(status_code, query_time, data, errors):
    formatted_json_response = "{\"status_code\": " + status_code + ",\"body\": {\"meta\": \"query_time\": " + query_time + "},\"data\": \"" + data + "\",\"errors\": \"" + errors + "\"}}"
    return formatted_json_response