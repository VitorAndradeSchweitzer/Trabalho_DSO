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

    def mensagem_de_criação(self, numero):
        sg.Popup(f"-----Mesa Numero {numero} criada!")

    def mensagem_de_exclusão(self, numero):
        sg.Popup(f"---Mesa {numero} excluida")
         
    def mostrar_mesa(self, dados_mesa):
        """Exibe os dados de uma mesa específica."""
        layout = [
            [sg.Text(f"Mesa Número: {dados_mesa['numero']}", font=("Fixedsys", 14))],
            [sg.Text(f"Clientes na Mesa: {', '.join(dados_mesa['clientes']) if dados_mesa['clientes'] else 'Nenhum'}")],
            [sg.Button("OK")]
        ]
        window = sg.Window("Detalhes da Mesa", layout)
        window.read()
        window.close()

    def seleciona_mesa(self):
            """Permite ao usuário selecionar uma mesa pelo número."""
            layout = [
                [sg.Text("Digite o número da mesa:", font=("Fixedsys", 12))],
                [sg.InputText(key='numero')],
                [sg.Button("Confirmar"), sg.Button("Cancelar")]
            ]

            window = sg.Window("Selecionar Mesa", layout)
            while True:
                event, values = window.read()
                if event in (sg.WINDOW_CLOSED, "Cancelar"):
                    window.close()
                    return None  # Retorna None se cancelar
                if values['numero'].isdigit():
                    numero = int(values['numero'])
                    window.close()
                    return numero
                else:
                    sg.popup_error("Por favor, insira um número válido.")

    def mostra_mensagem(self, msg):
        """Exibe mensagens gerais na interface gráfica."""
        sg.popup_ok(msg, title="Mensagem")