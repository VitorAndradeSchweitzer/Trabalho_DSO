from .musica import Musica
from .genero import Genero
from .idioma import Idioma
from .artista import Artista
from ..DAOs.musica_DAO import MusicaDAO
from ..DAOs.idioma_DAO  import IdiomaDAO
from ..DAOs.genero_DAO import GeneroDAO
from ..DAOs.artista_DAO import ArtistaDAO

class BibliotecaDeMusicas:
    def __init__(self):
        self.__musicas = MusicaDAO()
        self.__artistas = ArtistaDAO()
        self.__idiomas = IdiomaDAO()
        self.__generos = GeneroDAO()

    @property
    def musicas(self):
        return self.__musicas
    
    @musicas.setter
    def musicas(self, musicas: Musica):
        self.__musicas.append(musicas)

    @property
    def artistas(self):
        return self.__artistas
    
    @artistas.setter
    def artistas(self, artistas: Artista):
        self.__artistas.append(artistas)

    @property
    def idiomas(self):
        return self.__idiomas
    
    @idiomas.setter
    def idiomas(self, idiomas: Idioma):
        self.__idiomas.append(idiomas)

    @property
    def generos(self):
        return self.__generos
    
    @generos.setter
    def generos(self, genero: Genero):
        self.__generos.append(genero)


        

        
    def buscar_genero(self):
        cont = 0
        generos = list(self.__generos.get_all()) 
        for genero in generos:
            print(f"{genero} [{cont}]")
            cont += 1
        escolha = int(input("Insira o id do gênero escolhido: "))
        if 0 <= escolha < len(generos):
            return generos[escolha]  
        else:
            print("Escolha inválida!")
            return None

    
    def buscar_artista(self):
        cont = 0
        artistas = list(self.__artistas.get_all()) 
        for artista in artistas:
            print(f"{artista} [{cont}]")
            cont += 1
        escolha = int(input("Insira o id do artistas/banda escolhido: "))
        if 0 <= escolha < len(artistas):
            return artistas[escolha] 
        else:
            print("Escolha inválida!")
            return None

    
    def buscar_idioma(self):
        cont = 0
        idiomas = list(self.__idiomas.get_all()) 
        for idioma in idiomas:
            print(f"{idioma} [{cont}]")
            cont += 1
        escolha = int(input("Insira o id do idioma escolhido: "))
        if 0 <= escolha < len(idiomas):
            return idiomas[escolha] 
        else:
            print("Escolha inválida!")
            return None
    


    def adicionar_musica(self, musica: Musica):

        if isinstance(musica, Musica):
            if not self.__musicas.get(musica.codigo):
                self.__musicas.add(musica)
                          
            if  not self.__idiomas.get(musica.idioma.nome):
   
                self.__idiomas.add(musica.idioma)
          
            if not self.__generos.get(musica.genero.nome):
                self.__generos.add(musica.genero)
        
            if not self.__artistas.get(musica.artista.nome):
                self.__artistas.add(musica.artista)
   
            return "musica adicionada"



    def remover_musica(self, musica: Musica):
        if isinstance(musica, Musica):
                self.__musicas.remove(musica)


    def verificar_se_ja_foi_cantada(self, musica):
        if musica.__ja_cantada == True:
            return True
        return False

    def buscar_musica_por_codigo(self,codigo):
        return self.__musicas.get(codigo)
