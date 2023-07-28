from ingredient import Ingredient
from sandwich import Sandwich
class Order:
    def __init__(self):
        self.sandwich = None
        self.drink = None
        self.dessert = None

    def start(self):
        self.sandwich = self._create_sandwich()
        self._confirm_sandwich()
        self._add_drink()
        self._add_dessert()
        self._confirm_order()

    def _create_sandwich(self):
        print("Welcome to our sandwich shop!")
        print("Here is a list of our available bread:")
        print("1. Sandwich 15cm: 4.2 € / 198kcal")
        print("2. Sandwich 30cm: 6.2 € / 253kcal")
        bread_choice = input("Please select your bread choice (1-2): ")
        bread = Ingredient("Sandwich 15cm", 4.2, 198) if bread_choice == "1" else Ingredient("Sandwich 30cm", 6.2, 253)
        sandwich = Sandwich(bread, "30cm" if bread_choice == "2" else "15cm")

        print("\nHere is a list of our available ingredients:")
        print("1. Poulet   : 0.2 € / 239kcal")
        print("2. Boeuf    : 0.2 € / 250kcal")
        print("3. Vegan     : 0.3 € / 206kcal")
        print("4. Fromage  : 0.5 € / 402kcal")
        print("5. Salade   : 0.2 € / 16kcal")
        print("6. Tomate   : 0.2 € / 21kcal")
        print("7. Oignons  : 0.3 € / 40kcal")
        print("8. Sauce    : 0.55€ / 40kcal")
        print("Enter 'done' when finished")

        while True:
            ingredient_choice = input("Select an ingredient to add or remove: ")
            if ingredient_choice == "done":
                break
            ingredient = None
            if ingredient_choice == "1":
                ingredient = Ingredient("Poulet", 0.2, 239)
            elif ingredient_choice == "2":
                ingredient = Ingredient("Boeuf", 0.2, 250)
            elif ingredient_choice == "3":
                ingredient = Ingredient("Vegan", 0.3, 206)
            elif ingredient_choice == "4":
                ingredient = Ingredient("Fromage", 0.5, 402)
            elif ingredient_choice == "5":
                ingredient = Ingredient("Salade", 0.2, 16)
            elif ingredient_choice == "6":
                ingredient = Ingredient("Tomate", 0.2, 21)
            elif ingredient_choice == "7":
                ingredient = Ingredient("Oignons", 0.3, 40)
            elif ingredient_choice == "8":
                ingredient = Ingredient("Sauce", 0.55, 40)

            if ingredient is not None:
                action_choice = input("Do you want to add or remove this ingredient? (add/remove): ")
                if action_choice == "add":
                    sandwich.add_ingredient(ingredient)
                elif action_choice == "remove":
                    sandwich.remove_ingredient(ingredient)

        return sandwich

    def _confirm_sandwich(self):
        print("\nHere is your sandwich:")
        print("Bread: {}".format(self.sandwich.bread.name))
        print("Size: {}".format(self.sandwich.size))
        print("Ingredients:")
        for ingredient in self.sandwich.ingredients:
            print("- {} ({} €, {} kcal)".format(ingredient.name, ingredient.price, ingredient.calories))
        print("Total price: {} €".format(self.sandwich.calculate_price()))
        print("Total calories: {} kcal".format(self.sandwich.calculate_calories()))

        while True:
            confirmation = input("Is this sandwich ok? (yes/no): ")
            if confirmation == "yes":
                break
            elif confirmation == "no":
                self.sandwich = self._create_sandwich() 
                self._confirm_sandwich()
                break

    def _add_drink(self):
        print("\nHere is a list of our available drinks:")
        print("1. Water: 1 € / 0kcal")
        print("2. Coke : 1.5 € / 140kcal")
        print("3. Tea  : 1.2 € / 0kcal")
        drink_choice = input("Please select your drink choice (1-3): ")
        drink = Ingredient("Water", 1, 0) if drink_choice == "1" else Ingredient("Coke", 1.5, 140) if drink_choice == "2" else Ingredient("Tea", 1.2, 0)
        self.drink = drink

    def _add_dessert(self):
        print("\nHere is a list of our available desserts:")
        print("1. Chocolate cake: 2.5 € / 520kcal")
        print("2. Fruit salad   : 2.0 € / 210kcal")
        print("3. Ice cream     : 3.0 € / 340kcal")
        dessert_choice = input("Please select your dessert choice (1-3): ")
        dessert = Ingredient("Chocolate cake", 2.5, 520) if dessert_choice == "1" else Ingredient("Fruit salad", 2.0, 210) if dessert_choice == "2" else Ingredient("Ice cream", 3.0, 340)
        self.dessert = dessert

    def _confirm_order(self):
        print("\nHere is your order:")
        print("Sandwich:")
        print("- Bread: {}".format(self.sandwich.bread.name))
        print("- Size: {}".format(self.sandwich.size))
        print("- Ingredients:")
        for ingredient in self.sandwich.ingredients:
            print("- {} ({} €, {} kcal)".format(ingredient.name, ingredient.price, ingredient.calories))
            print("Total price: {} €".format(self.sandwich.calculate_price()))