import re

def count_words(string = ''):
    string = str(string).lower()
    words_array = re.split(r'[^a-z]+', string)
    dict_count = {}
    for word in words_array:
        if word:
            dict_count[word] = dict_count.setdefault(word, 0) + 1

    return dict_count


if __name__ == "__main__":
    print(count_words("A man, a plan, a canal -- Panama"))  # => {'a': 3, 'man': 1, 'plan': 1, 'canal': 1, 'panama': 1}
    print(count_words("Doo bee doo bee doo"))               # => {"doo": 3, "bee": 2}
    print(count_words())                                    # => {}
    print(count_words("    "))                              # => {}
    print(count_words(" &$@ Doo bee234doo bee @ doo &&&$")) # => {"doo": 3, "bee": 2}
