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

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'


  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # def tela_opcoes(self):
  #   print("-------- CLIENTES ----------")
  #   print("Escolha a opcao")
  #   print("1 - Incluir cliente")
  #   print("2 - Alterar cliente")
  #   print("3 - Excluir cliente")
  #   print("4 - Listar clientes")
  #   print("0 - Retornar")

    
  #   opcao = int(input("Escolha a opcao: "))
  #   while opcao > 4 or opcao < 0:
  #         opcao = int(input("Escolha errada, selecione um valor válido: "))
      
  #   return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

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

  # def receber_dados(self):
  #   print("-------- DADOS cliente ----------")
  #   nome = input("Nome: ")
  #   cpf = input("CPF: ")
  #   email = input("Email: ")
  #   telefone = input("Telefone: ")

  #   if isinstance(nome, str) and isinstance(telefone, str) and isinstance(cpf, str) and isinstance(email, str):
  #     return {"nome": nome, "cpf": cpf, "email": email, "telefone": telefone}

  def mostrar_cliente(self, dados_cliente):
    string_todos_clientes = ''
    for cliente in dados_cliente:
      string_todos_clientes += f"{cliente.nome}, {cliente.cpf}" + "\n"

      # string_todos_clientes = string_todos_clientes + "NOME DO AMIGO: " + str(dado["nome"]) + '\n'
      # string_todos_clientes = string_todos_clientes + "CPF DO AMIGO: " + str(dado["cpf"]) + '\n'
      # string_todos_clientes = string_todos_clientes + "EMAIL DO AMIGO: " + str(dado["email"]) + '\n'
      # string_todos_clientes = string_todos_clientes + "FONE DO AMIGO: " + str(dado["telefone"]) + '\n\n'

    sg.Popup('-------- LISTA DE CLIENTES ----------', string_todos_clientes)



  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # def mostrar_cliente(self, dados_cliente):
  #   print("NOME DO cliente: ", dados_cliente["nome"])
  #   print("CPF DO cliente: ", dados_cliente["cpf"])
  #   print("EMAIL DO cliente", dados_cliente["email"])
  #   print("FONE DO cliente: ", dados_cliente["telefone"])
  #   print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

  def seleciona_cliente(self):
    sg.ChangeLookAndFeel('DarkBrown2')
    layout = [
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

  # def seleciona_cliente(self):
  #   cpf = input("CPF do cliente que deseja selecionar: ")
  #   return cpf

  def mostra_mensagem(self, msg):
    sg.popup("", msg)

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values