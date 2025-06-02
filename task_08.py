def multiply_numbers(inputs = ''):
    inputs = str(inputs)
    digits = [char for char in inputs if char.isdigit()]
    return None if not digits else eval('*'.join(digits))

if __name__ == "__main__":
    print(multiply_numbers())                          # => None
    print(multiply_numbers('ss'))                      # => None
    print(multiply_numbers('1234'))                    # => 24
    print(multiply_numbers('sssdd34'))                 # => 12
    print(multiply_numbers(2.3))                       # => 6
    print(multiply_numbers([5, 6, 4]))                 # => 120
    print(multiply_numbers([5, 6, [4]]))               # => 120
    print(multiply_numbers([5, ['6&', '#1'], [4]]))    # => 120
    print(multiply_numbers(True))                      # => None
    print(multiply_numbers({'23': 2, 'wer': 5}))       # => 60
    print(multiply_numbers('ss2'))                     # => 2