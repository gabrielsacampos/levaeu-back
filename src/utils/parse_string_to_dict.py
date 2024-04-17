def parse_string_to_dict(input_string):
    if isinstance(input_string, dict):
        return input_string
    elif isinstance(input_string, str):
        pairs = input_string.split(", ")
        result = {}
        for pair in pairs:
            key, value = pair.split("=")
            result[key] = value
        return result
    else:
        raise ValueError("Unsupported input type")