#modulo4 aula 1 (https://cursos.alura.com.br/course/python-introducao-a-linguagem/task/24546)


print("********************************")
print("Bem vindo no jogo de Advinhacão")
print("********************************")

numero_secreto = 10
total_de_tentativas = 3
rodada = 1


#String interpolation => interpolação de strings
while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas)) #format é uma funcao que chama as duas variaveis seguintes para dentro dos {} => "String interpolation"
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