import math

def max_odd(array = None):
    if type(array) is not list:
        return None
    result = -math.inf
    for item in array:
        if type(item) is int and item % 2:
            result = max(item, result)
        elif type(item) is float and item.is_integer() and int(item) % 2:
            result = max(int(item), result)
    if math.isinf(result):
        result = None
    return result



print(max_odd([]))                              # => 3
print(max_odd([21.0, 2, 3, 4, 4]))                           # => 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))             # => 3
print(max_odd(['ololo', 'fufufu']))                          # => None
print(max_odd([2, 2, 4]))                                    # => None
print(max_odd([[2, 2, 4]]))                                  # => None
print(max_odd([False, True]))                                # => None
