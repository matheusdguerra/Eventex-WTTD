# Eventex

Sistema de eventos encomendado pela Morena
https://eventex-matheusguerra.herokuapp.com/

## Como desenvolver

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env.
6. Execute os testes.

```console
git@github.com:matheusdguerra/Eventex-wttd.git
cd wttd
.\.wttd.\Scripts\activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
manage test
```

## Como fazer deploy

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False.
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`contrib\secret_gen.py`
heroku config:set DEBUG= False
# Configura o email
gith push heroku master --force
```

