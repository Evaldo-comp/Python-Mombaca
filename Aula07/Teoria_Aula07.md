
# Aula 07 - Dicionários e Sets



## Sets

Os sets em python realizam operações básicas de união, intersecção e diferença, entre suas principais características, podemos destacar:
 - São imutáveis
 - São desordenados
 - Não indexáveis
 - Não permitem itens repetidos
 - Aceitam qualquer tipo de dado, inclusive outras coleções

---
### Criação e adição de elementos em um SET
A criação de um set pode ser feita associnado um conjunto de valores a uma variável ou simplismente invocando o construtor `set()` . 

```python
# Criando set com  a invocação do set()
a = set()
a.add("Banana") # adicionando itens individualmente
a.add("Jaca")
a.add("Banana")
print(a)

# Criando set com adição de vários itens ao mesmo tempo
b = {"Carro", "Bicicleta", 2, 1.2}
print(b)

# Criando set a partir de seu construtor, incluindo outras coleções

c = set([1, 2, 3]) # Convertendo uma lista para set
print(c)
print(type(c))
```
---
### Acessando itens em um SET:

Os itens de um set não podem ser referenciados pelo indice, caso precisemos acessá-lo, devemos utilizar um loop para percorrer o set
ou algum operador como por exemplo o `in`.

```python
frutas = {"Uva", "Banana", "Jaca"}
for x in frutas:
  print(x)
 ```
---

### Adicionando itens em um SET:
A adição de itens pode acontecer de forma única com o método `add()` ou adicionando itens de outro set ou até mesmo de outros tipos de coleções, 
para a segunda opção utilizamos o `update()`.

```python
# Utilizando add()
alunos_arte = {"Edson", "Pedro", "joão"}
alunos_arte.add("Ana") # Adiciona um aluno de forma individual



# Adicionando coleções com update
alunas_comp = ["Edinara", "Vitória", "Vanessa"]

alunos_uece ={"Lucas"}

alunos_uece.update(alunas_comp) # A lista é adicionada por meio do método update()
print(alunos_uece)

```
---
> 📝:Prática01
> Crie uma função que receba uma lista, uma tupla, e retorne um set contendo os itens dessas coleções.
---

### Removendo item de um SET:

Existem várias formas de realizar a remoção de um item de um set, cada uma tem um comportamento diferente

- `remove()`:  Retorna um erro se tentarmos remover um item que não existe

- `discard()`: Não retorna um erro se tentarmos eliminar um item que não existe.

 - `pop()`:  Remove o último item e guarda o valor

 - `clear()`: Limpa o set

 - `del`:  Destroi o set:

*Dica: Crie um set e teste cada opção

---

### Operações básicas com Sets:

**Diferença entre SETs:**

Retorna a diferença entre dois conjuntos
```python
set1={0,1, 2, 3, 4}
set2= {2, 3, 4,5}
print(set1  - set2) # imprime os elementos que estão em set1 e não estão em set2

dif = set1.difference(set2) # Recupera o valor para utilizar posteriormente
print(dif)
```

**União entre SETS**:
É semelhante  a operação clássica com conjuntos, ele junta dois conjuntos em um só.

```python
set1={0,1, 2, 3, 4}
set2= {2, 3, 4,5}
print(set1  | set2) # imprime a união de set1 e set2

uni = set1.union(set2) # Recupera o valor para utilizar posteriormente
print(uni)
```


**Intesecção entre SETs**

A intersecção é o conjunto de itens comuns entre 1 ou mais conjuntos, para fazer isso em python podemos utilizar dois métodos:


- O `intersection()` não altera o set
- O `intersection_update()` altera 1 dos sets que participam da intersecção
```python
set1 = {1, 2, 3}
set2 = {4, 5, 6, 1}

print(set1.intersection(set2))
set1.intersection_update(set2) # altera o set1, incluindo os valore de set2
print(set1)
```
---
> 📝:Prática02:
> Faça uma função que receba dois SETs e retorne alguma operação básica realizada entre ambos.
---

# Dicionários:

O dicionário consiste em uma combinação de CHAVE e VALOR. Cada elemento de um dicionário segue esta combinação e são organizados 
dentro de chaves, diferente das listas que utilizam colchetes e tuplas que utilizam parêteses.


`Estrutura = {“Chave”: valor, “Chave”: valor}`


Ao associar um valor a uma chave, se essa chave já existir o valor será substituído, se a chave não existir uma nova chave será criada.

```python
# Exemplo:
usuario_acesso = {
    "login": "adm",
     "senha": 123,
         }
```
    
### Acessando intens de um dicionário:

Podemos optar por acessar não apenas os itens, mas somente chaves ou somente valores.
```python
# Obtendo um valor
v = usuario_acesso["login"]
print(v)

# Obtendo o valor com o metodo get()
v2 = usuario_acesso.get("login")
print(v2)

# Obtendo todos valores com o método value()
v3 = usuario_acesso.values()
print(v3)

# Obtendo chaves com o métod keys()
k = usuario_acesso.keys()
print(k)

# Obtendo itens com o método itens()
i = usuario_acesso.items()
print(i)
```
---
###  Verificação de valores e chaves:
Pode ser que você precise, em algum momento, verificar a presença de deteminada chave dentro de um dicionário, para fazer isso use o operador `in`

```python
# Verifcando a existência de determinada chave
usuario_acesso = {
    "login": "adm",
     "senha": 123,
         }
if "palavra_chave" in usuario_acesso:  # Verifica se a chave "palavra_chave" está dentro do dicionário
  print("A chave existe")
else:
  print("a chave não existe")
  
print(usuario_acesso)
```
---
### Modificando o valor de uma chave

A modificação de um valor pode ser feita invocando o nome da chave e associando um novo valor, mas cuidado, se a chave não existir, ela será adicionada.

```python

usuario_acesso = {
    "login": "adm",
     "senha": 123,
         }
usuario_acesso["login"] = "usr" # modifica o valor da chave login
usuario_acesso["palavra_chave]: "Batata"  # como a chave invocada não existe, ela será inserida no dicionário
```
---
> 📝:Prática02:

>Crie uma função que receba um dicionario e uma chave, a função deve retornar "existe" e o  valor da chave, caso ela exista.
>Caso ela não exista, deve  adicionar a chave e retornar o dicionário.
---


### Adicionando chave e item ao mesmo tempo:

É possível adicionar um conjunto de chave e item com o método upadate

```python
usuario_acesso = {
    "login" : "Edson",
    "senha": 23
}
usuario_acesso.update({"palavra_chave": 1.76})
print(usuario_acesso)
```
---

### Removendo itens de um Dicionário:

Existem alguns métodos que servem para manipular os items de um dicionário, entre eles os mais utilizados são `pop()` e `del`:

```python
# Removendo item com pop
funcionário =  {
    "nome" : "José",
    "matricula" :1223766,
    "salário" : 989.0,
    "ferias": True,
    "horas_extras": 3
}

rem = funcionario.pop("ferias") # remove o item férias
print(funcionario)
print(rem)

# removendo com del. Este não retorna o valor
del funcionario["nome"]
print(funcionario)
```
---


### Dic Comprehension:

O Comprehension é uma forma de gerar uma estrutura em uma linha única, pode ser utilizada em lista e agora veremos como aplicar comprehension em dicionários
```python
# gerando um dicionário de chaves que vão de 0 a 10 e valores que são o quadrado dessas chaves.
a = {x :x**2 for x in range(0,10, 2)}
print(a)

# gera um dicionário de chaves strings e valores que são a metodade das chaves do tipo floats. A expressão final filtra somente os pares
b = { str(x) : x /2 for x in range (0, 100) if x %2 == 0}
print(b)
```

### Fazendo iteração com dicionários:

Podemos percorrer um dicionário e obter somente as chaves,valores ou ambos

```python
funcionario =  {
    "nome" : "José",
    "matricula" :1223766,
    "salário" : 989.0,
    "ferias": True,
    "horas_extras": 3
}

# Obtendo somente as chaves
for x in funcionario.keys():
  print(x)

print("###########################")

# Obtendo somente os valores
for x in funcionario.values():
  print(x)

print("###########################")

#Obterndo chaves e valores
for k, v in funcionario.items():
  print(k, v)
```
---
> 📝:Prática02:
> Utilizando dic comprehension crie um diconário que tenha como chave os números pares de 1 a 100 e como valor o seus respectivos triplos
---

:house: [HOME](https://github.com/Evaldo-comp/Python-Mombaca)

---

