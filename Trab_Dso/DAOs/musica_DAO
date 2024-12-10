from ..entidades.musica import Musica
from .dao import DAO

class MusicaDAO(DAO):
    def __init__(self):
        super().__init__('Musicas.pkl')  # Arquivo onde as músicas serão salvas

    def add(self, musica: Musica):
        """
        Adiciona uma nova música ao armazenamento.
        """
        if musica is not None and isinstance(musica, Musica):
            super().add(musica.codigo, musica)  # Usa o código da música como chave

    def update(self, musica: Musica):
        """
        Atualiza uma música existente.
        """
        if musica is not None and isinstance(musica, Musica):
            super().update(musica.codigo, musica)  # Atualiza a música usando o código como chave

    def get(self, codigo: int):
        """
        Recupera uma música pelo código.
        """
        if isinstance(codigo, int):
            return super().get(codigo)

    def remove(self, codigo: int):
        """
        Remove uma música pelo código.
        """
        if isinstance(codigo, int):
            super().remove(codigo)

    def get_all(self):
        """
        Retorna todas as músicas armazenadas.
        """
        return super().get_all()
