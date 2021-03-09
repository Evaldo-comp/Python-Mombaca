
# AULA04 - FUNÇÕES

## Funções
 - Definição
 - Exemplos
 - Variáveis locais e Globais
 - Parâmetros opcionais
 - Função como parâmetro
 - Funções Lambda

---

Quando começamos a programar em Python, normalmente iniciamos com conceitos básicos como fundamentos de sintaxe da linguagem, mas tem um elemento que está presente desde o primeiro "Hello World", são as funções. 
A linguagem possui funções embutidas que começamos a utilizar mesmo sem saber que são funções, as principais são (`len()`, `int()`, `print()`, `input()`). As funções são utilizadas principalmente para isolar uma
tarefa e dessa forma reutilizá-las em outra parte sem precisar reescrever a mesma instrução.

**Exemplo:**
```python
# função que retorna a área de um quadrado
def area_quadrado(area):
  return area ** 2
print(area_quadrado(4))
```
---

## Variáveis Locais e Globais

Quando começamos a trabalhar com funções, nós utilizamos variáveis em escopos diferentes, ou seja , em campos de atuação diferentes. Uma variável que é 
declarada dentro de uma função, só funciona dentro desta função, é o que chamamos de variável local, da mesma forma uma variável que é declarada fora 
de uma função é reconhecida por todas as funções e blocos de código, esta é a variável global, o que diferencia uma da outra é o escopo ao qual elas
tem alcance.

**Exemplo:**
```python
a = 10
def numero ():
  # a += 1
  print(a)
 
numero()
```
Obs:*Uma variável global pode ser lida e utilizada em operações dentro de uma função, mas não pode ser modificada, para que seu valor possa ser modificado 
dentro do escopo da função é preciso que declaremos esta variável como do tipo `global`.

**Exemplo:**
```python
a = 10
def numero ():
 
  global a
  a += 1
  print(a)  

 
numero()
```

*As variáveis locais nascem e morrem dentro da função, ou bloco ao qual ela foi inicializada. O trecho de código abaixo retorna um erro, pois a variável que
estamos tentando imprimir fora da função, não pode ser acessada tendo em vista que ela está fora do escopo.*

```python
def soma(numero):
  b = 10
  return num * 2
print(f"A variavel {b} é local")
```
---

## Parâmetros Opcionais:

Os parâmetros opcionais nos dão a liberdade de passar ou não um determinado argumento para a função, isso acontece porque esse parâmetro quando declarado 
na função, já recebe um valor padrão que será utilizado caso um outro valor não for passado como argumento.


**Exemplo:**
```python
def paredao_falso(b1 = "caio"):
  print(f"Está no paredão falso:  {b1}")
paredao_falso("Poca")
```
Podemos combinar parâmetros opcionais com obrigatórios, mas os opcionais devem ficar sempre por último na definição da função.

**Exemplo:**
```python
def paredao_falso(b2, b3, b1 = "Caio"):
  print(f"""Está no paredão falso:  
          {b1}
          {b2}
          {b3}""")
paredao_falso("Poca", "Carla")
```
---

## Nomeando Argumentos:

Uma função sempre pega os argumentos passados e associa aos parâmetros na ordem que se encontram na função, mas isso pode ser modificado se passarmos argumentos
nomeados para a função

**Exemplo:**
```python
def nome_sobrenome(nome, nome_meio, idade):
  print(f"{nome} {nome_meio}: {idade} anos")

nome_sobrenome(idade = 34, nome_meio="Evaldo", nome = "Francisco")
```
---

## Funções como Parâmetro:

Uma função pode ser utilizada por outra função como parâmetro, nesse caso o valor retornado por uma função é utilizado por uma segunda função, 
é bom ficar atento, para que na chamada da função de alta ordem, sejam passados os agumentos  de forma correta


**Exemplo:**
```python
def soma(a, b):
  return a + b

def quadrado_soma(soma):
  return soma ** 2

print(quadrado_soma(soma(3, 4)))

def par_impar(quadrado_soma):
  if quadrado_soma % 2 == 0:
    return "Par"
  return "Impar"

print(par_impar(quadrado_soma(soma(3, 4))))
```
---


## Função Lambda:

Podemos definir uma função lambda como uma função não nomeada de linha única que segue  seguinte estrutura  ` variável = lambda: parâmetro: retorno`

**Exemplo:**
```python

quadrado = lambda num : num ** 2

print(quadrado(2))

soma = lambda a, b: a + b     #if a > b else a
print(soma(1, 2))

mai = lambda word: word.upper()

print(mai('evaldo'))

```

---
:house: [HOME](https://github.com/Evaldo-comp/Python-Mombaca)

---
