class Person:

    def __init__(self, name, age, favoriteFoods):
        self.name = name
        self.age = age
        self.favoriteFoods = favoriteFoods

    def addFavoriteFood(self, item):
        self.favoriteFoods.append("item")

    def removeFavoriteFood(self, item):
        for food in self.favoriteFoods:
            if food == item:
                self.favoriteFoods.remove(item)


p1 = Person('Steve', 19, ['apples'])

print(p1.favoriteFoods)
p1.addFavoriteFood('pizza')
print(p1.favoriteFoods)
p1.removeFavoriteFood('apples')
print(p1.favoriteFoods)