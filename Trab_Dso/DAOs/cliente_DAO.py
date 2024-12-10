from ..entidades.cliente import Cliente  
from .dao import DAO 


class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('Clientes.pkl')

    def add(self, cliente: Cliente):
        print("entrou no add")
        if((cliente is not None) and isinstance(cliente, Cliente)):
            print("cliente adicionado")
            super().add(cliente.cpf, cliente)

    def update(self, cliente: Cliente):
        if((cliente is not None) and isinstance(cliente, Cliente) and isinstance(cliente.cpf, int)):
            super().update(cliente.cpf, cliente)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)

