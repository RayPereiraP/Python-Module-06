# IMPORT RELATIVO: Usamos ".." para voltar uma pasta (sair de transmutation e ir para alchemy) 
# e pegar a função create_air no arquivo elements.py
from ..elements import create_air

# IMPORT ABSOLUTO: Caminho completo desde a raiz (alchemy -> potions)
from alchemy.potions import strength_potion

# IMPORT ABSOLUTO: Pegando o arquivo da raiz do projeto diretamente
import elements

def lead_to_gold() -> str:
    # Retorna exatamente a string pedida no manual, executando as funções
    air = create_air()
    potion = strength_potion()
    fire = elements.create_fire()
    
    return f"Recipe transmuting Lead to Gold: brew '{air}' and '{potion}' mixed with '{fire}'"