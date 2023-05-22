#modulo 2 - ALURA (https://cursos.alura.com.br/course/python-introducao-a-linguagem/task/22691)

numero_secreto = 43
print("********************************")
print("Bem vindo no jogo de Advinhacão")
print("********************************")
chute_srt = input("Digite o seu numero: ")
print("Voce digitou o numero", chute_srt)
chute = int(chute_srt)
if (numero_secreto == chute):
    print("Voce acertou!")
else:
    print("Voce errou!")
print("Fim do jogo")