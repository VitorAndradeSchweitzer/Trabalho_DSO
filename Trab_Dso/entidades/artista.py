from .atributoscategorias import AtributosCategorias

class Artista(AtributosCategorias):
    def __init__(self, nome_artista):
        super().__init__(nome_artista)

    def __str__(self):
        return f"Artista: {self.nome}"
