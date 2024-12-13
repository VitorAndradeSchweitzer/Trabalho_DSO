from ..entidades.idioma import Idioma  
from .dao import DAO 


class IdiomaDAO(DAO):
    def __init__(self):
        super().__init__('Idiomas.pkl')

    def add(self, idioma: Idioma):
    
        if((idioma is not None) and isinstance(idioma, Idioma)):
            super().add(idioma.nome, idioma)

    def update(self, idioma: Idioma):
        if((idioma is not None) and isinstance(idioma, Idioma)):
            super().update(idioma.nome, idioma)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)
