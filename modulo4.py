#modulo4 aula 1 (https://cursos.alura.com.br/course/python-introducao-a-linguagem/task/24543)
#Laço WHILE
#contado 3 rodadas, fazendo o while e verfica-se no Run o comportamento alcançado

print("********************************")
print("Bem vindo no johgo de Advinhacão")
print("********************************")

numero_secreto = 10
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa", rodada, "de", total_de_tentativas)
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
    rodada = rodada + 1

print("fim do jogo")

# O que o if e while tem em comum?
# Ambos, if e while, possuem uma condição de entrada. A diferença é que o if executa o bloco apenas uma vez, mas o while repete o bloco enquanto a condição for verdadeira.
# O interessante é que o Python não possui um laço com uma condição de saída, que outras linguagens chamam de do-while.
