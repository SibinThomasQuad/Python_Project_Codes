import json
import base64
import pickle
from xml.etree.ElementTree import Element, ElementTree, tostring, fromstring


class DataMarshaller:
    def __init__(self, data):
        self.data = data

    def json_encode(self):
        return json.dumps(self.data)

    def json_decode(self, json_str):
        return json.loads(json_str)

    def xml_encode(self):
        root = Element('data')
        self._encode_dict(self.data, root)
        return tostring(root, encoding='utf-8').decode('utf-8')

    def xml_decode(self, xml_str):
        root = fromstring(xml_str)
        return self._decode_dict(root)

    def base64_encode(self):
        data_bytes = pickle.dumps(self.data)
        return base64.b64encode(data_bytes).decode('utf-8')

    def base64_decode(self, base64_str):
        data_bytes = base64.b64decode(base64_str)
        return pickle.loads(data_bytes)

    def pickle_serialize(self):
        return pickle.dumps(self.data)

    def pickle_deserialize(self, pickle_bytes):
        return pickle.loads(pickle_bytes)

    def _encode_dict(self, data, parent):
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    child = Element(str(key))
                    parent.append(child)
                    self._encode_dict(value, child)
                else:
                    element = Element(str(key))
                    element.text = str(value)
                    parent.append(element)
        elif isinstance(data, list):
            for item in data:
                element = Element('item')
                parent.append(element)
                self._encode_dict(item, element)

    def _decode_dict(self, element):
        data = {}
        for child in element:
            if child.tag == 'item':
                if 'items' not in data:
                    data['items'] = []
                data['items'].append(self._decode_dict(child))
            else:
                data[child.tag] = self._decode_dict(child) if child else None
        return data
