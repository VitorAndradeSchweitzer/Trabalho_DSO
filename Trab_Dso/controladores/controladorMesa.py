from ..entidades.mesa import Mesa
from ..telas.telamesa import TelaMesa

class ControladorMesa():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__mesas = []
        self.__tela = TelaMesa()


    def incluir_mesa(self):
        numero = len(self.__mesas)

        novamesa = Mesa(numero = numero+1)
        self.__mesas.append(novamesa)
        self.__tela.mensagem_de_criação(numero+1)

    def excluir_mesa(self):
        self.lista_mesa()
        numero_mesa = self.__tela.seleciona_mesa()
        mesa = self.buscar_mesa_por_numero(numero_mesa)

        if mesa is not None:
            self.__mesas.remove(mesa)
            self.lista_mesa()
            self.__tela.mensagem_de_exclusão(numero_mesa)
        else:
            self.__tela.mostra_mensagem("MESA NÃO EXISTE!!!!!!!")

    def buscar_mesa_por_numero(self, numero):
        for mesa in self.__mesas:
            if int(mesa.numero) == int(numero):
                return mesa
        print(f"Não existe uma mesa com o número {numero}")
        return None
    
    def lista_mesa(self):
        for mesa in self.__mesas:
            clientes = ""
            for cliente in mesa.clientes:
                clientes += cliente.nome
                clientes += ' ,'
            self.__tela.mostrar_mesa({"numero" : mesa.numero, "clientes": clientes})


    def abrir_tela(self):
        listaopcoes = {1: self.incluir_mesa, 2: self.excluir_mesa, 3: self.lista_mesa, 4:self.alocar_cliente, 5: self.desalocar_cliente, 0: self.sair }
        continua = True
        
        while continua:
            listaopcoes[self.__tela.tela_opcoes()]()

    def inicializa_tela(self):
        self.abrir_tela()

    def alocar_cliente(self):
        self.lista_mesa()
        numero_mesa = self.__tela.seleciona_mesa()
        mesa = self.buscar_mesa_por_numero(numero_mesa)

        self.__controlador_sistema.cliente_controlador.lista_cliente()
        cpf = self.__controlador_sistema.cliente_controlador.tela.seleciona_cliente()
        cliente = self.__controlador_sistema.cliente_controlador.buscar_cliente_cpf(cpf)

        mesa.clientes.append(cliente)

    def desalocar_cliente(self):
        for mesa in self.__mesas:
            if len(mesa.clientes) > 0:
                mesa = {"numero": mesa.numero, "clientes":mesa.clientes}
                self.__tela.mostrar_mesa(mesa)
        numero_mesa = self.__tela.seleciona_mesa()
        mesa = self.buscar_mesa_por_numero(numero_mesa)
        for cliente in mesa.clientes:
                dados = {"nome":cliente.nome, "cpf": cliente.cpf, "email":cliente.email, "telefone":cliente.telefone}
                self.__controlador_sistema.cliente_controlador.tela.mostrar_cliente(dados)

        cpf = self.__controlador_sistema.cliente_controlador.tela.seleciona_cliente()
        cliente = self.__controlador_sistema.cliente_controlador.buscar_cliente_cpf(cpf)

        mesa.clientes.remove(cliente)

    def sair(self):
        self.__controlador_sistema.abrir_tela()


