from ..entidades.musica import Musica  
from .dao import DAO 


class MusicaDAO(DAO):
    def __init__(self):
        super().__init__('Musicas.pkl')

    def add(self, musica: Musica):
        if((musica is not None) and isinstance(musica, Musica)):
            super().add(musica.codigo, musica)

    def update(self, musica: Musica):
        if((musica is not None) and isinstance(musica, Musica)):
            super().update(musica.codigo, musica)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)
