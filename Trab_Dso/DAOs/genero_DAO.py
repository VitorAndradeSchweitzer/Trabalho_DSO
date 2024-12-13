from ..entidades.genero import Genero  
from .dao import DAO 


class GeneroDAO(DAO):
    def __init__(self):
        super().__init__('Generos.pkl')

    def add(self, genero: Genero):
    
        if((genero is not None) and isinstance(genero, Genero)):
            super().add(genero.nome, genero)

    def update(self, genero: Genero):
        if((genero is not None) and isinstance(genero, Genero)):
            super().update(genero.nome, genero)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)
