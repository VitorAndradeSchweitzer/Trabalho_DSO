from .atributoscategorias import AtributosCategorias

class Idioma(AtributosCategorias):
    def __init__(self, nome_idioma):
        super().__init__(nome_idioma)


    @property
    def nome_idioma(self):
        return self.__nome_idioma
    
    def __str__(self):
        return f"Idioma: {self.nome}"

