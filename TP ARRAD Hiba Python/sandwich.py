class Sandwich:
    def __init__(self, bread, size):
        self.bread = bread
        self.size = size
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        self.ingredients.remove(ingredient)

    def calculate_price(self):
        price = self.bread.price * (2 if self.size == "30cm" else 1)
        for ingredient in self.ingredients:
            price += ingredient.price
        return price

    def calculate_calories(self):
        calories = self.bread.calories * (2 if self.size == "30cm" else 1)
        for ingredient in self.ingredients:
            calories += ingredient.calories
        return calories
