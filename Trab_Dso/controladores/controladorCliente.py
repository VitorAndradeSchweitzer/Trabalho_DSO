from ..entidades.cliente import Cliente
from ..telas.telacliente import TelaCliente
import re
from ..DAOs.cliente_DAO import ClienteDAO


class ControladorCliente():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__clientes_DAO = ClienteDAO()
        self.__tela = TelaCliente()

    @property
    def clientes_DAO(self):
        return self.__clientes_DAO

    @property
    def tela(self):
        return self.__tela
    
    def incluir_cliente(self):
        dados_cliente = self.__tela.receber_dados()
        try:
            self.validar_cpf(dados_cliente["cpf"])
            self.validar_email(dados_cliente["email"])
            self.validar_telefone(dados_cliente["telefone"])
            
            NovoCliente = Cliente(dados_cliente["nome"], dados_cliente["cpf"], dados_cliente["email"], dados_cliente["telefone"])
            self.__clientes_DAO.add(NovoCliente)
        
        except ValueError as e:
            self.__tela.mostra_mensagem(f"Erro ao incluir cliente: {e}")

    def alterar_cliente(self):
        if self.__clientes_DAO.get_all() == []:
            self.__tela.mostra_mensagem("Nenhum cliente cadastrado")
            self.abrir_tela()
        cpf_selecionado = self.__tela.seleciona_cliente(self.__clientes_DAO.get_all())
        cliente = self.buscar_cliente_cpf(cpf_selecionado)

        if cliente is not None:
            novos_dados_cliente = self.__tela.receber_dados()

            try:
                self.validar_cpf(novos_dados_cliente["cpf"])
                self.validar_email(novos_dados_cliente["email"])
                self.validar_telefone(novos_dados_cliente["telefone"])
                
                cliente.nome = novos_dados_cliente["nome"]
                cliente.cpf = novos_dados_cliente["cpf"]
                cliente.email = novos_dados_cliente["email"]
                cliente.telefone = novos_dados_cliente["telefone"]
                self.__clientes_DAO.update(cliente)


            except ValueError as e:
                self.__tela.mostra_mensagem(f"Erro ao alterar cliente: {e}")

        else:
            self.__tela.mostra_mensagem("CLIENTE INFORMADO NÃO CADASTRADO!!!!!!!")

    def excluir_cliente(self):

        cpf_cliente = self.__tela.seleciona_cliente(self.__clientes_DAO.get_all())
 
        cliente = self.buscar_cliente_cpf(cpf_cliente)
    
        if cliente is not None:
            self.__clientes_DAO.remove(cpf_cliente)
            self.lista_cliente()
        else:
            self.__tela.mostra_mensagem("CLIENTE INFORMADO NÃO CADASTRADO!!!!!!!")

    def buscar_cliente_cpf(self, cpf: int):
        
        for cliente in self.__clientes_DAO.get_all():
            if cliente.cpf == cpf:
                return cliente
        return None


    def lista_cliente(self):
            self.__tela.mostrar_cliente(self.__clientes_DAO.get_all())

    def abrir_tela(self):
        listaopcoes = {1: self.incluir_cliente, 2: self.alterar_cliente, 3: self.lista_cliente, 4:self.excluir_cliente, 0: self.sair }
        continua = True
        
        while continua:
            listaopcoes[self.__tela.tela_opcoes()]()

    def inicializa_tela(self):
        self.abrir_tela()

    def sair(self):
        self.__controlador_sistema.abrir_tela()
        
    def validar_cpf(self, cpf):
        if not cpf.isdigit() or len(cpf) != 11:
            raise ValueError("CPF inválido. O CPF deve conter exatamente 11 dígitos numéricos (ex.: 12345678910).")

    def validar_email(self, email):
        regex_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(regex_email, email):
            raise ValueError("E-mail inválido. Por favor, insira um e-mail válido (ex.: nome@exemplo.com).")

    def validar_telefone(self, telefone):
        if not telefone.isdigit() or len(telefone) < 10:
            raise ValueError("Telefone inválido. O telefone deve conter apenas números e ter pelo menos 10 dígitos (ex.: 4899991234).")
