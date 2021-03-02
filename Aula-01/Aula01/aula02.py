# funções
# Identação
# Variáveis
# Cometários
# Input e output
# Strings
# Operadores


# funções
'''
def quadrado(num):
    return num ** 2


def nome(nome):
    if nome[0] == "n":
        print(nome)


nome("Evaldo")
a = quadrado(2)
print(quadrado(3))


# Variáveis
idade = 12.0
nome = "Evaldo"
altura = 1.75
is_casado = True
a = None
print(type(idade))

# nomenado variáveis
# 1valor = 12
v@lor = 12
classe = 12
print(classe)

# nomeação de nomes compostos
minhaNotaSemanal = 12  # Camel Case

MinhaNotaSemanal = 12  # pascal Case

minha_nota_semanal = 12  # snake_case

# comentários
# uma linha

variás
linhas


# input output

nome = input("digite seu nome")
idade = int(input("Idade: "))

# print(type(nome))
# print(type(idade))

print("Meu nome é : ", nome)
print("Meu nome é {} e minha idade é {}".format(nome, idade))
print(f"Meu nome é {nome} e eu tenho {idade} anos")

a = 'Evaldo'
print("{0:#^100}".format(a))

1 Pratica:
Criem três funções que retornem respectivamente
Nome, idade, estado civil



def nome(nome):
    return nome


n = input("nome")

print(nome(n))
'''
# Operadores
# Aritméticos
# Atribuiçãp
# comapração
# lógicos
# relacionais

# operadores Artiméticos
soma = 1 + 2
div = 10 / 5
div2 = 10 // 5
sub = 10 - 4
modulo = 10 % 3
pot = 2 ** 2

# Atribuição
num1 = 2
num2 = 3

num1 += num2  # num1 = num1+ num2
num1 -= num2  # num1 = num1 - num2
num1 *= num2  # num1 = num1 * num2
num1 /= num2  # num1 = num1 / num2
num1 **= num2  # num1 = num1 ** num2

# Operadores Comparação / Relacionais
'''
print(num1 == num2)

print(num1 != num2)

print(num1 >= num2)

print(num1 <= num2)

print(num1 > num2)
print(num1 < num2)
'''

# Operadores Lógicos
# num4 = 2
# num5 = 3
# print((num4 == num5) or (num5 >= 3))


# operadores  De Associação
# nome = " Francisco Evaldo"
# print("F" not in nome)

# Crie uma função que retorne seu nome em caixa alta(.upper)

'''
def idade(num):
    return num


def minutos(idade):

    dias = idade * 365
    horas = dias * 24
    minutos = horas * 60
    return minutos


print(minutos(idade(23)))
'''


def estado_civil(estado):
    return estado


def Match(estado_civil, meu):
    a = estado_civil and meu
    if estado_civil == "Solteiro" and meu == "Solteiro":
        return True
    else:
        return False


print(Match(estado_civil("Casado"), "Solteiro"))
print(type(estado_civil))


def genero(gen):
    return gen


def encontro(Match, genero):
    if Match == True and genero == "M":
        return "Bora"
    else:
        return "Deixa quieto"


print(encontro(Match(estado_civil("Casado"), "Solteiro")), genero(gen))
