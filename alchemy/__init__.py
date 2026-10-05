from .elements import create_air
from .potions import strength_potion, healing_potion
from . import transmutation
# Adicionamos o grimoire!
from . import grimoire

heal = healing_potion

__all__ = ['create_air', 'strength_potion', 'heal', 'transmutation', 'grimoire']