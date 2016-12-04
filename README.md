# UnBSolidaria

####Pré-requisitos: 

 - MySQL (```sudo apt-get install build-essential python-dev libmysqlclient-dev``` )
 - Pyhton 2.7.12

####Instalação:

 1. ``` mkdir unbsolidaria ```
 2. ``` cd unbsolidaria ```
 3. ``` virtualenv . ```
 4. ``` git clone https://github.com/RafaelDiasSilveira/UnBSolidaria.git```
 5. ``` source bin/activate ```
 6. ``` cd UnBSolidaria ```
 7. ``` pip install -r requirements.txt ```
 
 Caso você já tenho um banco criado, drope o banco e crie novamente.
 
 8. ``` python manage.py makemigrations ```
 9. ``` python manage.py migrate auth ```
 10. ``` python manage.py migrate ```
 11. ``` python manage.py runserver ```
 
####Observações:
Ao criar o banco de dados MySQL (supondo que seu usuário e senha sejam: root/root), crie com o seguinte comando:
 ``` CREATE DATABASE unbsolidaria CHARACTER SET utf8; ```   

