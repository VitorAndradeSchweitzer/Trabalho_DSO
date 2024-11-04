from .atributoscategorias import AtributosCategorias

class Genero(AtributosCategorias):
    def __init__(self, nome_genero):
        super().__init__(nome_genero)

    @property
    def nome_genero(self):
        return self.__nome_genero
    
    def __str__(self):
        return f"Gênero: {self.nome}"
