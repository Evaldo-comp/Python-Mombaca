# Faça quatro funções que retornem respectivamente
# (Nome, idade, Estado civil e Gênero)
'''
nome = input("Nome: ")
idade = int(input("Idade: "))
estado_civil = "Casado"
genero = "M"


# função do nome
def nome_pessoa(n):
    return n

# função da idade


def idade_pessoa(i):
    return i

# Função do estado civil


def estado_c(ec):
    return ec

# Função do genero


def genero(g):
    return g


print(nome_pessoa(nome))


# Crie uma função que receba como argumento sua idade
# e retorne o equivalente em minutos

def idade_em_minutos(i):
    dias = i * 365
    horas = dias * 24
    minutos = horas * 60
    return minutos


minutos = idade_em_minutos(20)
print(f"O lucas viveu até hoje {minutos} minutos")


# Crie uma função que retorne seu nome em caixa alta
'''


def maiusculo(n):

    return n.lower()


print(maiusculo("VANESSA"))
