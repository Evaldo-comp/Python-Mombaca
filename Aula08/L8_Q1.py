# Criação do arquivo
with open("numeros.txt", "w") as numeros:
    for i in range(2, 1001):

        numeros.write(f"{i}\n")

# Gerando os múltiplos
with open("multiplos2.txt", "w") as multiplos2:
    with open("numeros.txt") as numeros:
        for i in numeros.readlines():

            if int(i) % 2 == 0:
                multiplos2.write(f"{i}")
# Gerando os invertidos
with open("multiplos_invertidos.txt", "w") as multiplos_invertidos:
    with open("multiplos2.txt") as multiplos2:
        l = []
        for i in multiplos2.readlines():
            l.append(int(i))

        for i in l[::-1]:
            multiplos_invertidos.write(f"{i}\n")
# Impares
with open("impares.txt", "w") as impares:
    with open("numeros.txt") as numeros:
        for i in numeros.readlines():
            if int(i) % 2 != 0 and 10 < int(i) < 800:
                impares.write(f"{i}")

# Primos


def primo(n):
    cont = 0
    i = 0
    while i <= n or cont < 2:
        i = i + 1
        x = n % i
        if x == 0:
            cont = cont + 1

    if cont <= 2:
        primos.write(f"{n}\n")
        print("\n")


with open("primos.txt", "w") as primos:
    with open("numeros.txt") as numeros:

        for i in numeros:
            primo(int(i))


# multiplos
with open("multiplos2.txt", "w") as m2, open("multiplos3.txt", "w") as m3, open("multiplos5.txt", "w") as m5:
    with open("numeros.txt") as numeros:
        for i in numeros.readlines():
            if int(i) % 2 == 0:
                m2.write(f"{int(i)}\n")
            if int(i) % 3 == 0:
                m3.write(f"{int(i)}\n")
            if int(i) % 5 == 0:
                m5.write(f"{int(i)}\n")
