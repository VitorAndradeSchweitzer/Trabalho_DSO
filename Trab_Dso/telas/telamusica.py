import PySimpleGUI as sg
from ..entidades.artista import Artista
from ..entidades.genero import Genero
from ..entidades.idioma import Idioma

class TelaMusica:
    def __init__(self):
        sg.ChangeLookAndFeel('DarkBrown2')

    def mostrar_opcoes(self) -> int:
        layout = [
            [sg.Text("=== Gerenciamento de Músicas ===")],
            [sg.Button("Registrar Nova Música", key=1)],
            [sg.Button("Listar Todas as Músicas", key=2)],
            [sg.Button("Listar por Artista", key=3)],
            [sg.Button("Listar por Gênero", key=4)],
            [sg.Button("Listar por Idioma", key=5)],
            [sg.Button("Atualizar Música", key=6)],
            [sg.Button("Retornar", key=0)]
        ]
        window = sg.Window("Menu de Músicas", layout)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, 0):
                window.close()
                return 0
            if event in range(1, 7):
                window.close()
                return event

    def pegar_dados_musica(self) -> dict:
        layout = [
            [sg.Text("=== Registro de Música ===")],
            [sg.Text("Título:", size=(10, 1)), sg.InputText(key="titulo")],
            [sg.Button("Registrar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Registrar Música", layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return {}
            if event == "Registrar":
                window.close()
                return {"titulo": values["titulo"]}

    def escolher_ou_adicionar(self, lista, tipo_categoria):
        opcoes = [f"{i} - {item.nome}" for i, item in enumerate(lista)]
        layout = [
            [sg.Text(f"Lista de {tipo_categoria}s:")],
            [sg.Listbox(values=opcoes, size=(40, 10), key="opcao")],
            [sg.Text(f"Novo {tipo_categoria}:", size=(15, 1)), sg.InputText(key="novo")],
            [sg.Button("Escolher"), sg.Button("Cancelar")]
        ]
        window = sg.Window(f"Escolher ou Adicionar {tipo_categoria}", layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return None
            if event == "Escolher":
                escolha = values["opcao"]
                if escolha:
                    window.close()
                    return escolha[0].split(" - ")[0]  # Retorna o ID
                elif values["novo"]:
                    window.close()
                    return values["novo"]

    def escolher_ou_adicionar_artista(self, lista):
        return self.escolher_ou_adicionar(lista, "Artista")

    def escolher_ou_adicionar_genero(self, lista):
        return self.escolher_ou_adicionar(lista, "Gênero")

    def escolher_ou_adicionar_idioma(self, lista):
        return self.escolher_ou_adicionar(lista, "Idioma")

    def recebe_id_para_listar(self):
        layout = [
            [sg.Text("Digite o ID desejado:"), sg.InputText(key="id")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Selecionar ID", layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return None
            if event == "Confirmar":
                try:
                    id_escolhido = int(values["id"])
                    window.close()
                    return id_escolhido
                except ValueError:
                    sg.popup("Por favor, insira um número válido")

    def mostrar_musica(self, musica):
        layout = [
            [sg.Text("=== Detalhes da Música ===")],
            [sg.Text(f"Título: {musica.titulo}")],
            [sg.Text(f"Código: {musica.codigo}")],
            [sg.Text(f"Artista: {musica.artista.nome}")],
            [sg.Text(f"Gênero: {musica.genero.nome}")],
            [sg.Text(f"Idioma: {musica.idioma.nome}")],
            [sg.Text(f"Vezes tocadas: {musica.contador}")],
            [sg.Button("Fechar")]
        ]
        window = sg.Window("Detalhes da Música", layout)
        window.read()
        window.close()

    def mostrar_mensagem(self, mensagem: str):
        sg.popup(mensagem)
