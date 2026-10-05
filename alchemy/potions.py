# Aqui, a poção precisa importar os elementos para ser criada.
# Vamos importar os elementos da raiz e de dentro da pasta alchemy.

# Importa o fogo e a água do arquivo elements.py que está na RAIZ do projeto.
import elements

# Importa a terra e o ar do arquivo elements.py que está DENTRO da pasta alchemy.
# O ponto (.) significa "na mesma pasta que este arquivo está".
from .elements import create_earth, create_air

def healing_potion() -> str:
    # Retorna o texto exato pedido no manual
    return f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"

def strength_potion() -> str:
    # Retorna o texto exato pedido no manual usando os elementos da raiz
    return f"Strength potion brewed with '{elements.create_fire()}' and '{elements.create_water()}'"