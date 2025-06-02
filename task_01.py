import re

def is_palindrome(string = ""):
    string = str(string)
    new_string = re.sub(r'([\W_])', '', string.lower())
    return new_string == new_string[::-1]


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal -- Panama"))    # => True
    print(is_palindrome("Madam, I'm Adam!"))                    # => True
    print(is_palindrome(333))                                   # => True
    print(is_palindrome(None))                                  # => False
    print(is_palindrome("Abracadabra"))                         # => False
    print(is_palindrome([1, 32.3, 1]))                          # => True
    print(is_palindrome("   "))                                 # => True
    print(is_palindrome())                                      # => True


