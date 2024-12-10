from ..entidades.filakaraoke import Fila_Karaoke
from ..telas.telafila_karaoke import TelaFila

class ControladorFila:
    #controlador_sistema
    def __init__(self,  controlador_sistema ):
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaFila()
        self.__fila = Fila_Karaoke()

    def abrir_tela(self):
        opcoes = {
            1: self.mostrar_fila,
            2: self.proximo_cantar,
            3: self.adicionar_pedido,
            4: self.remover_pedido,
            0: self.sair
        }

        while True:
            try:
                opcao = self.__tela.tela_opcoes()
                if opcao in opcoes:
                    opcoes[opcao]()
                else:
                    self.__tela.mostra_menssagem("Opcao Invalida")

            except Exception as e:
                self.__tela.mostra_menssagem(f"An error occurred: {str(e)}")

    def inicializa_tela(self):
        self.abrir_tela()
        
    def mostrar_fila(self):
        if not self.__fila.fila_karaoke:
            self.__tela.mostra_menssagem("fila está vazia")
            return
            
        for i, (cliente, musica) in enumerate(self.__fila.fila_karaoke):
            self.__tela.mostrar_fila(i, cliente, musica)

    def proximo_cantar(self):
        proximo = self.__fila.proximo_cantar()
        print("aqui a função proximo a cantar foi chamada")
        if proximo:
            print("entrou no proximo")
            cliente, musica = proximo
            self.__tela.proximo_cantar(cliente, musica)
        else:
            self.__tela.mostra_menssagem("fila está vazia")

    def adicionar_pedido(self):
        try:

            dados_cliente = self.__controlador_sistema.cliente_controlador.lista_cliente()
            dados_cliente = self.__tela.receber_cpf_cliente()
            dados_musica= self.__controlador_sistema.musica_controlador.listar_musica()
            dados_musica= self.__tela.receber_id_musica()
            

            cliente = self.__controlador_sistema.cliente_controlador.buscar_cliente_cpf(dados_cliente)
            musica = self.__controlador_sistema.musica_controlador.controlador_biblioteca.buscar_musica(int(dados_musica))
            
            if cliente and musica:
                self.__fila.adicionar_na_fila(cliente, musica)
                self.__tela.mostra_menssagem("Pedido adicionado")
            else:
                self.__tela.mostra_menssagem("Cliente ou Música não encontrados")
        except Exception as e:
            self.__tela.mostra_menssagem(f"Error adding request: {str(e)}")

    def remover_pedido(self):
        try:
            self.listar_clientes_na_fila()
            cliente = self.__tela.receber_cpf_cliente()
            
            if self.__controlador_sistema.cliente_controlador.buscar_cliente_cpf(cliente) is not None:
                    cliente = self.__controlador_sistema.cliente_controlador.buscar_cliente_cpf(cliente)
                    self.__fila.remover_fila(cliente)
                    self.__tela.mostra_menssagem("Pedido removido")
            else:
                    self.__tela.mostra_menssagem("Cliente não está na fila")

        except Exception as e:
            self.__tela.mostra_menssagem(f"Error removing request: {str(e)}")

    def sair(self):
        self.__controlador_sistema.abrir_tela()

    def listar_clientes_na_fila(self):
        for cliente in self.__fila.fila_karaoke:
            cliente = cliente[0]
            dados_cliente = {"nome": cliente.nome, "telefone": cliente.telefone, "cpf": cliente.cpf, "email": cliente.email}
            self.__controlador_sistema.cliente_controlador.tela.mostrar_cliente(dados_cliente)