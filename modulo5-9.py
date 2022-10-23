#modulo5 - 09:   Para saber mais: Formatação de strings

#Exemplo 1:
print ("Tentativa {} de {}".format(3, 10))
#imprimi: Tentativa 3 de 10

#Exemplo 2:
print ("Tentativa {1} de {0}".format(3, 10))
#imprimi: Tentativa 10 de 3
#Ou seja, o primeiro item de uma lista, é sempre o zero e voce pode ir alterando eles entre si, conforme necessidade

print ("R$ {:.2f}".format(11111.50))
print ("R$ {:6.2f}".format(11111.50))
print ("R$ {:8.2f}".format(1.50))
print ("R$ {:08.2f}".format(1.5))
print ("R$ {:08.3f}".format(1.5))
print ("R$ {:07d}".format(4)) #d é digito ou inteiro
print ("R$ {:07d}".format(46))
print ("Data {:2d}/{:02d}".format(20,5))
print ("Data {:2d}/{:02d}/{:4d}".format(20,5,1990))

""""
ITEM 5.10:  Adaptando o Padrão Americano

Um desenvolvedor Python está tendo que adaptar um sistema americano de cadastro de clientes americanos para os clientes brasileiros. Ele está esbarrando em um problema, pois lá as pessoas têm o costume de se referir pelo sobrenome antes do primeiro nome, por exemplo: Smith, John .
Ele deseja adaptar as mensagens do sistema para o padrão brasileiro, mas sem alterar a estrutura de dados que ele recebe do banco de dados.
Digamos que ele queira exibir a seguinte mensagem: "Ola Sr. Leonardo Cordeiro", como ele pode formatar a string para obter o resultado desejado?

print("Ola Sr.{1} {0}".format("Cordeiro","Leonardo"))
"""

"""
ITEM 5.11: O resultado da interpolação

Temos as seguintes instruções:

"R$ {:7.1f}".format(1000.12)   =====>1000.12 tem 7 caraccteres
"R$ {:07.2f}".format(4.11)     =====>07 vai fazer com que o total de caracteres fique = 7, e 2f dps da virgula

Será impresso respectivamente no console:

R$  1000.1
R$ 0004.11
"""


""""
ITEM 5.12 Interpolação - Python 2 vs Python 3
A interpolação de strings também mudou entre o Python 2 e o Python 3.
Como você já viu, no Python 3 usa-se a função format junto com a sintaxe {} dentro da string, por exemplo:

"{} {}".format(1, 2)
O Python 2 usava uma sintaxe especial, ao invés do format era preciso usar o caractere %. Veja o exemplo:

"%d %d" % (1, 2)

Repare também que o % também era utilizado dentro da string.
Mais exemplos, sempre comparando o Python 2 com Python 3, existem no link: https://pyformat.info/
Vale a pena ver!



"""