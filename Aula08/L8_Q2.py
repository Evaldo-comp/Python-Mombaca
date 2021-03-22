

# Tamanho dos nomes
with open("nomes.txt") as nomes:
    for i in nomes:
        print(i, len(i))

######################################################

# Iniciados com A
with open("inicial_A.txt", "w") as inicial_a:
    with open("nomes.txt") as nomes:
        for i in nomes.readlines():
            if i[0] == "A":
                inicial_a.write(f"{i}\n")

######################################################

# Palindromos
with open("palindromos.txt", "w") as palindromos:
    with open("nomes.txt") as nomes:
        for i in nomes:
            word1 = i
            word2 = word1.lower().strip().replace(' ', '')
            if word2 == word2[::-1]:
                palindromos.write(f"{word2}\n")

######################################################

# Busca por nome
with open("nomes.txt", "r") as nomes:
    if "Abílioaa" in nomes.read():
        print(True)
    else:
        print(False)
