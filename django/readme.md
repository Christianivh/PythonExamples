

# Tutorial de Django, iniciando con una EC2 Linux de AWS

Este ejercicio se basara en la documentacion de la pagina de django, para mayor informacion puede ingresar a la pagina para enconrar mas informacion relacionada a django.

https://www.djangoproject.com/
https://docs.djangoproject.com/en/5.0/intro/tutorial01/


Esta ayuda es para utilizar Django en maquinas tipo AWS EC2, estas tienen por defecto ya instalado Python3.9, sin embargo falta instalar algunas aplicaciones y librerias que vamos ir desarrollando.


### Instalacion de python-pip

```
sudo yum install python3-pip
```


### Instalar la libreria de Django.

Django no deja de ser una libreria que posee su propio framework para trabajar aplicaciones web.


```
pip install Django
```


### Para inicializar un proyecto se debe ejecutar las siguiente instruccion, siendo "mysite" el nombre de la aplicacion web que desean generar.

```
django-admin startproject mysite
```

### EC2 consideraciones

En las consideraciones de la maquina EC2, debe permitir que esta en una VPC publica, y que esta tenga acceso hacia el puero 5000 en el Inbound del SecurityGroup de la EC2.

Adicionalmente se debe configurar en el proyecto, el modulo setting, ubicar la linea donde se encuentre ALLOWED_HOST y reemplazar el listado vacio por uno que contenga la IP Publica de la maquina EC2.

```
cd mysite
nano mysite/settings.py 
#  add IP Public in ALLOWED_HOST=['##.##.##.##']
```

# Iniciando la APP de Django

Una vez configurado ya todo ya puede lanzar su proyecto demo django. 
```
python3 manage.py runserver 0.0.0.0:8000
```


bye



```
#!/bin/bash
yum update -y
yum install -y httpd
sudo systemctl start httpd.service
sudo systemctl enable httpd.service
sudo echo "BPC from $(hostname -f)" > /var/www/html/index.html
```
