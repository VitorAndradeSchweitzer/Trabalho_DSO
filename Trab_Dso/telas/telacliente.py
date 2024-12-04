import PySimpleGUI as sg

class TelaCliente():
  def __init__(self):
    self.__window = None
    self.init_opcoes()


  def tela_opcoes(self):
    self.init_opcoes()
    button, values = self.open()
    if values['1']:
      opcao = 1
    if values['2']:
      opcao = 2
    if values['3']:
      opcao = 3
    if values['4']:
      opcao = 4
    # cobre os casos de Retornar, fechar janela, ou clicar cancelar
    #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
    if values['0'] or button in (None, 'Cancelar'):
      opcao = 0
    self.close()
    return opcao

  def init_opcoes(self):
#    sg.theme_previewer()
    sg.ChangeLookAndFeel('DarkBrown2')
    layout = [
      [sg.Text('-------- CLIENTES ----------', font=("Fixedsys", 25))],
      [sg.Text('Escolha a opção', font=("Fixedsys", 15))],
      [sg.Radio('Incluir Cliente', "RD1", key='1')],
      [sg.Radio('Alterar Cliente', "RD1", key='2')],
      [sg.Radio('Listar Cliente', "RD1", key='3')],
      [sg.Radio('Excluir Cliente', "RD1", key='4')],
      [sg.Radio('Retornar', "RD1", key='0')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema Karaoke').Layout(layout)

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