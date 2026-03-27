# Bookstore

### O projeto bookstore é um sistema back-end completo para gerenciamento de livraria desenvolvida com Python e Django. Sistema que demonstra as melhores práticas de desenvolvimento de APIs, tendo autenticação, paginação e container com Docker.

## Tecnologias

* **Django 6.0**: Framework principal para o desenvolvimento do backend.
* **Django REST Framework (DRF)**: Conjunto de ferramentas potente para a construção de APIs Web.
* **Psycopg2**: Adaptador do banco de dados PostgreSQL para Python.
* **Gunicorn**: Servidor HTTP WSGI para rodar a aplicação em produção.
* **WhiteNoise**: Permite que a aplicação sirva seus próprios arquivos estáticos (CSS, imagens).
* **Django Extensions**: Coleção de extensões customizadas para acelerar o desenvolvimento.
* **Django Debug Toolbar**: Painel para depuração e análise de performance das requisições e queries SQL.
* **Flake8**: Ferramenta de linting para garantir que o código siga as boas práticas (PEP 8).

## O que o projeto propõe

* Arquitetura back-end escalável
* CRUD completo com gerenciamento de produtos, categorias e pedidos
* Paginação
* Autenticação
* Containerização com Docker
* Testes automatizados com Pytest e Factory Boy
* Banco de dados PostgreSQL