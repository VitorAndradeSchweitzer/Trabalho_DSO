from ..entidades.cliente import Cliente  
from .dao import DAO 


class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('Clientes.pkl')

    def add(self, cliente: Cliente):
        print("entrou no add")
        if((cliente is not None) and isinstance(cliente, Cliente)):
       
            super().add(cliente.cpf, cliente)

    def update(self, cliente: Cliente):
        if((cliente is not None) and isinstance(cliente, Cliente)):
            super().update(cliente.cpf, cliente)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)
