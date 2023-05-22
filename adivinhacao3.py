#modulo 3 - ALURA (https://cursos.alura.com.br/course/python-introducao-a-linguagem/task/22811)

numero_secreto = 43
print("********************************")
print("Bem vindo no jogo de Advinhacão")
print("********************************")
chute_srt = input("Digite o seu numero: ")
print("Voce digitou o numero", chute_srt)

chute = int(chute_srt)

acertou = chute == numero_secreto
e_maior = chute > numero_secreto
e_menor = chute < numero_secreto

if (acertou):
    print("Voce acertou!")
else:
    if (e_maior):
        print ("Voce errou! O chute foi maior do que o numero secreto.")
    elif (e_menor): #elif vai substituir o que poderia ser if tbm. elif = else
        print("Voce errou! O chute foi menor do que o numero secreto.")
print("Fim do jogo")