class SystemScreen:
    def mostrar_opcoes(self) -> int:
        print("\n=== Karaoke Management System ===")
        print("1. Controlador Cliente")
        print("2. Controlador Musica")
        print("3. Controlador Fila")
        print("4. Controlador Mesa")
        print("5. Relatórios Músicas")
        print("0. Exit")
        
        while True:
            try:
                option = int(input("Escolha uma opção: "))
                if 0 <= option <= 5:
                    return option
                print("Por favor escolha uma opção válida (0-4)")
            except ValueError:
                print("Insira um numero por favor")

    def mostra_menssagem(self, menssagem):
        print(menssagem)
