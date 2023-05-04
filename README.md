# MVP 1 - Backend

Este projeto (`KCO - kitchen cabinet organizer`) foi criado com a ideia de fazer um site que possibilitasse a organização de armários da minha casa, com um catálogo de itens e gestão de contéudo de cada armário.  
O conteúdo deste repositório refere-se ao backend do site, que foi escrito utilizando o framework `Flask` (`Python`) para a configuração das rotas da API e `SQLite` como base de dados.

## Estrutura do projeto

Este projeto está organizado na seguinte maneira:
```
.
├── app.py
├── logger.py
├── requirements.txt
├── .venv
├── database
├── db
│   ├── database.sql
│   └── KCO-ER-diagrama.jpeg
├── log
├── model
├── schemas
````
O script `app.py` é o script principal que executa a aplicação. O script `logger.py` é o script que contém definições para a utilização do logger e o arquivo `requirements.txt` é onde estão descritas todas as dependências do projeto.  

A pasta `.venv` não está no repositório mas faz parte do projeto, isto porque é extremamente recomendado a presença de um ambiente virtual dentro do projeto para lidar com as dependências locais.  

A pasta `db` contém os arquivos gerados na fase de modelação do banco de dados: o diagrama entidade relacionamento (`KCO-ER-diagrama.jpeg`) e o script sql que foi gerado para testar a base de dados (`database.sql`).

As pastas `database` e `log` são geradas automaticamente, sendo que a primeira armazena o nosso banco de dados sqlite e a segunda armazena os logs gerados pelo logger.

As pastas `model` e `schemas` são as classes mapeadas do banco de dados (model) e seus respectivos schemas (schemas).

## Instalação

Antes de rodar o projeto, é preciso ter as dependências instaladas no seu ambiente. para isso, use o comando abaixo:

```
pip install -r requirments.txt
```

É preciso rodar este comando na raíz do projeto, pois é onde o arquivo `requriments.txt` se encontra. Após baixar todas as dependências, podemos seguir para a próxima etapa.

## Execução

Para rodar a API criada, basta executar o seguinte comando:

```
flask run --host 0.0.0.0 --port 5002
```

Sendo que o parâmetro `--host 0.0.0.0` refere-se ao localhost e o parâmetro `--port 5002` refere-se à porta que será associada o serviço. Após rodar o comando, será possível abrir a url `http://localhost:5002` no seu browser para visualizar a documentação da API.  

Escolha a documentação mais familiar para você (Swagger, ReDoc ou RapiDoc) e explore as rotas da API.


## **Importante**

Para esta primeira fase do MVP apenas será possível realizar a gestão de itens no front end, por isso é fortemente recomendado o cadastramento de alguns tipos (`Type`) e armários (`Cabinet`) para o funcionamento correto da aplicação. Neste repositório já está armazenada uma base de dados preparada para a execução da aplicação frontend.
