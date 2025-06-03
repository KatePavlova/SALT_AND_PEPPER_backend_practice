
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


class JellyBean(Dessert):
    def __init__(self, name = None, calories = 0, flavor = None):
        super().__init__(name, calories)
        self.__flavor = flavor

    @property
    def flavor(self):
        return self.__flavor

    @flavor.setter
    def flavor(self, flavor):
        self.__flavor = flavor

    def is_delicious(self):
        if type(self.__flavor) is str and self.__flavor.lower() == "black licorice":
            return False
        return super().is_delicious()


if __name__ == "__main__":
    jelly_bean = JellyBean("jelly bean", 166.8)
    print(jelly_bean.is_healthy())                                            # => True
    print(jelly_bean.is_delicious())                                          # => True
    print(jelly_bean.name, jelly_bean.calories, jelly_bean.flavor)            # => jelly bean 166.8 None
    jelly_bean.name = []
    jelly_bean.calories = "apple"
    jelly_bean.flavor = "Black licorice"
    print(jelly_bean.is_healthy())                                            # => False
    print(jelly_bean.is_delicious())                                          # => False
    print(jelly_bean.name, jelly_bean.calories, jelly_bean.flavor)            # => [] apple Black licorice
    jelly_bean = JellyBean()
    print(jelly_bean.name, jelly_bean.calories, jelly_bean.flavor)            # => None 0 None
