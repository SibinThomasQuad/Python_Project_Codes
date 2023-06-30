import json

class JSONUtils:
    @staticmethod
    def add_key_value(json_str, key, value):
        json_obj = json.loads(json_str)
        json_obj[key] = value
        return json.dumps(json_obj)

    @staticmethod
    def json_to_object(json_str):
        return json.loads(json_str)

    @staticmethod
    def json_to_dict(json_str):
        return json.loads(json_str)

    @staticmethod
    def remove_key(json_str, key):
        json_obj = json.loads(json_str)
        if key in json_obj:
            del json_obj[key]
        return json.dumps(json_obj)

    @staticmethod
    def dict_to_json(dictionary):
        return json.dumps(dictionary)
