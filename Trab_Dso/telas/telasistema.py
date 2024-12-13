import PySimpleGUI as sg

class SystemScreen:
    def __init__(self):
        self.__window = None
        

# fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
# precisa chamar self.init_components() aqui para o caso de chamar essa janela uma 2a vez. Não é possível reusar layouts de janelas depois de fechadas.
    # def tela_opcoes(self):
    #     self.init_components()
    #     button, values = self.__window.Read()
    #     opcao = 0
    #     if values['1']:
    #         opcao = 1
    #     if values['2']:
    #         opcao = 2
    #     if values['3']:
    #         opcao = 3
    #     if values['4']:
    #         opcao = 4
    #     if values['5']:
    #         opcao = 5 
    #     # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
    #     if values['0'] or button in (None,'Cancelar'):
    #         opcao = 0
    #     self.close()
    #     return opcao

    # def close(self):
    #     self.__window.close()
    def tela_opcoes(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkBrown2')
        layout = [
            [sg.Text('Bem vindo ao sistema de Karaoke!', font=("Fixedsys",25))],
            [sg.Text('Escolha sua opção', font=("Fixedsys",15))],
            [sg.Button('Controlador Cliente', key=1)],
            [sg.Button('Controlador Musica', key=2)],
            [sg.Button('Controlador Fila', key=3)],
            [sg.Button('Controlador Mesa', key=4)],
            [sg.Button('Relatórios Músicas', key=5)],
            [sg.Text('')],
            [sg.Button('Cancelar', key=0)]
        ]
        self.__window = sg.Window('Sistema Karaoke', layout)

        while True:
            event, _ = self.__window.read()
            if event in (sg.WINDOW_CLOSED, 0):
                self.__window.close()
                return 0

            if event in range(1, 6):
                self.__window.close()
                return event
        
        


# class SystemScreen:
#     def mostrar_opcoes(self) -> int:
#         print("\n=== Karaoke Management System ===")
#         print("1. Controlador Cliente")
#         print("2. Controlador Musica")
#         print("3. Controlador Fila")
#         print("4. Controlador Mesa")
#         print("5. Relatórios Músicas")
#         print("0. Exit")
        
#         while True:
#             try:
#                 option = int(input("Escolha uma opção: "))
#                 if 0 <= option <= 5:
#                     return option
#                 print("Por favor escolha uma opção válida (0-4)")
#             except ValueError:
#                 print("Insira um numero por favor")

    def mostra_menssagem(self, menssagem):
        sg.popup(menssagem)
