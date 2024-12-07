import sys
from ..controladores import controladorCliente, controladorFila, controladorMesa, controladorMusica, controladorBibliotecaDeMusica 
from ..telas import telasistema

class ControladorSistema:
    def __init__(self):
        self.__bibliotecademusicas = controladorBibliotecaDeMusica.ControladorBibliotecaDeMusica(self)
        self.__cliente_controlador = controladorCliente.ControladorCliente(self)
        self.__musica_controlador = controladorMusica.ControladorMusica(self)
        self.__fila_controlador = controladorFila.ControladorFila(self)
        self.__mesa_controlador = controladorMesa.ControladorMesa(self)
        self.__tela = telasistema.SystemScreen()


    @property
    def bibliotecademusicas_controlador(self):
        return self.__bibliotecademusicas

    def iniciar(self):
        self.abrir_tela()

    def abrir_tela(self):
        opcoes = {
            1: self.__cliente_controlador.abrir_tela,
            2: self.__musica_controlador.abrir_tela,
            3: self.__fila_controlador.abrir_tela,
            4: self.__mesa_controlador.abrir_tela,
            5: self.__bibliotecademusicas.abrir_tela,
            0: self.close
        }

        while True:
            try:
                opcao = self.__tela.tela_opcoes()
                if opcao == 0:
                    self.close()
                    break
                if opcao in opcoes:
                    opcoes[opcao]()
                else:
                    self.__tela.mostra_menssagem("Opção invalida")
            except ValueError:
                self.__tela.mostra_menssagem("Por favor coloque um valor valido")

    @property
    def cliente_controlador(self):
        return self.__cliente_controlador
    
    @property
    def musica_controlador(self):
        return self.__musica_controlador


    def close(self):
        self.__tela.mostra_menssagem("Fechando ...")
        sys.exit() 

    
