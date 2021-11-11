
# CodMorse

CodMorse é um sistema que recebe um código morse e converte ele em texto.

![enter image description here](https://i.pinimg.com/originals/69/db/da/69dbdaab54a29c88f1231720b150a139.jpg)
  

Para obter o projeto para sua máquina, execute no seu terminal o comando abaixo:
```
git clone https://github.com/Jerffeson/CodMorse.git
```


# Backend

## Dependências

  
- [Python 3.9.8](https://www.python.org/downloads/release/python-398/) ou superior

- Crie um ambiente virtual para manter as dependência do projeto isoladas do escorpo global do Python:
			```
		python3 -m venv {PASTA_DO_PROJETO}/venv
		```

- Ative o ambiente virtual com o comando abaixo:

	```
	// WINDOWS
	{PASTA_DO_PROJETO}\venv\Scripts\activate
	// LINUX
	source {PASTA_DO_PROJETO}/venv/bin/activate
	```

- Agora instale o Django e DRF com os seguintes comandos:

	```
	pip install Django==3.2.9;
	pip install rest_framework;
	```

  
## Serviço em localhost

Para subir o serviço localmente, use os comandos abaixo. Certifique-se de alterar PASTA_DO_PROJETO para o caminho do projeto na sua máquina.

```
cd {PASTA_DO_PROJETO}\CodMorse\appserver
python manage.py runserver {SEU_IP}:8000
```

Requisição para conversão através da API

```

curl --location --request GET 'http://localhost:8000/api/morse?codMorseParam=.-' \
--header 'Content-Type: application/json' \


 
Response

code - 200
{
	"data": "H"
}
```

  
  

# Frontend


## Dependências

- Node >= v15.11.0

 - Com Nodejs já instalado em sua máquina, entre no diretório do projeto e instale as dependências:
	```
	cd {PASTA_DO_PROJETO}\CodMorse\appfront;
	npm install;
	```
- Inicie o serviço com o seguinte comando:
	```
	npm start;
	```  
  
  

# NGINX

Para evitar problemas de CORS, adicione as configuração a seguir ao arquivo .conf do serviço Nginx:

```
// nginx.conf ou *.conf
location / {
	proxy_pass http://{SEU_IP}:3000/;
}

location /api {
	add_header 'Access-Control-Allow-Origin' '*';
	add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
	proxy_pass http://{SEU_IP}:8000/api;
}
```


## Acesssando localmente
Após o comando npm para iniciar o react, será aberto uma aba no localhost na porta **3000** automaticamente. Feche essa aba e acesse o sistema através do http://localhost *sem a porta*.  O Nginx deverá realizar o proxy para o serviço Node e API em Python das requisições.