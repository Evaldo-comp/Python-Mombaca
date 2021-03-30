# Aula 11: POO - Herança

## Herança:

Herança é um dos conceitos mais importantes da Programação Orientada a Objetos, a utilização de herança melhora a escrita do código, evitando reescrita 
de atributos e métodos que podem ser compartilhados, de classes mais generalistas para outras mais específicas. Uma classe mais generalista pode compartilhar 
seus atributos e/ou métodos com classes mais específicas.

Para facilitar o entendimento podemos fazer uma analogia. 

> Pessoas:

>> Profissionais de Saúde

>>> Médico

>>>>Pediatra


No exemplo apresentado, a classe Pessoa é a mais generalista, a cada nível que descemos nós vamos especificando um pouco mais , podemos dizer que Pessoas 
é a *Superclasse* e as demais são as *subclasses*, diferentemente do que o nome pode te levar a pensar, uma *subclasse* não é menos eficiente do que uma 
*superclasse*, acontece ao contrário, uma *subclasse* é mais especializada, o que torna ela mais poderosa.

---

## Herança Simples:

Essa é basicamente o caso que tratamos até aqui, quando subclasses herdam atributos e métodos de uma única classe.

imagem

---

## Herança Múltipla:

 Acontece quando uma classe herda atributos e/ou metod de mais de uma classe, essa herança por sua vez pode ser caracterizada como direta ou indireta
 
 ---
 
 ## Derivação Direta:
  
Nesse caso a classe que herda, o faz diretamente da superclasse, sem intermediários.

```python

class Pai:

class Filho:

class Neto(Pai, Filho): # Herda Diretamente

```

## Derivação Indireta:

Na derivação indireta a herança ocorre com a ajuda de intermediários como podemos observar no exemplo.

```python

class Pai:

class Filho(Pai):

class Neto(Filho): # Herda indiretamente atributos e/ou métodos da classe Pai

```

---

## Implentando Herança na Prática:




