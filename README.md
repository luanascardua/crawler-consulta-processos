<h1 align="center"> Consulta de Processos Jurídicos </h1>

<p align="center">
  Consulta de processos dos Tribunais de Justiça de Alagoas (TJAL) e Ceará (TJCE). 
<p>

## OVERVIEW
API que consulta e retorna dados de um processo em todos os graus dos Tribunais de Justiça de Alagoas (TJAL) e do Ceará (TJCE). <br>
Os dados são coletados por um crawler utilizando web scraping e o resultado é consultado pela API.


### API
A aplicação possui dois endpoints: *"/processo"* e *"/dadosProcessuais"*; <br>
O endpoint */processo* é usado para receber um json via método HTTP POST; <br>
O endpoint */dadosProcessuais* é usado para retornar dados coletados pelo crawler.

### CRAWLER
O crawler acessa os sites [TJAL](https://www2.tjal.jus.br/cpopg/open.do) e [TJCE](https://esaj.tjce.jus.br/cpopg/open.do) para consultar processos de 1ª e 2ª instância.
É necessário fornecer um número de processo - é retornado pela API; <br>
O crawler verifica a qual tribunal o número de processo pertence de acordo com o padrão cnj de numeração de processos jurídicos; <br>
Realiza a busca nos sites correspondentes de 1ª e 2ª instância; <br>
Ao final do processo é retornado um json com as informações coletadas.

#### dados coletados pelo crawler:
- classe
- área
- assunto
- data de distribuição
- juiz
- valor da ação
- partes do processo
- lista das movimentações (data e movimento)

## Stack
- [Python](https://docs.python.org/3.10/)
- [Selenium](https://www.selenium.dev/documentation/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)

## Installation
1. clone the repository
2. install required packages
3. run app

```
git clone https://github.com/luanascardua/crawler-consulta-processos.git
```

``` python
pip install -r requiriments.txt
```

*na raiz do projeto executar o comando:*
``` 
python app.py
```

## Execute
na raiz do projeto executar o comando:
```
python app.py
```

Ao executar o comando, o método *app.run()* é chamado para iniciar o app Flask num servidor local. A partir daí será possível acessar a aplicação pelo navegador ou alguma 
ferramenta que permite interagir com APIs, como [Postman](https://www.postman.com/) e [Insomnia](https://insomnia.rest/download). <br>
Endereço local: http://localhost:5000/.

É necessário fazer uma requisição via método HTTP POST para o endpoint **/processo* para receber um json contendo o número do processo. <br>
O json deve seguir a estrutura:
``` python
{
	"numero":"0710802-55.2018.8.02.0001"
}
```

O status da requisição dever retornar 200: *"POST /processo HTTP/1.1" 200*; <br>
Poderá ser feita uma nova requisção via método HTTP GET para o endpoint **/dadosProcessuais*; <br>
Feita a requisição o crawler irá iniciar e fazer a consulta nos sites de Tribunais de 1ª e 2ª instância; <br>
Será retornado um json com os dados do processo.

### Executar *apenas* o crawler

No arquivo *webcrawler.py* basta chamar a função *start_crawler* passando como argumento uma string contendo o número do processo. <br>
Executar na raiz do projeto:
```
python webcrawler.py
```

#### executar no modo interativo Python
```
python -i webcrawler.py
```
Ao executar o crawler com interpretador do python o objeto *driver* irá retornar como saída da função, possibilitando interagir com a página web pelo prompt de comandos, sendo útil para testes ou debug.
O objeto driver será retornado em caso de erro e ao finalizar a execução da aplicação.

Para sair do modo interativo python basta executar o comando:
```python
exit()
```

<br>

> Exemplos de processos:
``` python
{"numero":"0710802-55.2018.8.02.0001"},
{"numero":"0727328-63.2019.8.02.0001"},
{"numero":"0213467-51.2022.8.06.0001"},
{"numero":"0008002-09.2016.8.06.0081"}
```
