
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


class JellyBean(Dessert):
    def __init__(self, name = None, calories = None, flavor = None):
        super().__init__(name, calories)
        self.__flavor = flavor if type(flavor) is str else None

    @property
    def flavor(self):
        return self.__flavor

    @flavor.setter
    def flavor(self, flavor):
        self.__flavor = flavor if type(flavor) is str else None

    def is_delicious(self):
        if self.__flavor is None or self.__flavor.lower() != "black licorice":
            return super().is_delicious()
        return False


if __name__ == "__main__":
    jelly_bean = JellyBean("jelly bean", 166.8)
    print(jelly_bean.is_healthy())                                            # => True
    print(jelly_bean.is_delicious())                                          # => True
    print(jelly_bean.name, jelly_bean.calories, jelly_bean.flavor)            # => jelly bean 166.8 None
    jelly_bean.name = []
    jelly_bean.calories = "apple"
    jelly_bean.flavor = "Black licorice"
    print(jelly_bean.is_healthy())                                            # => None
    print(jelly_bean.is_delicious())                                          # => False
    print(jelly_bean.name, jelly_bean.calories, jelly_bean.flavor)            # => None None Black licorice
    jelly_bean = JellyBean()
    print(jelly_bean.name, jelly_bean.calories, jelly_bean.flavor)            # => None None None
