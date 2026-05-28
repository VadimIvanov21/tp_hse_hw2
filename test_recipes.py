def test_ingredient_init():
    ing = Ingredient("Мука", 500, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit == "г"

def test_ingredient_str():
    assert str(Ingredient("Мука", 500, "г")) == "Мука: 500.0 г"

def test_ingredient_eq_different_quantity():
    assert Ingredient("Мука", 200, "г") == Ingredient("Мука", 67, "г")

def test_ingredient_eq_different_name():
    assert Ingredient("Мука", 200, "г") != Ingredient("Медь", 200, "г")

def test_ingredient_eq_different_unit():
    assert Ingredient("Мука", 200, "мл") != Ingredient("Мука", 200, "г")