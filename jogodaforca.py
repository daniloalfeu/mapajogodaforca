import random
import sys
import MenuJogos


def carrega_palavra_secreta():
    palavras = []
    with open("basedepalavras.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("\nAgora escolha uma letra: ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1

def acertou_todas():
    print("Parabéns, você acertou a palavra!")

def errou_todas(palavra_secreta):
    print("Xiii! Uma pena você foi enforcado!")
    print("A palavra era: {}".format(palavra_secreta))


    print(" |  (X_X) ")
    print(" |   \|/  ")
    print(" |    |   ")
    print(" |   / \  ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (o_o) ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |     (o_o)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |     (o_o)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |     (o_o)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |     (o_o)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |     (o_o)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |     (o_o)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():

    print("Divirta-se!")
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    exibiu_quantidade_letras = False
    primeira_iteracao = True

    while not acertou and not enforcou:
        if primeira_iteracao:
            print("\nVamos começar:")
            primeira_iteracao = False

        if not exibiu_quantidade_letras:
            print("\nA Palavra tem:", len(palavra_secreta),"letras:",)
            exibiu_quantidade_letras = True

        print(" ".join(letras_acertadas))
        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            if "_" not in letras_acertadas:
                acertou = True
        else:
            erros += 1
            print("\nVocê errou! Restam apenas {} tentativas.".format(7 - erros))
            desenha_forca(erros)

        if erros == 7:
            enforcou = True

    if acertou:
        acertou_todas()
    else:
        errou_todas(palavra_secreta)

    menu_reiniciar()


def menu_reiniciar():
    while True:
        resposta = input("Quer jogar novamente? (s/n): ")

        if resposta.lower() == "s":
            jogar()
        elif resposta.lower() == "n":
            menujogo()
            break
        else:
            print("Opção inválida. Escolha novamente.")


def exibir_menuforca():
    print("Jogos de outras décadas - Jogo da Forca")
    print("Bem vindo ao jogo da forca.")
    print("--------------------")
    print("1 - Jogar")
    print("2 - Sobre o jogo")
    print("3 - Sair")

def menujogo() -> object:
    exibir_menuforca()

    while True:
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            jogar()
        elif opcao == "2":
            print("Jogo da Forca é um jogo em que o jogador deve acertar uma palavra secreta.")
            print("O jogador deve chutar letras até acertar todas as letras da palavra ou até ser enforcado.")
            print("Vamos jogar?")
            menu2()
        elif opcao == "3":
            print("Obrigado por jogar!")
            MenuJogos.menu()
            sys.exit()
        else:
            print("Opção inválida. Escolha novamente.")

def menu2():
    print("1 - Jogar")
    print("2 - Sair")

    while True:
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            jogar()
            break
        elif opcao == "2":
            print("Obrigado e retorne sempre que quiser.")
            sys.exit()
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    menujogo()