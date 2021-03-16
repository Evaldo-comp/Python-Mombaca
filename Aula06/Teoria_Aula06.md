


# Aula 06 - Listas de Tuplas

* Lista
   - Criação e características
   - Modifcando items
   - Acesso e Fatiamento
   - Percorrendo uma lista (for-while - List Comprehension) 
   - Listas de listas
   - Métodos
* Tuplas
  - Características
  - Desenpacotamento

## Criação de  Listas
Listas são tipos de dados compostos que podêm conter elementos de vários tipos, inclusive outras listas. As listas são mutáveis e representadas por elementos 
dentro de um par de colchetes:

```python
L = [1, 1.75, True, "Evaldo"]
```

*O exemplo acima mostra a criação de uma lista de nome L que contém dados do tipo int, string, float e bool.

---

## Acessando um elemento:
Para acessar um elemento de uma lista utilise a refrência ao indice, para acessar a lista como um todo basta chamar o nome da lista

```python

# Acesso item
L = [1, 1.75, True, "Evaldo"]
print(L)
print(L[0]) # acesso a um item em especifico
print(L[-1]) #utilizando  índice negativo
```
---

## Modificando elemento:

As listas são indexáveis, sendo que o primeiro índice é o 0. Para alterar determinado elemento de uma lista, basta atribuir esse novo elemento a um determinado 
índice da lista.

Veja abaixo a forma de alterar um elemento de uma lista 

```python
L = [1, 1.75, True, "Evaldo"]
L[2] = False  # altera o valor do indice dois de True para False
```
----
> 📝:Prática01

> - Crie uma lista com pelo menos 5 items. 
> - Crie uma função que receba a lista e um item. A  função deve retornar a mesma lista com o item modificado
> - Adicione mais um parâmetro que será a posição que será modificada
 ---


## Fatiamento de Lista
Podemos selecionar um intervalo dentro de uma lista apenas utilizando uma técnica chamada slice, ou fatiamento, essa técnica nos permite extrair 
um um 'pedaço' da lista, caso não queiramos ela por inteiro. Imagine um bolo 🥮: o slice nos permite tirar uma fatia desse bolo, ou melhor, um 
pedaço da lista..



#### Exemplos de slice 
```python
lista = ["P", "y", "t", "h", "o", "n"]
lista[0:5]
lista[0:]
lista[:]
lista[:5]
lista[:-1]
lista[2:5]
lista[::4]
lista[::-1]

```

Podemos utilizar o slice para modificar um determinado trecho da lista 

```python

L[:3] = "X","X", "X"
print(L)
```
---

> 📝:Prática02
> Crie uma função que receba 3 números e uma listae dentro da função você vai gerar três recortes diferentes.

---

## Percorrendo uma lista:
A forma mais eficiente de percorrer uma lista é utilizando o laço `for`:

```python
L = [1, 1.75, True, "Evaldo"]
for i in L:
  print(i)
```

Também é possível percorrer a lista com o `while`.

```python

i = 0
while i < len(L):
  print(L[i])
  i = i + 1
  ```
---

## List Comprehension
Essa técnica gera uma nova lista com base em condições, e iteração de objetos, assemalha-se a função lambda, pois de certa forma simplifica 
trechos que seriam escritos em blocos de código mais extensos.

 Sintax:  `nova_lista = [expressao for item in iterável ]`

#### Exemplo: 
```python
nova_lista = [x for x in range(0, 12) ]
print(nova_lista)
```

Essa técnica pode ser aperfeiçoada para gerar listas com condicionais
```python
# nova_lista = [expressao for item in iteravel if condicao == True]

nova_lista = [x for x in range(0, 12) if x%2 !=0 ]
print(lis2)
```

Alterando a expressão antes do `for` podemos manipular melhor as saídas.
```python
nova_lista = [x ** 2 for x in range(0. 100)]
print(nova_lista)
```

---
> 📝:Prática03

> Crie um lista uilizando list comprehension, tente incluir algum criatério

---

## Lista de listas:

Uma lista pode ser composta por outras listas, gerando dessa forma um estrutura bidimensional(Matriz)


#### Exemplo de lista de lista
```python
produto1 = ["Arroz", 1, 2.20]
produto2 = ["Feijão", 2, 4.20]
produto3 = ["Maçã", 5, 0.20]

lista_compras =[produto1, produto2, produto3]

print(lista_compras)
#print(lista_compras[1][2]) Referenciar um item especifico
for e in lista_compras:
  print(f"Produto: {e[0]} quantidade {e[1]} preço {e[2]:.2f}")

```
----

## Métodos de Listas

#### append() - Adiciona um elemento no fim da lista

```python
L = ["a", "b"]
L..append("c")
```

#### sort() - sse método organiza a lista na ordem crescente:

```python
vogais = ["u", "a", "i", "e", "o"]
vogais.sort()
print(vogais)
```

#### insert() - Para adicionar um item em um lugar especifico devemos utilizar o método insert(), que recebe dois argumentos, o primeiro é o indice onde o elemento será adicionado e o segundo será o próprio elemento.
```python
L = [1, 3, 4, 5]
L.insert(1, 2)
```

#### pop() - Esse método recebe como argumento o indice do elemento que você deseja excluir, e retorna o elemento excluido, se não for inserido nenhum argumento, ele irá remover o último elemento da lista:


```python
titulos_palmeiras =["Brasileiro", "Copa do Brasil","Mundial", "Libertadores"]

nao_tem = titulos_palmeiras.pop(2)
print(nao_tem)
print(titulos_palmeiras)
```


#### del - Caso não seja necessário recuperar o item excluído, basta usar o del, ele simplismente descarta o item

```python
titulos_palmeiras =["Brasileiro", "Copa do Brasil","Mundial", "Libertadores"]

del titulos_palmeniras[1]
print(titulos_palmeiras)
``` 

#### copy() - Esse método copia o conteúdo de uma lista para outra


```python
numeros = [1, 2, 3, 4, 5]

novos_numeros = numeros.copy()

``` 

#### extend() - Esse método junta uma lista a outra, ele não gera uma terceira 


```python
numeros = [1, 2, 3, 4, 5]
letras = ["a", "b", "c"]

numeros.extend(letras)

Oberve a diferença entre
lista3 = numeros + letras

``` 
---


# Tuplas:

As tuplas são imutáveis, por isso são indicadas para trabalhar com valores constantes, como por exemplo, dias da semana, meses do ano e etc. Para criar uma tupla utilizamos parênteses, apesar dos parênteses serem opcionais,sua utilização é indicada para facilitar a leitura.


`Cavaleiros = (Seya, Yoga, Shun, Shiriu, Ikki)`


OBS: Se a tupla tiver apenas um elemento, a sua estrutura deve ser a a seguinte:

Elemento único, dentro de parênteses e uma vírgula

`Aries =("Mu",)`

## Criando uma tupla
Podemos criar tuplas de duas formas:

A primeira é associando os valores a uma variável e a outra é utilizando o construtor  `tuple()`.

```python
# Criando tupla com associação de valores
t = ("a", "e", "i", "o", "u")
print(type(t))
print(t)

# Criando uma tupla utilizando o contrutor tuple()
Nome = "Evaldo"
t2 = tuple(Nome)
print(type(t2))
print(t2)

Lista = [1, 2, 3, 4]
t3 = tuple(Lista)
print(t3)
```
---
> 📝:Prática04

> Crie uma lista que contenha: Nome, idade, cidade.

> Converta essa lista para tupla
---

##  Utilizando tupla para desempacotar
A tupla empacota dados em uma única estrutura, o caminho inverso, chama-se desenpacotamento, você atribui uma variável para cada item da tupla

```python
T = ("Evaldo", 34, "Maranguape" ) # packing

nome, idade, cidade = T           # unpacking
print(nome)
```

---

## Removendo e adicionando itens em uma tupla:

Não é possivel remover e adicionar items em uma tupla, o que podemos fazer é transformar  tupla em lista, fazer o processo de remoção ou adição e 
transformar a lista em tupla

```python
T = ("Evaldo", 34, "Maranguape")
lis = list(T) # converte a tupla em lista
print(lis)
lis.append(1.75)  # altera a lista
print(lis)
T = tuple(lis) # converte a lista em tupla
print(T)

```

---

> 📝:Prática04
> Adicione um item na sua tupla e desempacote ela

---

:house: [HOME](https://github.com/Evaldo-comp/Python-Mombaca)

---
