class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if float(value) <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(value)

    def __str__(self):
        return f"{self.name}: {self._quantity} {self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}', {self._quantity}, '{self.unit}')"

    def __eq__(self, other):
        return self.name == other.name and self.unit == other.unit




class Recipe:
    def __init__(self, title: str, ingredients=None):
        self.title = title
        self.ingredients = ingredients or []

    def add_ingredient(self, ingredient):
        for ing in self.ingredients:
            if ing == ingredient:
                ing.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if (type(ratio) == float or type(ratio) == int) and ratio > 0:
            return True
        else:
            return False

    def scale(self, ratio):
        new_recipe = Recipe(self.title)
        for i in self.ingredients:
            new_recipe.ingredients.append(Ingredient(i.name, i.quantity * ratio, i.unit))
        return new_recipe

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        s = [self.title] + [str(i) for i in self.ingredients]
        return "\n".join(s)


class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled = recipe.scale(portions)
        for ingredient in scaled.ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title: str):
        self._items = [(i, t) for i, t in self._items if t != title]

    def get_list(self):
        totals = {}
        for ingredient, i in self._items:
            key = (ingredient.name, ingredient.unit)
            if key in totals:
                totals[key] += ingredient.quantity
            else:
                totals[key] = ingredient.quantity
        result = [Ingredient(name, qty, unit) for (name, unit), qty in totals.items()]
        result.sort(key=lambda i: i.name)
        return result

    def __add__(self, other):
        new_list = ShoppingList()
        new_list._items = self._items + other._items
        return new_list  


class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients=None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio: float):
        scaled = super().scale(ratio)
        return DietaryRecipe(self.title, self.diet_type, scaled.ingredients)

    def __str__(self):
        return f"[{self.diet_type}] {super().__str__()}"