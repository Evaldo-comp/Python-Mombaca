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

---
<h1 align= "center">
<img src = "https://github.com/Evaldo-comp/Python-Mombaca/blob/main/Aula11/img-2105f66f.jpg" width = "300px" height = "300px" align = "center">
</h1>
---

## Herança Múltipla:

 Acontece quando uma classe herda atributos e/ou metod de mais de uma classe, essa herança por sua vez pode ser caracterizada como direta ou indireta:
 
 ---
<h1 align= "center">
<img src = "https://github.com/Evaldo-comp/Python-Mombaca/blob/main/Aula11/heran%C3%A7a%20Multipla.PNG" width = "300px" height = "300px" align = "center">
</h1>
---
 
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

### Criando a SuperClase Funcionário:

```python
class Funcionario:
    def __init__(self, nome, mat):
        self.nome = nome
        self.mat = mat
```

Com a superclasse criada, vamos inserir alguns métodos

```python
class Funcionario:
    def __init__(self, nome, mat):
        self.nome = nome
        self.mat = mat
        
        
    def bater_cartao(self):
        print(f'{self.nome} está presente')
```

Em seguida vamos criar as subclasses que aleḿ de receber os atributos  da superclasse, podem possuir atributos próprios:
```python
class Funcionario:
    def __init__(self, nome, mat):
        self.nome = nome
        self.mat = mat
        
        
    def bater_cartao(self):
        print(f'{self.nome} está presente')
       
class RH(Funcionario):
    def __init__(self, nome, mat, relacao={}):
        super().__init__(nome, mat) # init da superclasse
        self.relacao = relacao  #atributo exclusivo da subclasse RH
        
 class Porteiro(RH, Funcionario):
    def __init__(self, nome, mat):
        super().__init__(nome, mat)
        
        
 class Financeiro(Funcionario):
    def __init__(self, nome, mat):
        super().__init__(nome, mat)
```
 
 
 Como podemos perceber, quando criamos uma subclasse, ela deve iniciar também o construtor da superclasse, indicando quais os atributos
 ela está herdando, e caso ela possua um atributo próprio, como é o caso da classe RH com seu atributo relação, ele deve ser declarado
 separadamente.
 
 Agora vamos incluir métodos próprios, ou seja, as subclasses além de herdar o método `bater_cartao()` da superclasse, também terão métodos 
 exclusivos.
 
 ```python
 class Funcionario:
    def __init__(self, nome, mat):
        self.nome = nome
        self.mat = mat
        
        
    def bater_cartao(self):
        print(f'{self.nome} está presente')
       
class RH(Funcionario):
    def __init__(self, nome, mat, relacao={}):
        super().__init__(nome, mat) # init da superclasse
        self.relacao = relacao  #atributo exclusivo da subclasse RH
        
    def contratar(self, nome, mat):
        if mat not in self.relacao:
            self.relacao[mat] = nome
            print(f'{self.relacao[mat]} Contratado')
        else:
            print("Contratação Inválida")
        
 class Porteiro(RH, Funcionario):
    def __init__(self, nome, mat):
        super().__init__(nome, mat)
        
    def autorizar_entrada(self, mat):
        if mat in self.relacao.keys():
            print("Pode entrar")
        else:
            print("Espere")
            
 class Financeiro(Funcionario):
    def __init__(self, nome, mat):
        super().__init__(nome, mat)

    def pagar(self, valorH, diasT):
        pagamento = (valorH * 8) * diasT
        print(f"Você reberá R$ {pagamento} reais")
```
---

No código acima ocorre um caso de herança múltipla, onde a classe `Porteiro` herda a classe `Funcionario` e a classe `RH`. A herança possui muitos
benefícios e é indispensável na Programação Orientada a Objetos, mas ela deve ser utilizada com muito cuidado, pois a implementação inpensada pode 
distribuir poderes para classes que não precisão deles ou não deveriam ter, essa falha acontece na classe `Porteiro` que ao herdar os métodos da 
classe `RH` herda o método contratar, que não é uma função dela, ou seja, temos uma falha de implementação, isso pode ser resolvido mudando o perfil
de acesso do método, mas isso é assunto para próxima aula.

---
:house:[Home](https://github.com/Evaldo-comp/Python-Mombaca)
---


