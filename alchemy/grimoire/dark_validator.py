# O validador importa o livro no topo do arquivo (CRIANDO O LOOP!)
from .dark_spellbook import dark_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    
    # Checa se algum ingrediente permitido está na string
    is_valid = any(item.lower() in ingredients.lower() for item in allowed)
    keyword = "VALID" if is_valid else "INVALID"
    
    return f"{ingredients} - {keyword}"