# Trabalho de redes - AB2
## Alunos: Jackson Barbosa da Silva e Samuel Lucas Vieira Lins Barbosa
## Curso: Ciência da Computação

### Sobre o projeto
Consiste de um cliente/servidor que julga algoritmos a partir de uma entrada e saída pré-estabelecidas no servidor (como os utilizados em competições de programação), de forma que o cliente envia seu código em C++ para o servidor, o servidor processa o arquivo, compila, executa e testa com o resultado esperado, feito isso ele devolve ao cliente o resultado da analise do seu código para os testes da questão.

## Instruções:

### Servidor

Para executar o servidor você deve usar o seguinte comando:
```sh
python3 server.py [host] [porta]
```
Ao executar o comando acima você irá se deparar com algo como a imagem abaixo.
![run_server](screenshots/run_server.png)

### Cliente

Para executar o cliente você deve usar o seguinte comando:
```sh
python3 client.py [host] [porta]
```

Onde *[host]* e *[porta]* devem ser o host e a porta do servidor
