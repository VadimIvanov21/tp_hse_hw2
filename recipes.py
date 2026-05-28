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