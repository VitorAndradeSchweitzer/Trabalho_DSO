import PySimpleGUI as sg

class TelaMesa():
    def __init__(self):
        sg.ChangeLookAndFeel('DarkBrown2')
    
    def tela_opcoes(self):

        layout = [
             [sg.Text("-------- SISTEMA MESA ----------")],
             [sg.Text("Escolha a opção:")],
             [sg.Button("Incluir mesa", key=1)],
             [sg.Button("Excluir mesa", key=2)],
             [sg.Button("Listar mesa", key=3)],
             [sg.Button("Alocar cliente", key=4)],
             [sg.Button("Remover cliente", key=5)],
             [sg.Text("")],
             [sg.Button("Retornar", key=0)]
        ]

        window = sg.Window("Sistema Mesa", layout)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, 0):
                window.close()
                return 0
            if event in range(1, 6):
                window.close()
                return event        



        # print("-------- MESA ----------")
        # print("Escolha a opcao")
        # print("1 - Incluir mesa")
        # print("2 - Excluir mesa")
        # print("3 - Listar mesa")
        # print("4 - Alocar Cliente")
        # print("5 - Desalocar Cliente")
        # print("0 - Retornar")


        # opcao = int(input("Escolha a opcao: "))
        # while opcao > 5 or opcao < 0:
        #       opcao = int(input("Escolha errada, selecione um valor válido: "))
      
        # return opcao
    

    def mensagem_de_criação(self, numero):
        sg.Popup(f"-----Mesa Numero {numero} criada!")

    def mensagem_de_exclusão(self, numero):
        sg.Popup(f"---Mesa {numero} excluida")
         
    def mostrar_mesa(self,dados_mesa):
        sg.Popup(f"Mesa Numero {dados_mesa['numero']}, Clientes na Mesa: {dados_mesa['clientes']}")

    def seleciona_mesa(self):
        numero = input("Numero da mesa que deseja selecionar: ")
        return numero
    
    def mostra_mensagem(self, msg):
        print(msg)
         
