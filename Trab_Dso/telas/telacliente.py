import PySimpleGUI as sg

class TelaCliente():
  def __init__(self):  
    self.__window = None 
    self.init_opcoes()

  def init_opcoes(self):
    sg.theme_previewer()
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- AMIGOS ----------', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Incluir Amigo', "RD1", key='1')],
      [sg.Radio('Alterar Amigo', "RD1", key='2')],
      [sg.Radio('Listar Amigos', "RD1", key='3')],
      [sg.Radio('Excluir Amigo', "RD1", key='4')],
      [sg.Radio('Retornar', "RD1", key='0')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema de livros').Layout(layout)
    

  def tela_opcoes(self):
    # print("-------- CLIENTES ----------")
    # print("Escolha a opcao")
    # print("1 - Incluir cliente")
    # print("2 - Alterar cliente")
    # print("3 - Excluir cliente")
    # print("4 - Listar clientes")
    # print("0 - Retornar")

      # opcao = int(input("Escolha a opcao: "))
      # while opcao > 4 or opcao < 0:
      #       opcao = int(input("Escolha errada, selecione um valor válido: "))
        
      # return opcao
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

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def receber_dados(self):
    print("-------- DADOS cliente ----------")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    if isinstance(nome, str) and isinstance(telefone, str) and isinstance(cpf, str) and isinstance(email, str):
      return {"nome": nome, "cpf": cpf, "email": email, "telefone": telefone}
      

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostrar_cliente(self, dados_cliente):
    print("NOME DO cliente: ", dados_cliente["nome"])
    print("CPF DO cliente: ", dados_cliente["cpf"])
    print("EMAIL DO cliente", dados_cliente["email"])
    print("FONE DO cliente: ", dados_cliente["telefone"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_cliente(self):
    cpf = input("CPF do cliente que deseja selecionar: ")
    return cpf

  def mostra_mensagem(self, msg):
    print(msg)


  
  