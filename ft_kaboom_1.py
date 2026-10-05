print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

# Ao tentar importar isso, o loop infinito acontece e o Python corta a execução.
from alchemy.grimoire.dark_spellbook import dark_spell_record