* have python installed
* have mysql installed

create a new virtal environment

```
$ python3 -m venv nameofthevirtualenvironment

```

activate the virtual environment

```
$ source virt/Scripts/activate

```
install django

```
$ pip install django

```

install the mysql-django connector

```
$ pip install mysql-connector-python

```

or

```
$ pip3 install mysql-connector

```

run mydb.py file to create the database

```
$ python mydb.py

```

migrate the database

```
$ python manage.py migrate

```

create a admin account

```
$ python manage.py createsuperuser

```

run the server

```
$ python manage.py runserver

