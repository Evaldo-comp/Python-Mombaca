



#  Repetições:


- Repetições
  - Contadores
  - Acumuladores
  - While
  - for

---

## Repetições:

As repetições servem para executar determinadas instruções até que um elemento atinja um valor predeterminado pelo desenvolvedor. 
A primeira estrutura de reptição que vamos ver é o `while`, que possui a seguinte estrutura:
```python
while<condição>:
    bloco
```
Exemplo de implementação da estrutura:
```python
x = 1
while x <= 3:
    print(x)
    x = x + 1
 ```
 
**Contadores:**
Para que uma estrutura de repetição exiba somente a quantidade certa de operações desejadas pelo desenvovledor, utiliza-se uma variável que faz o controle destas repetições, essa variavel é incrementada ou decrementada a cada execução e chama-se **Contador**

## Break:
Nem sempre queremos esperar que o controlador estoure o valor limite e force a saída  do loop, pode ser que seja necessário parar as repetições com outra condição, para isso utilizados o break

**Exemplo:**
```python
alunos = ["Marcelo", "Vanessa", "Edinara", "Lucas", "Jonas"]
cont =0
while(cont <= (len(alunos))):
 
  if alunos[cont] == "Edinara":
    print(f"{alunos[cont]} Faltou")
    break 
  print(f"{alunos[cont]} Presente")
  cont+=1
```
**Continue:**
O continue é utilizado quando queremos que o loop ignore uma iteração mas não pare a execução, então ele ignora a interação indicada e pula para a próxima


**Exemplo:**
```python
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
```


**Acumuladores:**

As estruturas de repetição também utilizam **Acumuladores**, a principal diferença entre os acumuladores e os contadores, é que no primeiro o valor adicionado é variável, já no segundo, o valor incrementado ou decrementado é constante.

**Exemplo:**
```python
n = 1
soma = 0
while n <= 10:
  x = int(input(f"Digite o {n} número\n "))
  soma = soma + x
  n = n + 1
print(f"Soma: {soma}\n")
```

---

## FOR: 
O for é uma estrutura de repetição que no python é mais comumente utilizada para manipular percorrer listas:

```python
lista = [1, 2, 3, 4, 5]
for i in lista:
    print(i)
```
O ***for*** não substitui o ***while*** em qualquer implementação. Como já foi dito, o for é mais utilizado pra trabalhar com listas, já o `while` utiliza-se normalmente quando não sabemos a quantidade de vezes que a repetição irá ocorrer.

**range:**

Algumas funções embutidas funcionam muito bem com o for, como é o caso do `range()`. Essa função integrada da linguagem retorna um intervalo.

```python
'''for i in range(10):  # um unico argumento, esse argumento será o limite  e o primeiro será zero
  print(i)

for i in range(2, 10):  # dois  argumentos, o primeiro argumento será o inicio e o segundo será o fim
  print(i)

for i in range(2, 10, 2):  # ao adicionar três argumentos, o terceiro é o intervalo de um item a outro dentro do intervalo
  print(i)
```


**Exemplo: Buscar um elemento em uma lista**
```python
 L = ["Marcelo", "Dayane", "Lucas"]
 p = input("Digite o nome de uma aluno")
 indice = 0
 for i in L:
   if i.upper() == p.upper():
     indice +=1
     print(f"Elemento {i} econtrado no indice {indice}")
     break
   else:
      print(f"elemento não encontrado ")
```

---

:house:[Home](https://github.com/Evaldo-comp/Python-EEEP-JJLG/blob/main/README.md)

---

