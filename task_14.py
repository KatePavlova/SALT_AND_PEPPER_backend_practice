class EvenNumbers:
    def __init__(self, cnt = 0):
        self.__current = 0
        self.__cnt = cnt if type(cnt) is int else 0

    def __iter__(self):
        self.__current = 0
        return self

    def __next__(self):
        if self.__current < self.__cnt:
            value = self.__current * 2
            self.__current += 1
            return value
        else:
            raise StopIteration

if __name__ == "__main__":
    evens = EvenNumbers(5)
    print(next(evens)) # Должно вывести 0
    print(next(evens)) # Должно вывести 2
    for num in evens:
        print(num, end=" ") # Должно вывести 0, 2, 4, 6, 8
    print()

    for num in evens:
        print(num, end=" ") # Должно вывести 0, 2, 4, 6, 8
    print()

    evens = EvenNumbers("tutyu")
    for num in evens:
        print(num, end=" ")  # Ничего не выведет
    print()


