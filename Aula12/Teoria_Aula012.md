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

E AGORA?

Python é uma linguagem muito poderosa e versátil, fácil de ler e de aprender, por isso é utilizada nos mais diversos campos de conhecimento, como por exemplo:

NSA (Agência de Segurança Nacional ) Americana, que usa Python em análise e criptografia de inteligência
BitTorrent -  É baseado em Python
Google e Youtube usam Python dentre outras linguagens

Onde Python pode ser utilizado?

AI:
O Python é utilizado para construção de redes neurais, essas redes tentam emular o cérebro humano e ensinar máquinas a se comportarem com base na análise de exemplos

Cálculo de rotas de aviões
Aplicativo clínico AICure

Recursos Python para aprendizagem de máquina:

Biblioteca KERAS : Biblioteca de rede neural de código Aberto
 https://keras.io/

TensorFlow: Também é uma biblioteca de código aberto voltada para ML https://www.tensorflow.org/?hl=pt-br

PyTorch: Biblioteca para ML baseada na Torch desenvolvida inicialmente pela equipe de IA do Facebook
 https://pytorch.org/

Theano: Theano é uma biblioteca Python e um compilador de otimização para manipular e avaliar expressões matemáticas, especialmente aquelas com valor de matriz
https://github.com/Theano/Theano

Criando bots
Os bots servem para automatizar tarefas maçantes e repetitivas na web, podem servir desde contas fakes no twitter para inundar como algum conteúdo ou subir alguma hashtag, como para atendimento ao cliente  nos SAC’s.

Como principais ferramentas, temos:

Python- rtmbot: https://github.com/slackapi/python-rtmbot
Errbot:  https://github.com/errbotio/errbot

Python na WEB

Python também é utilizado para desenvolvimento web, ele roda no backend como apoio a alguma outra tecnologia, segue alguns exemplos:

Pyramid: um framework python para aplicações web
https://trypyramid.com/

PyJs: É uma ferramenta que permite que você escreva seus códigos javascript  em python,
http://pyjs.org/

Django: É um framework escrito em Python que encoraja o desenvolvimento rápido e limpo
https://www.djangoproject.com/

Python na mineração de DAdos:
A mineração de dados é a análise de um banco extenso de dados para prever ou simular algum comportamento, a mineração pode envolver desde análise de comportamento de usuários em redes sociais até análise de imagens de crimes.
Recursos:

numPy: estrutura focada na realização de cálculos numéricos em python
https://numpy.org/

SciPy: modulo para matemática, ciência e engenharia
https://www.scipy.org/

Python e a interface de usuário(GUI)

Python não é só terminal, é possível criar aplicações com interface que interagem diretamente com o usuário através de janelas botões e etc, para isso temos os seguintes recursos

Tkinter: É um interface embutida da linguagem, já vem na instalação padrão do Python

PyGtk: Kit De ferramentas que ajudam na criação de interfaces
https://wiki.python.org/moin/PyGtk

KiVY: Uma biblioteca python especializada na geração de aplicativos móveis, mas que também serve para criação de interface de usuário inclusive multitoque
https://kivy.org/#home

Python e os Games

Python também pode ser usado para a criação de jogos e gráficos 3d, seguem abaixo alguns recursos utilizados nesse campo:

PyGame: 
Uma biblioteca que oferece muitos módulos que permitem a criação de jogos com python, é  mais indicada para quem está começando
https://www.pygame.org/news

Panda3D: Utilizado para renderização de objetos 3d e criação de jogos
https://www.panda3d.org/

Arcade: biblioteca python focada em jogos 2D
https://arcade.academy/


