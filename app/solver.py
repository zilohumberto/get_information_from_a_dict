import json
from app.utils import Utils


class Solver(Utils):
    data = None
    expected_data = None

    def __init__(self, data, expected_data):
        self.data = data
        self.expected_data = expected_data

    def transform(self):
        self.data = json.loads(self.data)
        self.expected_data = self.expected_data

    def start(self):
        self.transform()
        output = dict()
        for expected in self.expected_data:
            candidate = self.find_output(expected, self.data)
            if candidate:
                output[expected] = candidate
        return output

    def find_output(self, key, candidate):
        for dot in self.get_dots(key):
            key = self.get_key(dot)
            if key:
                if self.is_valid_dict(key, candidate):
                    candidate = candidate[key]
                else:
                    return None

            for complete_key in self.get_array(dot):
                index = self.get_index(complete_key)
                if self.is_valid_iterable(index, candidate):
                    candidate = candidate[index]
                else:
                    return None

        return candidate
