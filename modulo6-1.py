#modulo6 - 01:  Gerando e arredondando um número aleatório
import random

print("********************************")
print("Bem vindo no jogo de Advinhacão")
print("********************************")

numero_secreto = 10
total_de_tentativas = 3
numero_random = random.random() * 100
#int(numero_random)
#print (int(numero_random))
print (round(numero_random))




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
        print("Voce acertou! parabens!")
        break
    else:
        if (maior):
            print("Voce errou. O numero é maior que este!")
        elif (menor):
            print("Voce errou. O numero é menor que este!")

print("fim do jogo")



""""ITEM 6.2
Vimos no video que foi necessário importar o módulo random:
import random
Por que foi necessário usar o comando import?

Porque o módulo random não está automaticamente disponível dentro do programa, só após importação.
"""