from ..entidades.artista import Artista  
from .dao import DAO 


class ArtistaDAO(DAO):
    def __init__(self):
        super().__init__('Artistas.pkl')

    def add(self, artista: Artista):
    
        if((artista is not None) and isinstance(artista, Artista)):
            super().add(artista.nome, artista)

    def update(self, artista: Artista):
        if((artista is not None) and isinstance(artista, Artista)):
            super().update(artista.nome, artista)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)
