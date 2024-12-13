import PySimpleGUI as sg

class TelaBibliotecaDeMusica:
    def __init__(self):
        sg.theme("DarkBrown2")

    def mostrar_mensagem(self, mensagem: str):
        sg.popup(mensagem, title="Mensagem")

    def mostrar_lista_musicas(self, lista_musicas: list):
        if not lista_musicas:
            self.mostrar_mensagem("Nenhuma música disponível.")
            return

        texto_musicas = "\n=== Biblioteca de Músicas ===\n\n"
        for musica in lista_musicas:
            texto_musicas += (
                f"Título: {musica.titulo}\n"
                f"Artista: {musica.artista}\n"
                f"Gênero: {musica.genero}\n"
                f"Idioma: {musica.idioma}\n"
                f"Código: {musica.codigo}\n"
                f"Vezes Tocada: {musica.contador}\n\n"
            )

        layout = [[sg.Text("Biblioteca de Músicas", font=("Fixedsys", 25))],
                  [sg.Multiline(default_text=texto_musicas, size=(60, 20), disabled=True)],
                  [sg.Button("Fechar")]]
        
        janela = sg.Window("Biblioteca de Músicas", layout)
        while True:
            evento, _ = janela.read()
            if evento in (sg.WIN_CLOSED, "Fechar"):
                break
        janela.close()

    def mostrar_opcoes(self) -> int:
        layout = [
            [sg.Text("=== Relatório de Músicas ===", font=("Fixedsys", 25))],
            [sg.Button("1. Relatório de Artista mais cantado", key=1)],
            [sg.Button("2. Relatório de Gênero mais cantado", key=2)],
            [sg.Button("3. Relatório de Idioma mais cantado", key=3)],
            [sg.Button("4. Relatório de Músicas mais cantadas", key=4)],
            [sg.Button("0. Retornar", key=0)]
        ]

        janela = sg.Window("Opções de Relatórios", layout)

        while True:
            evento, _ = janela.read()
            if evento in (0, 1, 2, 3, 4):
                janela.close()
                return evento
            elif evento == sg.WIN_CLOSED:
                janela.close()
                return 0

    def mostrar_relatorio_musicas(self, musicas_ordenadas):
        texto = "=== Relatório de Músicas Mais Cantadas ===\n\n"
        for musica in musicas_ordenadas:
            texto += f"{musica.titulo} - {musica.artista} ({musica.contador} vezes)\n"

        sg.popup_scrolled(texto, title="Relatório de Músicas")

    def mostrar_relatorio_artistas(self, artistas_ordenados):
        texto = "=== Relatório de Artistas Mais Cantados ===\n\n"
        for artista in artistas_ordenados:
            texto += f"{artista.nome} ({artista.contador} vezes)\n"

        sg.popup_scrolled(texto, title="Relatório de Artistas")

    def mostrar_relatorio_generos(self, generos_ordenados):
        texto = "=== Relatório de Gêneros Mais Cantados ===\n\n"
        for genero in generos_ordenados:
            texto += f"{genero.nome} ({genero.contador} vezes)\n"

        sg.popup_scrolled(texto, title="Relatório de Gêneros")

    def mostrar_relatorio_idiomas(self, idiomas_ordenados):
        texto = "=== Relatório de Idiomas Mais Cantados ===\n\n"
        for idioma in idiomas_ordenados:
            texto += f"{idioma.nome} ({idioma.contador} vezes)\n"

        sg.popup_scrolled(texto, title="Relatório de Idiomas")
