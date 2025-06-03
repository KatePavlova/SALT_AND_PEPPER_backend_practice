
class Dessert:
    def __init__(self, name = None, calories = 0):
        self.__name = name
        self.__calories = calories

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, calories):
        self.__calories = calories

    def is_healthy(self):
        if type(self.__calories) in (int, float) and self.__calories < 200:
            return True
        return False

    def is_delicious(self):
        return True


if __name__ == "__main__":
    dessert = Dessert("meringue", 234.4)
    print(dessert.is_healthy())                        # => False
    print(dessert.is_delicious())                      # => True
    print(dessert.name, dessert.calories)              # => meringue 234.4
    dessert.name = []
    dessert.calories = "apple"
    print(dessert.is_healthy())                        # => False
    print(dessert.is_delicious())                      # => True
    print(dessert.name, dessert.calories)              # => [] apple
    dessert = Dessert()
    print(dessert.name, dessert.calories)              # => None None
