#https://cursos.alura.com.br/course/python-introducao-a-linguagem/task/24567
#modulo5 - 01: Laço com for
print("********************************")
print("Bem vindo no johgo de Advinhacão")
print("********************************")

numero_secreto = 10
total_de_tentativas = 3
rodada = 1


for rodada in range (1, total_de_tentativas +1) : # o +1 eh pois o range nao inclui o ultimo elemento dele
    print("Tentativa {} de {}".format(rodada, total_de_tentativas)) #format é uma funcao que chama as duas variaveis seguintes para dentro dos {}
    chute_str = input("Digite o numero: ")
    print("Começo do teste!!", chute_str)
    ##chute_srt = input ("Digite seu numero: ")
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior   = numero_secreto > chute
    menor   = numero_secreto < chute

    if (acertou):
        print("Voce acertou! parabens!")
    else:
        if (maior):
            print("Voce errou. O numero é maior que este!")
        elif (menor):
            print("Voce errou. O numero é menor que este!")
#    rodada = rodada + 1
# nao precisa do incremento acima, pois o for da linha 10 ja faz isso

print("fim do jogo")


'''
ITEM 5.2
Temos o seguinte loop usando while:

contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 1

Qual das opções abaixo possui o mesmo resultado usando for .. range?

for contador in range(1, 11):
    print(contador)

'''



"""
ITEM 5.3
Temos o seguinte código:

contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 3

Que imprime:

1
4
7
10

Como você poderia substituir o código acima usando o laço for .. range?

    for contador in range(1,11,3):
        print(contador)

"""