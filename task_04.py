
def sort_list(List = None):
    if type(List) is not list:
        return None
    if not List:
        return []
    min_list = List[0]
    max_list = List[0]

    for item in List:
        if type(item) is not int:
            return None
        min_list = min(item, min_list)
        max_list = max(item, max_list)

    result = [min_list if item == max_list else max_list if item == min_list else item for item in List]
    result.append(min_list)
    return result



if __name__ == "__main__":
    print(sort_list([]))                    # => []
    print(sort_list([2, 4, 6, 8]))          # => [8, 4, 6, 2, 2]
    print(sort_list([1]))                   # => [1, 1]
    print(sort_list([1, 2, 1, 3]))          # => [3, 2, 3, 1, 1]
    print(sort_list([1, 2, 1, [1, 4]]))     # => None
    print(sort_list())                      # => None
