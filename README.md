# Django Dataset API:
This solution was developed using Python 3 and Django with Django Rest Framework and sqlite.
The main purpose with it was to show how it's easy and simple to build an application with Django.


# Installing Application by docker image:
```
firstly 
 
$ cd dataset-api/

and then
 
$ docker build -t dataset-api .

after that

$ docker run --name datasetapi -p 8000:8000 -d datasetapi
```

# Installing Python on OSX (Pure Python):
Please, first of all check if Python is installed in your system:

```
$ which python

or

$ which python3
```

If this command returns /usr/bin/python it means that python is already installed in your system.

# Installing Python
Please, to install python follow this link: http://programwithus.com/learn-to-code/install-python3-mac/

# Installing pip
```
$ sudo easy_install pip
```
Now please, install the third-party
```
$ pip install -r requirements.txt
```
# Running the application 
Open your command line and go through the main application directory
```
$ cd ../dataset-api
$ python manage.py runserver
```

# Running tests
```
$ python manage.py test  
```

# API documentation
After you have started the application, you'll be able to open your browser and access this address below:

<a href='http://localhost:8000'>http://localhost:8000</a>

