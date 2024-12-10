from typing import Optional, List
from ..telas.telamusica import TelaMusica
from ..entidades.musica import Musica
from ..entidades.artista import Artista
from ..entidades.genero import Genero
from ..entidades.idioma import Idioma


class ControladorMusica:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaMusica()
        self.__controlador_biblioteca = self.__controlador_sistema.bibliotecademusicas_controlador

    @property
    def tela(self):
        return self.__tela
    @property
    def controlador_biblioteca(self):
        return self.__controlador_biblioteca
    def abrir_tela(self):
        opcoes = {
            1: self.registrar_musica,
            2: self.listar_musica,
            3: self.listar_artistas,
            4: self.listar_generos,
            5: self.listar_idiomas,
            6: self.atualizar_musica,
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

    def registrar_musica(self):

        try:
            codigo = self.__controlador_biblioteca.retornar_ultimo_codigo()
            dados_musica = self.__tela.pegar_dados_musica() #ID É O SISTEMA QUE DEFINE
            
            #FAZER FUNÇÃO INTERMEDIARIA PAR MOSTRAR CATEGORIAS JÁ CADASTRADAS E DAR OPCAO DE CRiAR NOVO
            
            opcoes_de_artista = self.__controlador_biblioteca.lista_de_artista()
            opcoes = self.__tela.escolher_ou_adicionar_artista(opcoes_de_artista)
            if opcoes.isdigit():
                artista = self.__controlador_biblioteca.retornar_artista_por_id(int(opcoes))
                dados_musica["artista"] = artista
            else:
                print(f"opcoes é {opcoes}")
                achado = False
                print("novo artista é false")
                for artista in self.__controlador_biblioteca.bibliotecademusica.artistas:
                    print("entrou no loop")
                    if artista.nome == opcoes:
                        novo_artista = artista
                        achado = True
                if achado == False:
                        print("achado entrou aqui")
                        novo_artista = Artista(opcoes)
                dados_musica["artista"] = novo_artista
            

            opcoes_genero = self.__controlador_biblioteca.lista_de_genero()
            opcoes = self.__tela.escolher_ou_adicionar_genero(opcoes_genero)
            if opcoes.isdigit():
                genero = self.__controlador_biblioteca.retornar_genero_por_id(int(opcoes))
                dados_musica["genero"] = genero
            else:
                achado = False

                for genero in self.__controlador_biblioteca.bibliotecademusica.generos:
                    if genero.nome == opcoes:
                        novo_genero = genero
                        achado = True
                if achado == False:
                        novo_genero = Genero(opcoes)
                dados_musica["genero"] = novo_genero

            
            opcoes_idioma = self.__controlador_biblioteca.lista_de_idioma()
            opcoes = self.__tela.escolher_ou_adicionar_idioma(opcoes_idioma)
            if opcoes.isdigit():
                idioma = self.__controlador_biblioteca.retornar_idioma_por_id(int(opcoes))
                dados_musica["idioma"] = idioma
            else:
                achado = False
                for idioma in self.__controlador_biblioteca.bibliotecademusica.idiomas:
                    if idioma.nome == opcoes:
                        novo_idioma = idioma
                        achado = True
                if achado == False:
                        novo_idioma = Idioma(opcoes)
                dados_musica["idioma"] = novo_idioma


            nova_musica = Musica(
                codigo,
                dados_musica["titulo"], 
                dados_musica["artista"],
                dados_musica["genero"],
                dados_musica["idioma"]
            )
            if self.__controlador_biblioteca.adicionar_musica(nova_musica):
                self.__tela.mostrar_mensagem("Música registrada com sucesso")
            else:
                self.__tela.mostrar_mensagem("Música já existe")
        except Exception as e:
            self.__tela.mostrar_mensagem(f"Erro registrando música: {str(e)}")

    def buscar_musica(self, codigo: str) -> Musica:
        return self.__controlador_biblioteca.buscar_musica(codigo)

    def listar_musica(self):
        lista_musica = self.__controlador_biblioteca.lista_musica()
        if not lista_musica:
            self.__tela.mostrar_mensagem("Sem Músicas registrada")
            return
        
        for musica in lista_musica:
            self.__tela.mostrar_musica(musica)

    def __mostrar_musica_por_filtro(self, lista_musica):
        if not lista_musica:
            self.__tela.mostrar_mensagem("Música não encontrada")
            return
        
        for musica in lista_musica:
            self.__tela.mostrar_musica(musica)


    def listar_artistas(self):
        resultados = self.__controlador_biblioteca.lista_de_artista()
        cont = 0
        for resultado in resultados:
            
            self.__tela.mostrar_mensagem(f"{cont} - {resultado}")
            cont +=1
        id_escolhido = self.__tela.recebe_id_para_listar()
        lista_musicas = self.__controlador_biblioteca.lista_musica()
        for musica in lista_musicas:
            if musica.artista == resultados[id_escolhido]:
                self.__tela.mostrar_musica(musica)
            

    def listar_generos(self):
        resultados = self.__controlador_biblioteca.lista_de_genero()
        cont = 0
        for resultado in resultados:

            self.__tela.mostrar_mensagem(f"{cont} - {resultado}")
            cont += 1
        id_escolhido = self.__tela.recebe_id_para_listar()
        lista_musicas = self.__controlador_biblioteca.lista_musica()
        for musica in lista_musicas:
            if musica.genero == resultados[id_escolhido]:
                self.__tela.mostrar_musica(musica)

    def listar_idiomas(self):
        resultados = self.__controlador_biblioteca.lista_de_idioma()
        cont=0
        for resultado in resultados:
            self.__tela.mostrar_mensagem(f"{cont} - {resultado}")
            cont += 1
        id_escolhido = self.__tela.recebe_id_para_listar()
        lista_musicas = self.__controlador_biblioteca.lista_musica()
        for musica in lista_musicas:
            if musica.idioma == resultados[id_escolhido]:
                self.__tela.mostrar_musica(musica)

    def atualizar_musica(self):
        self.listar_musica()
        codigo_escolhido = self.__tela.recebe_id_para_listar()
        musica = self.buscar_musica(codigo_escolhido)
        if isinstance(musica, Musica):
            dados_musica = self.__tela.pegar_dados_musica()
            opcoes_de_artista = self.__controlador_biblioteca.lista_de_artista()
            opcoes = self.__tela.escolher_ou_adicionar_artista(opcoes_de_artista)
            if opcoes.isdigit():
                artista = self.__controlador_biblioteca.retornar_artista_por_id(int(opcoes))
                dados_musica["artista"] = artista
            else:
                novo_artista = Artista(opcoes)
                dados_musica["artista"] = novo_artista
            
            opcoes_genero = self.__controlador_biblioteca.lista_de_genero()
            opcoes = self.__tela.escolher_ou_adicionar_genero(opcoes_genero)
            if opcoes.isdigit():
                genero = self.__controlador_biblioteca.retornar_genero_por_id(int(opcoes))
                dados_musica["genero"] = genero
            else:
                novo_genero = Genero(opcoes)
                dados_musica["genero"] = novo_genero

            opcoes_idioma = self.__controlador_biblioteca.lista_de_idioma()
            opcoes = self.__tela.escolher_ou_adicionar_idioma(opcoes_idioma)
            if opcoes.isdigit():
                idioma = self.__controlador_biblioteca.retornar_idioma_por_id(int(opcoes))
                dados_musica["idioma"] = idioma
            else:
                novo_idioma = Idioma(opcoes)
                dados_musica["idioma"] = novo_idioma


            musica.titulo = dados_musica["titulo"]
            musica.artista = dados_musica["artista"]
            musica.genero = dados_musica["genero"]
            musica.idioma = dados_musica["idioma"]

            self.__tela.mostrar_mensagem("Tudo certo, música atualziada!")
        else:
            self.__tela.mostrar_mensagem("Nenhuma musica possui esse id")




    def sair(self):
        self.__controlador_sistema.abrir_tela()
