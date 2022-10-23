#modulo3 aula 5
numero_secreto = 10

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

print("fim do jogo")