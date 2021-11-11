# CodMorse
CodMorse é um sistema que recebe um código morse e converte ele em texto.

Para obter o projeto para sua máquina, execulte no seu terminal o comando abaixo:
```
git clone https://github.com/Jerffeson/CodMorse.git
```

# Backend
## Dependências

[Python 3.9.8](https://www.python.org/downloads/release/python-398/) ou superior

Crie um ambiente virtual para manter as dependência do projeto isoladas do escorpo global do Python
```
	python3 -m venv {PASTA_DO_PROJETO}/venv	
```
Ative o ambiente virtual com o comando abaixo: 
```
    WINDOWS
    {PASTA_DO_PROJETO}\venv\Scripts\activate
    LINUX
    source {PASTA_DO_PROJETO}/venv/bin/activate

```
Agora instale o Django e DRF com os seguintes comandos:
```
    pip install Django==3.2.9
    pip install rest_framework
```


## Serviço em localhost
Para subir o serviço localmente, siga os seguintes passos. Certifique-se de alterar PASTA_DO_PROJETO para o caminho do projeto na sua máquina.

```
cd {PASTA_DO_PROJETO}\CodMorse\appserver
python manage.py runserver
```
Requisição para conversão através da API
```
curl --location --request GET 'http://localhost:8000/api/morse' \
--header 'Content-Type: application/json' \
--data-raw '{
    "codMorseParam": "...."
}'

Response
code - 200
{
    "data": "H"
}
```


# Frontend
A aplicação frontend foi desenvolvida em Javascript, com Framework React
## Dependências
[Node]

```
cd {PASTA_DO_PROJETO}\CodMorse\appfront;
npm install;
```



# NGINX
Para evitar problemas de CORS, adicione a configuração a seguir ao serviço Nginx na sua máquina:
```
location / {
    proxy_pass http://{SEU_IP}:3000/;
}

location /api {
    add_header 'Access-Control-Allow-Origin' '*';
    add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
    proxy_pass http://{SEU_IP}:8000/api;
}
```