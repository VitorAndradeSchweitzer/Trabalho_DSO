from typing import Optional, List

from ..entidades.bibliotecademusicas import BibliotecaDeMusicas
from ..entidades.musica import Musica
from ..entidades.artista import Artista
from ..entidades.genero import Genero
from ..entidades.idioma import Idioma

class ControladorBibliotecaDeMusica:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__bibliotecademusica = BibliotecaDeMusicas()

    @property
    def bibliotecademusica(self):
        return self.__bibliotecademusica
    def retornar_ultimo_codigo(self) -> int:
        return len(self.__bibliotecademusica.musicas) + 1

    def adicionar_musica(self, musica: Musica) -> bool:
        if self.__bibliotecademusica.adicionar_musica(musica) == "musica adicionada":
            return True
        return False

    def buscar_musica(self, codigo: str) -> Musica:
        return self.__bibliotecademusica.buscar_musica_por_codigo(codigo)

    def pegar_musica_por_artista(self, artista: Artista) -> list:
        return self.__bibliotecademusica.pegar_musica_por_artista(artista)

    def pegar_musica_por_genero(self, genero: Genero) -> list:
        return self.__bibliotecademusica.pegar_musica_por_genero(genero)

    def pegar_musica_por_idioma(self, idioma: Idioma) -> list:
        return self.__bibliotecademusica.pegar_musica_por_idioma(idioma)
    
    def lista_musica(self):
        return self.__bibliotecademusica.musicas
        
    def lista_de_artista(self):
        return self.__bibliotecademusica.artistas
    def retornar_artista_por_id(self, id):
        return self.__bibliotecademusica.artistas[id]
    
    def lista_de_genero(self):
        return self.__bibliotecademusica.generos
    def retornar_genero_por_id(self, id):
        return self.__bibliotecademusica.generos[id]
    
    def lista_de_idioma(self):
        return  self.__bibliotecademusica.idiomas
    def retornar_idioma_por_id(self, id):
        return self.__bibliotecademusica.idiomas[id]