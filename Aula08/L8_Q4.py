# Questão 4 da lista 07

nome = "marcelo"


def dicionario(nome):
    dicionario = open("dicionario.txt", "w")
    dic = {x: [x for x in range(10) if x % 2 == 0] for x in nome}
    dicionario.write(f"{dic}\n")
    dicionario.close()


dicionario(nome)
