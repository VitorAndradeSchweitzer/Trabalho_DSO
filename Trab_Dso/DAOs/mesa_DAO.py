from ..entidades.mesa import Mesa  
from .dao import DAO 


class MesaDAO(DAO):
    def __init__(self):
        super().__init__('Mesas.pkl')

    def add(self, mesa: Mesa):
        if((mesa is not None) and isinstance(mesa, Mesa)):
   
            super().add(mesa.numero, mesa)

    def update(self, mesa: Mesa):
        if((mesa is not None) and isinstance(mesa, Mesa) and isinstance(mesa.numero, int)):
            print("excluiu")
            super().update(mesa.numero, mesa)

    def get(self, key:int):

        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
