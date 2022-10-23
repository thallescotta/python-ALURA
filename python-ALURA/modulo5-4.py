#modulo5 - 04:  Encerrando a interação e o loop

print("********************************")
print("Bem vindo no johgo de Advinhacão")
print("********************************")

numero_secreto = 10
total_de_tentativas = 3
rodada = 1


for rodada in range (1, total_de_tentativas +1) :
    print("Tentativa {} de {}".format(rodada, total_de_tentativas)) #format é uma funcao que chama as duas variaveis seguintes para dentro dos {}
    chute_str = input("Digite um numero entre 1 e 100: ")
    print("Começo do teste!!", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute >= 100):
        print ("Voce deve digitar um numero entre 1 e 100!")
        continue #em tese, continua com a proxima interação, caso o programa pare durante o loop.


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
#    rodada = rodada + 1
# nao precisa do incremento acima, pois o for da linha 10 ja faz isso

print("fim do jogo")

"""
ITEM: 5.5
Dentro de um laço, qual é a diferença entre break e continue?
break sai do bloco do laço abruptamente, continue apenas pula para próxima iteração.
"""

"ITEM: 5.6"
""""
Temos o seguinte código:

i = 1
while(i <= 7):
    print(i)
    i = i + 1
    if(i == 5):
        break
        
Apenas olhando esse código, sem executá-lo, qual será a saída no console?
1
2
3
4
"""

""""
ITEM 5.7:
E se fosse o código abaixo usando for e continue?

for i in range(1,8):
    if(i == 5):
        continue
    print(i)

Qual será a saída no console?
1
2
3
4
6
7
"""