def connect_dicts(dict1 = None, dict2 = None):
    if type(dict1) is not dict or type(dict2) is not dict:
        return None
    if not all(type(val) in (int, float) for val in dict1.values()):
        return None
    if not all(type(val) in (int, float) for val in dict2.values()):
        return None
    if sum(dict1.values()) > sum(dict2.values()):
        dict1, dict2 = dict2, dict1
    new_dict = {**dict1, **dict2}
    return dict(sorted(filter(lambda item: item[1] >= 10, new_dict.items()), key = lambda item: item[1]))

if __name__ == "__main__":
    print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))            # =>     {"c": 11, "b": 12}
    print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))  # =>     {d: 11, "c": 12, "a": 13}
    print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))          # =>     {"c": 11, "b": 12, "a": 15}
    print(connect_dicts())                                                # =>     None
    print(connect_dicts({"a": 12}, {(1, 3): 45}))                         # =>     {'a': 12, (1, 3): 45}
    print(connect_dicts({"a": 12}, {"b": [7]}))                           # =>     None
