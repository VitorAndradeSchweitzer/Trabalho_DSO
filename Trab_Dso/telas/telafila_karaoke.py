import PySimpleGUI as sg

class TelaFila:
    def __init__(self):
        sg.ChangeLookAndFeel('DarkBrown2')  # Define o tema da interface

    def tela_opcoes(self):
        """Exibe o menu de opções da fila."""
        layout = [
            [sg.Text("-------- FILA KARAOKÊ ----------", font=("Fixedsys", 18))],
            [sg.Text("Escolha a opção:", font=("Fixedsys", 12))],
            [sg.Button("Mostrar Fila", key=1)],
            [sg.Button("Passar a vez pro próximo", key=2)],
            [sg.Button("Adicionar Pedido", key=3)],
            [sg.Button("Remover Pedido", key=4)],
            [sg.Text("")],
            [sg.Button("Retornar", key=0)]
        ]

        window = sg.Window("Fila de Karaokê", layout)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, 0):  # Fecha no botão "Retornar" ou no X
                window.close()
                return 0
            if event in range(1, 5):
                window.close()
                return event



# class Telafila():
#     def tela_opcoes(self):
#         print("-------- FILA KARAOKE ----------")
#         print("Escolha a opcao")
#         print("1 - Mostrar Fila")
#         print("2 - Passar a vez pro proximo")
#         print("3 - Adicionar Pedido")
#         print("4 - Remover Pedido")
#         print("0 - Retornar")

#         resposta = int(input("Escolha o numero da opcao desejada: "))
#         return resposta

    def mostrar_fila(self, posicao, cliente, musica):
        """Mostra as informações de uma posição na fila."""
        sg.popup_ok(
            f"Posição: {posicao}\nCliente: {cliente.nome}\nCPF: {cliente.cpf}\nMúsica: {musica.titulo}",
            title="Detalhes da Fila"
        )

    def proximo_cantar(self, cliente, musica):
        """Mostra o próximo cliente a cantar e a música escolhida."""
        sg.popup_ok(
            f"--- Próximo a cantar ---\n\n{cliente.nome} irá cantar '{musica.titulo}'",
            title="Próximo a Cantar"
        )

    def receber_cpf_cliente(self):
        """Solicita o CPF do cliente."""
        layout = [
            [sg.Text("Digite o CPF do cliente:", font=("Fixedsys", 12))],
            [sg.InputText(key='cpf')],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Receber CPF", layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return None
            if values['cpf'].isdigit() and len(values['cpf']) == 11:  # Validação simples para CPF
                window.close()
                return values['cpf']
            else:
                sg.popup_error("Por favor, insira um CPF válido com 11 dígitos.")

    def receber_id_musica(self):
        """Solicita o ID da música."""
        layout = [
            [sg.Text("Digite o ID da música:", font=("Fixedsys", 12))],
            [sg.InputText(key='id_musica')],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Receber ID da Música", layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return None
            if values['id_musica'].isdigit():  # Validação simples para ID
                window.close()
                return int(values['id_musica'])
            else:
                sg.popup_error("Por favor, insira um ID válido (número).")

    def mostra_mensagem(self, msg):
        """Exibe mensagens gerais na interface gráfica."""
        sg.popup_ok(msg, title="Mensagem")