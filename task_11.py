
class Dessert:
    def __init__(self, name = None, calories = None):
        self.__name = name if type(name) is str else None
        self.__calories = calories if type(calories) in (int, float) and calories >= 0 else None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name if type(name) is str else None

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, calories):
        self.__calories = calories if type(calories) in (int, float) and calories >= 0 else None

    def is_healthy(self):
        if self.__calories is None:
            return None
        return self.__calories < 200

    def is_delicious(self):
        return True


if __name__ == "__main__":
    dessert = Dessert("meringue", 234.4)
    print(dessert.is_healthy())                        # => False
    print(dessert.is_delicious())                      # => True
    print(dessert.name, dessert.calories)              # => meringue 234.4
    dessert.name = []
    dessert.calories = "apple"
    print(dessert.is_healthy())                        # => None
    print(dessert.is_delicious())                      # => True
    print(dessert.name, dessert.calories)              # => None None
    dessert = Dessert()
    print(dessert.name, dessert.calories)              # => None None