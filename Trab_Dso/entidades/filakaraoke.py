from .musica import Musica

class Fila_Karaoke:
    def __init__(self):
        self.__fila_karaoke = []


    @property
    def fila_karaoke(self):
        return self.__fila_karaoke
    
    @fila_karaoke.setter
    def fila_karaoke(self, fila_karaoke: list):
        self.__fila_karaoke.append(fila_karaoke)



    def adicionar_na_fila(self, cliente, musica: Musica):
        inserido = False
        novo_pedido = [cliente, musica]

        if len(self.__fila_karaoke) == 0:
            inserido = True
            self.__fila_karaoke.append(novo_pedido)
        else:
            for i, pedido in enumerate(self.__fila_karaoke):
                if pedido[0].prioridade_fila > cliente.prioridade_fila:
            
                    self.__fila_karaoke.insert(i, novo_pedido)
                    inserido = True
                    break

        if inserido==False:
            self.__fila_karaoke.append(novo_pedido)

        cliente.prioridade_fila -= 1

    def proximo_cantar(self):
        if self.__fila_karaoke:
            cantor = self.__fila_karaoke[0]

            cantor[1].ja_cantada = True
            self.__fila_karaoke.pop(0)
            return cantor

    def ver_posicao(self, cliente):
        for pedidos in self.__fila_karaoke:
            if pedidos[0] == cliente:
                return self.__fila_karaoke.index(pedidos)

    def remover_fila(self, cliente):
        for pedidos in self.__fila_karaoke:
            if pedidos[0] == cliente:
                self.__fila_karaoke.remove(pedidos)
                pedidos[1].incrementar_contador()


    def recomecar_prioridade(self):
        for pedidos in self.__fila_karaoke:
            pedidos[0].prioridade_fila = 0
