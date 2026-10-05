def validate_ingredients(ingredients: str) -> str:
    # TÉCNICA DE DEFESA: Importamos DENTRO da função
    from .light_spellbook import light_spell_allowed_ingredients
    
    allowed = light_spell_allowed_ingredients()
    is_valid = any(item.lower() in ingredients.lower() for item in allowed)
    keyword = "VALID" if is_valid else "INVALID"
    
    return f"{ingredients} - {keyword}"