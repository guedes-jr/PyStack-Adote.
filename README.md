# PyStack-Adote.

ative o ambiente de desenvolvimento
```sh
#Ativar
	# Linux
		source venv/bin/activate
	# Windows
		venv\Scripts\Activate

# Caso algum comando retorne um erro de permissão execute o código e tente novamente:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Agora vamos fazer a instalação do Django e as demais bibliotecas:
```sh
pip install django
pip install pillow

```

Criar projeto com o django
```sh
django-admin startproject adote .
```

Criar um novo app no projeto
```sh
python manage.py startapp usuarios
```

Para iniciar o servidor 
```sh
python3 manage.py runserver
```

```sh
python3 manage.py makemigrations
```

```sh
python3 manage.py migrate
```

```sh
python3 manage.py createsuperuser
```