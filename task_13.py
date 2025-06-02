from collections import deque
import time


def cached(max_size = None, seconds = None):
    if type(max_size) is not int or max_size < 0:
        max_size = None
    if type(seconds) is not int or seconds < 0:
        seconds = None

    def cache_args(func):

        check = object()
        cache = {}
        time_ = deque()

        def make_key(args, kwargs):
            key = args
            if kwargs:
                for item in sorted(kwargs.items()):
                    key += item
            return str(key)

        def del_old_key():
            old_key = time_[0][1]
            del cache[old_key]
            time_.popleft()

        if max_size == 0 or seconds == 0:
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                return result

        elif max_size is None and seconds is None:
            def wrapper(*args, **kwargs):
                key = make_key(args, kwargs)
                result = cache.get(key, check)
                if result is not check:
                    return result
                else:
                    result = func(*args, **kwargs)
                    cache[key] = result
                    return result

        else:
            def wrapper(*args, **kwargs):
                key = make_key(args, kwargs)

                if seconds is not None:
                    while(time_ and int(time.time() - time_[0][0]) > seconds):
                        del_old_key()

                result = cache.get(key, check)
                if result is not check:
                    return result
                else:
                    if len(time_) == max_size:
                        del_old_key()
                    result = func(*args, **kwargs)
                    if seconds is not None:
                        time_.append((time.time(), key))
                    cache[key] = result
                    return result
        return wrapper
    return cache_args

if __name__ == "__main__":


    @cached(max_size=3, seconds=10)
    def slow_function(x):
        print(f"Вычисляю для {x}...")
        return x ** 2

    print("Тест 1")
    # Первый вызов — вычисляется
    print(slow_function(2)) # Вывод: "Вычисляю для 2..." → 4
    # Повторный вызов с теми же аргументами — берётся из кэша
    print(slow_function(2)) # Вывод: 4 (без вычисления)
    # Через 15 секунд кэш устареет, и будет новое вычисление
    time.sleep(15)
    print(slow_function(2)) # Вывод: "Вычисляю для 2..." → 4
    print(slow_function(3)) # Вывод: "Вычисляю для 3..." → 9
    print(slow_function(4)) # Вывод: "Вычисляю для 4..." → 16
    # Кэш достиг максимального размера, для новых записей будут удалены самые старые
    print(slow_function(5)) # Вывод: "Вычисляю для 5..." → 25
    # Повторный вызов, но для этого аргументы запись была удалена
    print(slow_function(2))  # Вывод: "Вычисляю для 2..." → 4


    @cached(max_size=0, seconds=10)
    def slow_function_2(x, y=None):
        print(f"Вычисляю для {x}...")
        return x ** 2

    print()
    print("Тест 2")
    # Кэш нулевого размера, не храним данные
    print(slow_function_2(2, {"a":8, "b":10}))  # Вывод: "Вычисляю для 2..." → 4
    print(slow_function_2(2, {"a": 8, "b": 10}))  # Вывод: "Вычисляю для 2..." → 4


    @cached(max_size={5, 6, 2}, seconds="")
    def slow_function_3(x, y=None):
        print(f"Вычисляю для {x}...")
        return x ** 2


    print()
    print("Тест 3")
    #Храним вызовы в кэше, записи не удалаяются
    print(slow_function_3(5))  # Вывод: "Вычисляю для 5..." → 25
    print(slow_function_3(5))  # Вывод: 25 (без вычисления)