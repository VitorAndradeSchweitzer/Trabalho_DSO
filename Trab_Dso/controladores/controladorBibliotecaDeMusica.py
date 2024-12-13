from typing import Optional, List

from ..telas.telabibliotecademusicas import TelaBibliotecaDeMusica
from ..entidades.bibliotecademusicas import BibliotecaDeMusicas
from ..entidades.musica import Musica
from ..entidades.artista import Artista
from ..entidades.genero import Genero
from ..entidades.idioma import Idioma

class ControladorBibliotecaDeMusica:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaBibliotecaDeMusica()
        self.__bibliotecademusica = BibliotecaDeMusicas()

    @property
    def bibliotecademusica(self):
        return self.__bibliotecademusica
    
    def retornar_ultimo_codigo(self) -> int:
        
        return len(self.__bibliotecademusica.musicas.get_all()) + 1

    def adicionar_musica(self, musica: Musica) -> bool:
        if self.__bibliotecademusica.adicionar_musica(musica) == "musica adicionada":
            return True
        return False

    def buscar_musica(self, codigo: int) -> Musica:
        return self.__bibliotecademusica.buscar_musica_por_codigo(codigo)
    
    def lista_musica(self):
        return self.__bibliotecademusica.musicas.get_all()
        
    def lista_de_artista(self):
        return self.__bibliotecademusica.artistas.get_all()
    def retornar_artista_por_id(self, id):
        cont = 0
        for artista in self.__bibliotecademusica.artistas.get_all():
            if cont == id:
                return artista
            cont+=1
            
    
    def lista_de_genero(self):
        return self.__bibliotecademusica.generos.get_all()
    def retornar_genero_por_id(self, id):
        cont = 0
        for genero in self.__bibliotecademusica.generos.get_all():
            if cont == id:
                return genero
            cont+=1
    
    def lista_de_idioma(self):
        return  self.__bibliotecademusica.idiomas.get_all()
    def retornar_idioma_por_id(self, id):
        cont = 0
        for idioma in self.__bibliotecademusica.idiomas.get_all():
            if cont == id:
                return idioma
            cont+=1

    @property
    def tela(self):
        return self.__tela
    
    def abrir_tela(self):
        opcoes = {
            1: self.relatorio_artistas,
            2: self.relatorio_generos,
            3: self.relatorio_idiomas,
            0: self.sair
        }

        while True:
            try:
                opcao = self.__tela.mostrar_opcoes()
                if opcao in opcoes:
                    opcoes[opcao]()
                else:
                    self.__tela.mostrar_mensagem("Opção Inválida")
            except ValueError:
                self.__tela.mostrar_mensagem("Por favor, insira um número válido")
            except Exception as e:
                self.__tela.mostrar_mensagem(f"Um erro ocorreu: {str(e)}")

    
    def relatorio_artistas(self):
        artistas_ordenados = sorted(self.lista_de_artista(), key=lambda artista: artista.contador, reverse=True)
        print("Relatório de Artistas (Mais Cantados para Menos Cantados):")
        for artista in artistas_ordenados:
            print(f'{artista}: {artista.contador}')


    def relatorio_generos(self):
        generos_ordenados = sorted(self.lista_de_genero(), key=lambda genero: genero.contador, reverse=True)
        print("Relatório de Gêneros (Mais Cantados para Menos Cantados):")
        for genero in generos_ordenados:
            print(f'{genero}: {genero.contador}')

    def relatorio_idiomas(self):
        idiomas_ordenados = sorted(self.lista_de_idioma(), key=lambda idioma: idioma.contador, reverse=True)
        print("Relatório de Idiomas (Mais Cantados para Menos Cantados):")
        for idioma in idiomas_ordenados:
            print(f'{idioma}: {idioma.contador}')

    def sair(self):
        self.__controlador_sistema.abrir_tela()
