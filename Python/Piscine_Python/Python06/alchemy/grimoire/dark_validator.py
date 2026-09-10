from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    lower_ingredients = ingredients.lower()
    allowed = dark_spell_allowed_ingredients()

    for ingredient in allowed:
        if ingredient in lower_ingredients:
            return ingredients + " - VALID"
    return ingredients + " - INVALID"
