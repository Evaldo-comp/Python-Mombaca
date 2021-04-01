# Aula12 - Encapsulamento


A Herança é um conceito fundamental para a Orientação a Objetos, mas a extensão do estado e comportamento de uma classe, pode dar a suas classes filhas , 
acesso a informações que não deveriam ser acessadas, por questões éticas e de segurança. Para evitar esse tipo de falha, utilizamos outro elemento fundamental
de POO, o ENCAPSULAMENTO, que consiste em você guardar, proteger alguns dados e comportamentos de outras entidades dentro do sistema. Para realizar esse 
encapsulamento mudamos o tipo de acesso aos métodos e atributos, tornando-os privados, em Python quando queremos indicar que um determinado atributo é 
privado inserimos um underline `_`,  no início dele.

```python
class Funcionario:
    def __init__(self, nome, mat, valorH, salario):
        self.nome = nome
        self.mat = mat
        self._valorH = valorH
        self._salario = salario		

```

Em Python não existe efetivamente métodos privados, o que existe é uma convenção que sinaliza um método ou atributo como provado, ou seja, 
não deve ser modificado fora do seu escopo, essa convenção trabalha basicamente com  `_` ou `__`, no primeiro caso um underline, serve apenas para 
indicar que aquele atributo ou método não deve ser modificado, fora de seu escopo. 
 
```python 
class Funcionario:
    def __init__(self, nome, mat, valorH, salario):
        self.nome = nome
        self.mat = mat
        self.__valorH = valorH
        self.__salario = salario		
```

Se utilizarmos dois underlines, o Python renomeia seu atributo ou método, fazendo com que ele seja acessado apenas seguindo a seguinte estrutura.`instancia._classe___atributo`

```python
class Funcionario:
   def __init__(self, nome, mat, salario):
       self.nome = nome
       self.mat = mat
       self.__salario = []
 
f = Funcionario("Edson", 1222, 200.0)
f.salario = 300
f._Funcionario__salario
```
---
Essa mesma lógica pode ser aplicada aos métodos.

```python
class Funcionario:
   def __init__(self, nome, mat, salario):
       self.nome = nome
       self.mat = mat
       self.__salario = []
 
   def passar_cartao():
     print(f' {self.nome} esta presente')
 
class RH(Funcionario):
 def __init__(self, nome, mat, salario):
   super().__init__(nome, mat, salario)
 
 def __contratar(self, nome):
     print(f"{nome} está contratado")
 
class Porteiro(RH, Funcionario):
 def __init__(self, nome, mat, salario):
   super().__init__(nome, mat, salario)
  
 
f = Funcionario("Edson", 1222, 200.0)
f1 = Porteiro("Jose", 222, 300.0)
f1.contratar("Andre")
 
```
No exemplo acima temos uma herança múltipla na classe Porteiro que herda RH e Funcionario, isso consequentemente faz com que a classe Porteiro
consiga manipular o método `contratar()`, isso não devia ser possível, tendo em vista que a função de contratar não desrespeito a essa classe, 
no exemplo foi utilizado por convenção os dois underlines, mas há outra solução, podemos sobrescrever o método, também chamado de override, observe.



```python
class Funcionario:
   def __init__(self, nome, mat, salario):
       self.nome = nome
       self.mat = mat
       self.__salario = []
 
   def passar_cartao():
     print(f' {self.nome} esta presente')
class RH(Funcionario):
 def __init__(self, nome, mat, salario):
   super().__init__(nome, mat, salario)
 
 def contratar(self, nome):
     print(f"{nome} está contratado")
 
class Porteiro(RH, Funcionario):
 def __init__(self, nome, mat, salario):
   super().__init__(nome, mat, salario)
 
  def contratar(self, nome):
     print("Eu nao posso contratar")
 
 ```
 

Um novo método `contratar()` foi criado dentro da classe Porteiro, mas com um comportamento específico desta classe.

---
:house: [Home](https://github.com/Evaldo-comp/Python-Mombaca)
---

