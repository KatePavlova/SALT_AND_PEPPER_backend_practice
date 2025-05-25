
def sort_list(List = None):
    if type(List) is not list:
        return None
    if not List:
        return []
    min_list = min(List)
    max_list = max(List)
    for i in range(len(List)):
        if List[i] == min_list:
            List[i] = max_list
        elif List[i] == max_list:
            List[i] = min_list
    List.append(min_list)
    return List



'''
print(max([1,2]))
print(sort_list([]))                    # => []
print(sort_list([2, 4, 6, 8]))          # => [8, 4, 6, 2, 2]
print(sort_list([1]))                   # => [1, 1]
print(sort_list([1, 2, 1, 3]))          # => [3, 2, 3, 1, 1]
'''