import random

def jogar():
    
    bem_vindo()
    palavra_secreta = puxando_palavras_do_arquivo()
    letras_acertadas = Preenchendo_lugares_com_letras_corretas(palavra_secreta)
    
    print(letras_acertadas)

#Funcao do arquivo
    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_palavras()

        if(chute in palavra_secreta):
            marca_chute_correto(palavra_secreta,chute,letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        
        print(letras_acertadas)


    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()


def bem_vindo():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def puxando_palavras_do_arquivo():
    arquivo = open("Palavras.txt", "r")
    palavras = []
    
    for linha in arquivo: 
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo. close()
    
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    
    return palavra_secreta

def Preenchendo_lugares_com_letras_corretas(palavra_secreta):
    return ["_"for letra in palavra_secreta]

def pede_palavras():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    
    return chute



def marca_chute_correto(palavra_secreta,chute,letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")





def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()

