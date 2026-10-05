# O livro importa o validador no topo do arquivo
from .dark_validator import validate_ingredients

def dark_spell_allowed_ingredients() -> list[str]:
    # Ingredientes proibidos conforme o manual
    return ["bats", "frogs", "arsenic", "eyeball"]

def dark_spell_record(spell_name: str, ingredients: str) -> str:
    status = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({status})"