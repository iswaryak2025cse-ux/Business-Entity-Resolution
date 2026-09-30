from difflib import SequenceMatcher


def string_similarity(value1, value2):
    value1 = str(value1)
    value2 = str(value2)

    return SequenceMatcher(None, value1, value2).ratio()