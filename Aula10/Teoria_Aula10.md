# Aula 10 - Orientação a Objetos

## Conceitos Iniciais

## Paradigma:

É uma metodologia ou a representação de um padrão. 
Até esse momento utilizamos um paradigma estrutural onde os comandos são executados de forma sequencial e linear, como utilizamos funções desde o início, 
nosso código não é 100% linear, ele possui algumas pitadas do paradigma funcional, pois as funções meio que quebram essa linearidade na hora de executar.

O Python possui uma curva de aprendizado suave, porque ele permite que iniciemos o aprendizado na linguagem com um paradigma procedural, e a imersão na 
paradigma orientado a objetos não trás grande mudanças no comportamento e nem na escrita, isso não ocorre em linguagens exclusivamente OO como Java.

---
## Paradigma Procedural:

O paradigma orientado a procedimentos parte do princípio que os estados dos dados são compartilhados pelas funções e subrotinas. Por exemplo, 
uma função toma uma variável como argumento, processa e devolve para que ela possa ser utilizada em outra função ou simplesmente para ser visualizada pelo usuário.
O que interessa é a mensagem recebida e enviada, e não como determinado objeto executou aquela operação.

---

## Paradigma Orientado a Objetos:
Na Orientação a Objetos existe uma dinâmica onde os obejtos  se comunicam entre si por meio de mensagens de suas interfaces. a ideia é simular o mundo real
através de rotinas

---

## Classes: 

É um conjunto de atributos e funções que servem para gerar objetos, a classe é geneŕica e serve como um molde. 

## Objeto:  

É uma instância de uma classe, ou seja, ele possui todas as características da classe, mas os valores podem ser diferentes. 

## Atributos:

São as características que essa classe  vai compartilhar com seus objetos.

## Métodos: 
É o comportamento do objeto, uma ação que pode ter ou não uma entrada.

---

## Implementando uma classe:

## Criando uma classe:

```python

class Carro:
  pass

c1 = Carro() # Aqui um objeto é instanciado
c2 = Carro()
```

---

## Inserindo atributos na classe

```python
class Carro:
  marca = "Fiat"
  cor = "Vermelho"

c1 = Carro()
c1.marca
c1.cor
```

---

## O método construtor:

O método `__init__` é um construtor padrão do python, ele inicia todos os atributos no momento da instanciação da classe.

```python
class Carro:
  def __init__(self, marca, cor, modelo): 
      self.marca = marca
      self.cor = cor
      self.modelo = modelo
      

c1 = Carro("Fiat", "Azul", "D20")
c1.marca
```

---

## Adicionando Métodos:

O método inserido abaixo, não possui nenhuma entrada, serve apenas para imprimir os atributos do objeto que o invoca.

```python
class Carro:
  def __init__(self, marca, cor, modelo): 
      self.marca = marca
      self.cor = cor
      self.modelo = modelo
      



  def mostrar_detalhes(self):
    print(f"""
           Marca: {self.marca}
           Cor: {self.cor}
           Modelo: {self.modelo}
          """)

c1 = Carro("Fiat", "Azul", "D20")
c2 = Carro("Toyota", "Vermelho", "H20")
c1.mostrar_detalhes()
c2.mostrar_detalhes()
```

--- 

## Métodos com entrada:

O método anterior não recebia nada como parâmetro, agora vamos criar um método que recebe um dado para que seja usado no seu interior.
O método acelerar irá recebar um inteiro que representa o acréscimo de velociade que o carro irá acelerar se o motor estiver ligado.

```python
class Carro:
  def __init__(self, marca, cor, modelo, sitMotor = True, velocidade = 0): 
      self.marca = marca
      self.cor = cor
      self.modelo = modelo
      self.sitMotor = sitMotor
      self.velocidade = velocidade
      



  def mostrar_detalhes(self):
    print(f"""
           Marca: {self.marca}
           Cor: {self.cor}
           Modelo: {self.modelo}
          """)
          
  def acelerar(self, Acr_vel):
    if self.sitMotor == False:
      print(f"Você não pode acelerar porque o carro está desligado")
    else:
      self.velocidade += Acr_vel
      print(f"Velocidade: {self.velocidade} Km/h")



c1 = Carro("Fiat", "Azul", "D20")
c2 = Carro("Toyota", "Vermelho", "H20")
#c1.mostrar_detalhes()
#c2.mostrar_detalhes()
c1.acelerar(3)
c1.acelerar(3)
```

Mais métodos podem ser adicionados a essa classe para automatizar algumas operações, fica aí o desafio.

---
:house:[Home](https://github.com/Evaldo-comp/Python-Mombaca)
---
  



