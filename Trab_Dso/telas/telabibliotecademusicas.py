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
            if evento == sg.WIN_CLOSED or evento == "Fechar":
                break
        janela.close()

    def mostrar_opcoes(self) -> int:
        """
        Exibe o menu de opções e retorna a opção selecionada.
        """
        layout = [
            [sg.Text("=== Relatório de Músicas ===", font=("Fixedsys", 25))],
            [sg.Button("1. Relatório de Artista mais cantado", key=1)],
            [sg.Button("2. Relatório de Gênero mais cantado", key=2)],
            [sg.Button("3. Relatório de Idioma mais cantado", key=3)],
            [sg.Button("0. Retornar", key=0)]
        ]
        
        janela = sg.Window("Opções de Relatórios", layout)

        while True:
            evento, _ = janela.read()
            if evento in (0, 1, 2, 3):  
                janela.close()
                return evento
            elif evento == sg.WIN_CLOSED:
                janela.close()
                return 0  

