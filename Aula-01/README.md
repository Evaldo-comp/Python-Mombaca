# Aula 01:
## O que é Python e porque Python?
Python é uma linguagem de progamação criada por [Guido van Rossum](https://pt.wikipedia.org/wiki/Guido_van_Rossum) em 1991, ela é uma linguagem interpretada, Orientada a Objetos e fortemente tipada, tá,  mais o que isso quer dizer? Quer dizer que Python necessita de um cast para fazer a conversão de tipos de dados caso necessário, esse casting não se faz necessário em linguagens fracamentes tipadas, Python também  é uma linguagem dinâmica, que não te obriga a colocar o tipo de dado que uma variável deve suportar, a alinguagem reconhece o tipo de dado e já reserva a quantidade de memória necessa´ria para ele.  Python também é uma linguagem multiplataforma de alto nível que te permite executar operações muito complexas em poucas linhas, isso torna sua escrita mais fácil de compreender, por isso Python vem ganhando espaço não só no mercado de trabalho com aplicações desktop, Front e Back end, mas também nas universidades por ser uma linguagem de simples aprendizagem mas que também obriga o aluno a codificar de forma limpa e organizada. Python é o que podemos chamar de linguagem de propósito geral e tem uma comunidade internacional e nacional bastante ativa, através dos links abaixo você pode conferir  onde a comunidade brasileira de Python está atuando, através destes sites você pode aprender mais, se enturmar, compartilhar e fortalecer a comundiade. **Aproveite!!!!**

 * [CPython Brasil ](https://python.org.br/)
 * [PayLadies Brasil](https://brasil.pyladies.com/)
 
 ---
 
## Preparação de Ambiente:

**Verificação da versão instalada:**
Primeiramente deve-se verificar se não há nenhuma versão instalada no seu computador com o comando ```python --version``` no terminal. A versão que será utilizada, será 3.9 ou 3.8.

**Instalação do Python:**

Normalmente distros linux já vem com o Python pré instalado, mas caso você não tenha ainda a versão mais recente na sua máquina siga os passos seguintes para realizar a instalação:

**1. Primeiramente adicione o repositório do programa:** Digite a seguinte  linha de comando no seu terminal.
```
 sudo add-apt-repository ppa:deadsnakes/pp
```
**2. Atualize o gerenciador de pacotes:** 
```
 sudo apt-get update
```

**3. Instalando o Python:** 
```
sudo apt-get install python3.8
# você pode alterar a versão conforme a disponibilidade da mesma
```

**4. Para desinstalar, adicione as duas linhas seguintes:** 
```
sudo add-apt-repository ppa:deadsnakes/ppa -r -y
sudo apt-get upgrade

```
---
## Instalando a IDE:
A Interface de Desenvolvimento que iremos utilizar é o Visual Studio Code. Em algumas distros Linux ela pode aparecer no repositório de programas nativos do Sistema, caso isso não aconteça, não precisa perder a cabeça, basta acessar o link abaixo que lá você vai encontrar vários caminhos para a instalação em várias distribuições diferentes.<br>
[Instalação do VSCode](https://code.visualstudio.com/docs/setup/linux)

---

## Criando seu GitHub:

Nesta etapa você vai criar uma conta do **GitHub**, caso você já tenha uma, passe para a próxima etapa. 

Criando o repositório da nossa disciplina: Você irá criar um repostória para armazenar os conteúdos, listas e desafios que irá executar durante a disciplina. Tanto a criação de repositórios quanto a utilização de outras funcionaliddes mais especificas podem ser aprendidas lendo a documentação que você pode acessar no link abaixo.<br>
:link:[GitHub Docs](https://docs.github.com/pt/github/getting-started-with-github/quickstart)

---

## instalando o Git:
Para que você possa vincular sua IDE ao seu repositório remoto no GitHub, será necessário ter o Git devidamente instalado e configurado na sua máquina. Abra o terminal e digite a seguinte linha de comando ```git --version```, essa linha irá verificar se você tem alguma versão do Git instalado, caso tenha, ela retornará essa versão,caso contrário, apareceŕá alguma mensagem de erro, no segundo caso você terá que proceder com a instalação. Esse processo  pode ser verificado no link abaixo:

:link:  [Instalando o Git](https://git-scm.com/download/linux)

## Configurar seu nome de usuário no Git:

Uma das primeiras coisas que você deve fazer depois que instalar o Git, é configurar seu nome de usuário nom computador local, para isso, siga as instruções a seguir no link:<br>
:link:  [Configurando nome de Usuário](https://docs.github.com/pt/github/using-git/setting-your-username-in-git)<br>

## Configurando o endereço de E-mail:

Você irá precisar associar um endereço de e-mail ao seu Git para que seja possivel associar o GitHub ao seu repositório local, esse processo pode ser verificado no link que segue<br>
:link:  [Configurando endereço de E-mail](https://docs.github.com/pt/github/setting-up-and-managing-your-github-user-account/setting-your-commit-email-address)

---

## Vinculando VSCode ao GitHub:
Com o VSCode instalado e o repostório do GitHub criado, você vai vincular a sua IDE a sua conta no GitHub. O passo a passo desse processo está detalhado nos links que seguem:

:link: [Integrando VSCode ao Git: Ocean](https://www.digitalocean.com/community/tutorials/how-to-use-git-integration-in-visual-studio-code-pt)

:link: [Integrando VSCode ao Git: Microsoft](https://docs.microsoft.com/pt-br/learn/modules/use-git-from-vs-code/)

---

## Finalizando:
Como você pode notar, muitos dos links utilizados nessa preparação, são links para documentação oficial das ferramentas. Crie o hábito de visitar a documentação oficial, pois é lá que podemos verificar updates oficiais, detalhes da ferramenta ou linguagem e etc. Ao fim dessa aula você deverá ter feito o seguinte:
1. Python instalado
2. Visual Studio Code Instalado
3. Git instalado
4. Conta no GitHub Criada
5. Repositório pessoal da disciplina criada e clonada
6. Git configurado
7. Integração entre Git e Vscode realizada

 ### Referências
 > [https://www.devmedia.com.br/guia/python/37024](https://www.devmedia.com.br/guia/python/37024)
 
 > [https://python.org.br/](https://python.org.br/)
 
 > [https://docs.github.com/pt](https://docs.github.com/pt)
---
:house: [Home](https://github.com/Evaldo-comp/Python-Mombaca)
---
