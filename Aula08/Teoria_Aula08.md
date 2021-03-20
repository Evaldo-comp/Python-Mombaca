# Aula08 - Manipulação de Arquivos

O Python assim como diversas outras linguagens nos permitem manipular arquivos para que possamos ler dados, escrever e armazenar, cada linguagem se comporta
de uma forma diferente, algumas mais complexas, outras com processos mais automatizados. a manipulação de arquivos no Python deve seguir um cliclo, que
chamamos de cilco de vida do arquivo:

 - Criação
 - Operação
 - Fechamento
 
Primeiro o arquivo é criado ou arberto, em seguida é feita alguma operação(Pesquisa, filtragem, corte e etc), depois de ser utilizado o arquivo deve
ser fechado para que ele não continue consumindo memória, ou gere algum conflito na sua reutilização em uma operação posteior.

## Acesando um Arquivo:

A primeira coisa que devemos fazer para acessar um arquivo é abri-lo, informando o nome e o caminho do mesmo, o caminho só será necessário informar se o arquivo não
estiver na pasta onde o código que irá manipul-a-lo também se encontra.

Para abrir usamos a função `open`, essa função leva dois parâmentros, o nome e modo. O nome é o nome do arquivo, hooooo 🙃  e o modo é a operação que desejamos realizar 
com o arquivo, as operações podem ser as seguintes da tabela.

| Modo | Operações                                      |
|------|------------------------------------------------|
| r    | leitura                                        |
| w    | escrita, apaga o conteúdo se já existir        |
| a    | escrita, mas preserva o conteúdo se já existir |
| b    | modo binário                                   |
| +    | atualização(leitura e escrita)                 |



*OBS: A função open retorna uma objeto do tipo file*

### Criando umArquivo

Segue abaixo o exemplo da geração de um arquivo .txt, o formato pode ser alterado para .doc, .pdf e etc. Para realizar operações de busca e filtragem é interessante
utilizar arquivos .txt, porque ele não possue formatação. O exemplo que segue utiliza como operação o `w`, essa operação escreve um dado em um arquivo, se esse
arquivo não existir ele cria um, se ele existir ele sobrescreve.

```python
arquivo = open("numero.txt", "w") 

for linha in range(1, 101):
  arquivo.write(f"{linha}\n")
arquivo.close()
```

---
> 🗒️: Pratica01:
> Gere um arquivo cadastro que receba nome e idade do usuário. fique a vontade para inserir mais dados
---

## Lendo um Arquivo:

Depois de criarmos um arquivo, vamos entender como funciona o processo para abrir e ler um arquivo. Agora vamos utilizar o modo `r` para leitura.
Aqui faremos uso do método `readlines()`, ele cria uma lista onde cada elemento é uma linha do arquivo

```python
# lendo um arquivo
arquivo = open("cadastro.txt", "r")

for linha in arquivo.readlines(): 
    print(linha)
arquivo.close()
```
### O uso do `with`:

Como o fechamento de arquivo é muito importante para a maniplação correta, o Python cria um bloco que contextulaiza e desobriga de chamar o método 
`close()` sempre que abrirmos um arquivo. Abaixo podemos  ver o mesmo o processo realizado no exemplo anterior, mas utilizando o `with`.

```python
with open("cadastro.txt", "r" ) as arquivo:
    for linha in arquivo.readlines():
        print(linha)
```
Ao encadearmos o with, podemos criar vários arquivos ao mesmo tempo com características diferentes:
```python
with open("impares.txt", "w") as impares:
    with open("pares.txt", "w") as pares:
        for n in range(0, 100):
            if n % 2 == 0:
                pares.write(f"{n}\n")
            else:
                impares.write(f"{n}\n")
```

---
## Operações com Arquivos:
Além de criar e manipular um arquivo, podemos simplismente abrir um arquivo existente para realizar algumas operações como por exemplo uma filtragem de dados.
O código que segue, abre um dos arquivos gerados anteriormente ("pares.txt") e gera outro arquivo apenas com números multiplos de 2 advindos desse arquivo original.

```python
# gerando um arquivo com base nos dois criados anteriormente
with open("multiplos_quatro.txt", "w") as multiplos4:
    with open("pares.txt") as pares:
        for l in pares.readlines():
            if int(l) % 4 == 0:
                multiplos4.write(l)
 ```
 
> 🗒️: Pratica02:
> Gere dois arquivos, um que tenha apenas números pares e outro com apenas números impares. Em seguida crie um novo arquivo que junte os dois(pares e impares).
---
Para que você consiga realizar processos de pesquisa e filtragem com uma quantidade maior de números, vamos utilizar um arquivo de texto com nomes coletados
originalmente neste  [repositório](https://github.com/emersonsoares/SampleDataGenerator/edit/master/SampleDataGenerator/Resources/nomes.txt), os nomes foram salvos
em arquivo.txt que pode ser acessado [aqui](https://github.com/Evaldo-comp/Python-Mombaca/tree/main/Aula08).

Sehuem alguns exemplos de operações realizadas com arquivo.

Filtragem de nomes com uma quantidade limite de letras
```python

nomes = open("nomes.txt")

for line in nomes:
    word = line.strip()
    if len(word)<=3:
        print(word.upper())
  ```
Filtragem de nomes por inicial:

```python
nomes = open("nomes.txt")

for line in nomes.readlines():
    if line[0] == "A":
        print(line.upper())
nomes.close()
```
---
## geração de Arquivos HTML:

HTML é uma linguagem de marcação, utilizada para estruturar páginas web, para escrevermos uma página web podemos utilizar um editor de texto simples 
apenas escrevendo a seguinte estrutura.
```html
<!DOCTYPE html>
<html lang="pt-BR">

  <head>
    <meta charset= "utf-8">
    <title>Titulo da Página</title>
  </head>

  <body>
    Olá!
  </body>
</html>
```

Para gerarmos um arquivo semelhante ao anterior utilizando Python, primeiramente vamos criar um arquivo com a função `open()`
mas aqui vamos utilizar a propriedade `encoding` que vai definir o padrão de rederização de cacateres que o brownser vai usar.

```python
# gerando HTML com python
with open("index.html", "w", encoding="utf-8") as index:
    index.write("""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
       <meta charset= "utf-8">
       <title>Titulo da Página</title>
    <head>
    <body>
    Olá!
    </body>
    </html>
    """)
```
A criação da estrtura padrão do HTML com Python não vai me trazer grandes benefícios a primeira vista, mas quando integramos  o Python juntamente com HTML
podemos ter ganhos incríveis na escrita de estruturas que poderia se tornar muito massante se fossemnos escrever linha por linha em HTML.
O próximo exemplo insere um dicionário dentro de um arquivo HTML. Observe que a lógica de inserção do dicionário tem apenas 4 linhas de código
e a estrutura criada dentro do HTML são mais de  de 10 linhas.
```python
filmes = { "drama":["Cidadão Kane", "O Poderoso Chefão"],
 "comedia":["Tempos Modernos", "Desejo de Matar"],
  "ficção":["Ad Astra", "Interestelar"],
   "guerra" : ["1937", "Platoon", "Lágrimas do Sol"] }

with open("filmes.html", "w", encoding="utf-8") as filme:
    filme.write("""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
       <meta charset= "utf-8">
       <title>Filmes</title>
    <head>
    <body>

    <h1 align="center"> Filmes</h1>
         """)

    for c, v in filmes.items():
        filme.write(f"<h1>{c}</1h>\n") 
        for e in v:
            filme.write(f"<h3>{e}</h3>\n")
    filme.write("</body></html>")
 ```
---
:house: [HOME](https://github.com/Evaldo-comp/Python-Mombaca)
---







