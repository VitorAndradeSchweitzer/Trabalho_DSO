import PySimpleGUI as sg

class TelaCliente():
  def __init__(self):
    sg.ChangeLookAndFeel('DarkBrown2')

  def tela_opcoes(self):
      
      sg.ChangeLookAndFeel('DarkBrown2')

      layout = [
          [sg.Text('-------- CLIENTES ----------', font=("Fixedsys", 25))],
          [sg.Button("Incluir Cliente", key=1)],
          [sg.Button("Alterar Cliente", key=2)],
          [sg.Button("Listar Cliente", key=3)],
          [sg.Button("Excluir Cliente", key=4)],
          [sg.Button("Retornar", key=0)]
      ]
      window = sg.Window("Menu de Cliente", layout)

      while True:
          event, _ = window.read()
          if event in (sg.WINDOW_CLOSED, 0):
              window.close()
              return 0
          if event in range(1, 5):
              window.close()
              return event

  def receber_dados(self):

    sg.ChangeLookAndFeel('DarkBrown2')
    layout = [

      [sg.Text('-------- DADOS CLIENTE ----------', font=("Fixedsys", 25))],
      [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
      [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
      [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
      [sg.Text('Telefone:', size=(15, 1)), sg.InputText('', key='telefone')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema Karaoke').Layout(layout)

    button, values = self.open()
    nome = values['nome']
    cpf = values['cpf']
    email = values['email']
    telefone = values['telefone']

    self.close()
    return {"nome": nome, "cpf": cpf, "email": email, "telefone": telefone}

  def mostrar_cliente(self, dados_cliente):
    string_todos_clientes = ''
    for cliente in dados_cliente:
      string_todos_clientes += f"{cliente.nome}, {cliente.cpf}" + "\n"
    sg.Popup('-------- LISTA DE CLIENTES ----------', string_todos_clientes)

  def seleciona_cliente(self, dados_cliente):
    string_todos_clientes = ''
    for cliente in dados_cliente:
      string_todos_clientes += f"{cliente.nome}, {cliente.cpf}" + "\n"
    
    sg.ChangeLookAndFeel('DarkBrown2')
    layout = [
      [sg.Text(string_todos_clientes)],
      [sg.Text('-------- SELECIONAR CLIENTE ----------', font=("Fixedsys", 25))],
      [sg.Text('Digite o CPF do cliente que deseja selecionar:', font=("Fixedsys", 15))],
      [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Seleciona cliente').Layout(layout)

    button, values = self.open()
    cpf = values['cpf']
    self.close()
    return cpf

  def mostra_mensagem(self, msg):
    sg.popup("", msg)

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values