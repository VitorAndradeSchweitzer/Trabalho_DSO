from ..entidades.mesa import Mesa
from ..telas.telamesa import TelaMesa
from ..DAOs.mesa_DAO import MesaDAO
class ControladorMesa():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__mesas_DAO = MesaDAO()
        self.__tela = TelaMesa()


    def incluir_mesa(self):
        mesas = self.__mesas_DAO.get_all()
        numeros = []
        numeros = [mesa.numero for mesa in mesas]
        numeros.sort() 

        numero = None
        for i in range(1, len(numeros) + 2):  
            if i not in numeros:
                numero = i
                break

        novamesa = Mesa(numero = numero)
        self.__mesas_DAO.add(novamesa)
        self.__tela.mensagem_de_criação(numero)

    def excluir_mesa(self):
        self.lista_mesa()
        numero_mesa = self.__tela.seleciona_mesa()
        mesa = self.buscar_mesa_por_numero(numero_mesa)

        if mesa is not None:
            self.__mesas_DAO.remove(int(numero_mesa))
            self.lista_mesa()
            self.__tela.mensagem_de_exclusão(numero_mesa)
        else:
            self.__tela.mostra_mensagem("MESA NÃO EXISTE!!!!!!!")

    def buscar_mesa_por_numero(self, numero):
        mesa = self.__mesas_DAO.get(int(numero))
        if mesa:
                return mesa
        return None
    
    def lista_mesa(self):
        for mesa in self.__mesas_DAO.get_all():
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
        cpf = self.__controlador_sistema.cliente_controlador.tela.seleciona_cliente(self.__controlador_sistema.cliente_controlador.clientes_DAO.get_all())
        cliente = self.__controlador_sistema.cliente_controlador.buscar_cliente_cpf(cpf)

        mesa.clientes.append(cliente)
        self.__mesas_DAO.update(mesa)

    def desalocar_cliente(self):
        clientes = ""
        for mesa in self.__mesas_DAO.get_all():
           
            if len(mesa.clientes) > 0:
                for cliente in mesa.clientes:
                    clientes += cliente.nome
                    clientes += ' ,'
                mesa = {"numero": mesa.numero, "clientes":clientes}
                self.__tela.mostrar_mesa(mesa)
        numero_mesa = self.__tela.seleciona_mesa()
        mesa = self.buscar_mesa_por_numero(numero_mesa)
        
        for cliente in mesa.clientes:
                dados = {"nome":cliente.nome, "cpf": cliente.cpf, "email":cliente.email, "telefone":cliente.telefone}
                self.__controlador_sistema.cliente_controlador.tela.mostrar_cliente(self.__controlador_sistema.cliente_controlador.clientes_DAO.get_all())

        cpf = self.__controlador_sistema.cliente_controlador.tela.seleciona_cliente(self.__controlador_sistema.cliente_controlador.clientes_DAO.get_all())
    
 
        cliente = self.__controlador_sistema.cliente_controlador.buscar_cliente_cpf(cpf)
    
        for alocado in mesa.clientes:
            if alocado.cpf == cliente.cpf:
                mesa.clientes.remove(alocado)
  
        self.__mesas_DAO.update(mesa)
           


    def sair(self):
        self.__controlador_sistema.abrir_tela()


