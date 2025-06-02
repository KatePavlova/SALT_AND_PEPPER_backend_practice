def combine_anagrams(words_array = None):
    if type(words_array) is not list:
        return []
    dict = {}
    for word in words_array:
        if type(word) is not str or not word.isalpha():
            return []
        word_lower = word.lower()
        hist = [0] * 26
        for char in word_lower:
            hist[ord(char) - ord('a')] += 1
        anagrams = dict.setdefault(tuple(hist), [])
        anagrams.append(word)
    return [val for val in dict.values()]


if __name__ == "__main__":
    print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))
    # => [['cars', 'racs', 'scar'], ['for'], ['potatoes'], ['four'], ['creams', 'scream']]
    print(combine_anagrams("wolf"))
    # => []
    print(combine_anagrams([[1, 4], 'wolf']))
    # => []
    print(combine_anagrams(['df@g', 'wolf']))
    # => []