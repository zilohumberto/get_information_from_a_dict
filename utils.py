import re


class Utils(object):

    @staticmethod
    def get_dots(key):
        return key.split(".")

    @staticmethod
    def get_array(data):
        return re.findall(r"\[[0-9]\]", data)

    @staticmethod
    def get_index(key):
        return int(key[1:-1])

    @staticmethod
    def get_key(key):
        return key.split('[')[0]

    @staticmethod
    def is_valid_iterable(index, candidate):
        if isinstance(candidate, list):
            return index < len(candidate)
        return False

    @staticmethod
    def is_valid_dict(key, candidate):
        if isinstance(candidate, dict):
            return key in candidate
        return False
