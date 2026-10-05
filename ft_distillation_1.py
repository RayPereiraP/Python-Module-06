import alchemy

print("=== Distillation 1 ===")
print("Using: 'import alchemy' structure to access potions")
# Note que aqui chamamos strength_potion normal
print(f"Testing strength_potion: {alchemy.strength_potion()}")
# Note que aqui usamos o apelido (alias) "heal", graças ao __init__.py!
print(f"Testing heal alias: {alchemy.heal()}")