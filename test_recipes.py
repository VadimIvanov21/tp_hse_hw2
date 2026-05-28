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



def test_recipe_init():
    r = Recipe("Кекс", [])
    assert r.title == "Кекс"
    assert r.ingredients == []

def test_recipe_add_ingredient():
    r = Recipe("Кекс", [])
    r.add_ingredient(Ingredient("Мука", 200, "г"))
    assert len(r) == 1

def test_recipe_add_duplicate():
    r = Recipe("Кекс", [])
    r.add_ingredient(Ingredient("Мука", 200, "г"))
    r.add_ingredient(Ingredient("Мука", 67, "г"))
    assert len(r) == 1
    assert r.ingredients[0].quantity == 267.0

def test_recipe_scale():
    r = Recipe("Кекс", [Ingredient("Мука", 200, "г")])
    scaled = r.scale(3)
    assert scaled is not r
    assert scaled.ingredients[0].quantity == 600.0

def test_recipe_scale_error():
    with pytest.raises(ValueError):
        Recipe("Кекс", []).scale(-1)

def test_recipe_len():
    r = Recipe("Кекс", [Ingredient("Мука", 200, "г"), Ingredient("Куриная Грудка", 52, "г")])
    assert len(r) == 2