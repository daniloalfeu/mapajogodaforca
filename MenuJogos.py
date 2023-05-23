import jogodaforca
def exibir_menu():
    print("Jogos de outras décadas - Menu Principal")
    print("--------------------")
    print("1 - Jogo da Forca")
    print("2 - Outro Jogo")
    print("3 - Sair")

def menu():
    exibir_menu()

    while True:
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            jogodaforca.menujogo()
        elif opcao == "2":
            # Lógica para abrir outro jogo
            pass
        elif opcao == "3":
            print("Obrigado por jogar!")
            break
        else:
            print("Opção inválida. Escolha novamente.")

menu()
