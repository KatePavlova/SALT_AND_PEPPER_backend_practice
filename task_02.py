def coincidence(List = None, Range = None):
    if type(List) is not list or type(Range) is not range:
        return []
    return [elem for elem in List if type(elem) in (int, float) and Range.start <= elem < Range.stop]

'''
print(coincidence([1, 2, 3, 4, 5], range(3, 6)))                  # => [3, 4, 5]
print(coincidence())                                              # => []
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))      # => [1, 2, 2.5]
print(coincidence([True, False, [1, 3], 0.5, 1.5], range(0, 2)))  # => [0.5, 1.5]
'''
