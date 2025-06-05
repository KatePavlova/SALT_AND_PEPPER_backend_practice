class BlockTranspositionCipher:
    def __init__(self, text, key, decrypt=False):
        if type(text) is not str:
            raise ValueError("Attribute text expects a string value, not a {0}".format(type(text)))
        if type(key) is not str:
            raise ValueError("Attribute key expects a string value, not a {0}".format(type(key)))
        if type(decrypt) is not bool:
            raise ValueError("Attribute decrypt expects a boolean value, not a {0}".format(type(decrypt)))

        key = key.lower()

        if not (key.isalpha() and key.isascii()):
            raise ValueError("Only string from the English alphabet should be used as a key")

        sz_text = len(text)
        sz_block = len(key)
        cnt_block = (sz_text + sz_block - 1) // sz_block

        if len(set(key)) != sz_block:
            raise ValueError("All characters in the key must be unique")
        if sz_text % sz_block != 0:
            if decrypt:
                raise ValueError("The length of the encrypted text is not a multiple of the key length")
            else:
                text = text.ljust(cnt_block * sz_block)

        sorted_key = sorted(key)

        self.__text = text
        self.__decrypt = decrypt
        self.__size_text = len(text)
        self.__size_block = len(key)
        self.__current = 0
        self.__num_of_blocks = cnt_block
        self.__key = [sorted_key.index(k) for k in key]

    def __iter__(self):
        self.__current = 0
        return self

    def __next__(self):
        if self.__current < self.__num_of_blocks:
            sz_block = self.__size_block
            cur = self.__current
            block = self.__text[cur * sz_block:(cur + 1) * sz_block]
            value = [""] * sz_block
            if self.__decrypt:
                for i in range(sz_block):
                    value[self.__key[i]] = block[i]
            else:
                for i in range(sz_block):
                    value[i] = block[self.__key[i]]

            value = ''.join(value)
            if self.__decrypt and self.__current == self.__num_of_blocks - 1:
                value = value.rstrip()
            self.__current += 1
            return value
        else:
            raise StopIteration


if __name__ == "__main__":

    # Шифрование с явной итерацией по блокам

    text = "HELLOWORLD"
    key = "bAc"

    print("Процесс шифрования по блокам:")
    cipher = BlockTranspositionCipher(text, key)
    for i, encrypted_block in enumerate(cipher, 1):
        print(f"Блок {i}: '{encrypted_block}'")

    # Полное шифрование

    encrypted = ''.join(cipher)
    print(f"\nПолный зашифрованный текст: '{encrypted}'")

    # Дешифрование с итерацией

    print("\nПроцесс дешифрования по блокам:")
    decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
    for i, decrypted_block in enumerate(decipher, 1):
        print(f"Блок {i}: '{decrypted_block}'")

    # Полное дешифрование с обрезкой пробелов

    decrypted = ''.join(decipher)
    print(f"\nПолный расшифрованный текст: '{decrypted}'")

