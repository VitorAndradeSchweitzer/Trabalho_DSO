class TelaBibliotecaDeMusica:
    def mostrar_mensagem(self, mensagem: str):
        print(f"\n{mensagem}")

    def mostrar_lista_musicas(self, lista_musicas: list):
        print("\n=== Biblioteca de Músicas ===")
        if not lista_musicas:
            print("Nenhuma música disponível")
            return
        
        for musica in lista_musicas:
            print(f"\nTítulo: {musica.titulo}")
            print(f"Artista: {musica.artista}")
            print(f"Gênero: {musica.genero}")
            print(f"Idioma: {musica.idioma}")
            print(f"Código: {musica.codigo}")
            print(f"Vezes Tocada: {musica.numero_de_vezes_tocada}")

    def mostrar_opcoes(self) -> int:
        print("\n=== Relatório de Músicas ===")
        print("1. Relatório de Artista mais cantado")
        print("2. Relatório de Gênero mais cantado")
        print("3. Relatório de Idioma mais cantado")
        print("0. Retornar")
        
        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                if 0 <= opcao <= 3:
                    return opcao
                print("Por favor, insira uma opção válida (0-6)")
            except ValueError:
                print("Por favor, insira um número válido")

    def mostrar_mensagem(self, mensagem: str):
        print(f"\n{mensagem}")
