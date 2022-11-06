import random

def jogar():

    print("********************************")
    print("Bem vindo no johgo de Advinhacão!")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qaul nível de dificuldade?", numero_secreto)
    print("[1] Fácil [2] Médio [3] Dificil")

    nivel = int(input ("Define o nivel: "))
    if (nivel == 1):
      total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else: 
        total_de_tentativas = 5


    for rodada in range (1, total_de_tentativas +1) :
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Começo do teste!!", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute >= 100):
            print ("Voce deve digitar um numero entre 1 e 100!")
            continue


        acertou = numero_secreto == chute
        maior   = numero_secreto > chute
        menor   = numero_secreto < chute

        if (acertou):
            print("Voce acertou! E fez {} pontos".format(pontos))
            break
        else:
            if (maior):
                print("Voce errou. O numero é maior que este!")
            elif (menor):
                print("Voce errou. O numero é menor que este!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("fim do jogo")