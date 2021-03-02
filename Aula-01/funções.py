def nome(n):
    return n


def idade(i):
    return i


def estado_civil(ec):
    return ec


def genero(g):
    return g


print(nome("Evaldo"))
print(idade(34))
print(estado_civil("Casado"))
print(genero("M"))


def nome_maiusculo(nome):
    a = nome.upper()
    return a


print(nome_maiusculo(nome("evaldo")))


def minutos_vividos(idade):
    dias = idade * 365
    horas = dias * 24
    minutos = horas * 60
    return minutos


print(minutos_vividos(idade(34)))


def match(estado_civil, crush_ec):
    if estado_civil == "solteiro" and crush_ec == "solteiro":
        return "bora"
    return "Deixa quieto"


print(match(estado_civil("solteiro"), "solteiro"))
