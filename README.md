# Zerodha Assignment
This project includes following apps.
* bhav 
    - Downloads the equity bhavcopy zip at 18:00 IST for the current date.
    - Extracts and parses the CSV file in it.
    - Writes the records into Redis.
    - API to access the data

* frontend 
    - Frontend with a search box that allows the stored entries to be searched by name 
    - a table of results and optionally downloads the results as CSV

##[DEMO](http://13.232.203.109/)


## Prerequisites

### Setting up Python3 and virtual environment:

#### Step 1:
Set up python3 on the system

#### Step 2:
Set up virtual environment
* [Link for step 1 and 2 (Ubuntu 18.04)](https://linoxide.com/linux-how-to/setup-python-virtual-environment-ubuntu/)
* [Link for step 1 and 2 (Windows)](https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/)

#### Step 3:
Install all dependencies  
```
$ pip3 install -r requirements.txt
```

To run the project on the development server:
```
$ python manage.py runserver
```
To start the cron job:
```
$ python manage.py installtasks
```

[A Django settings file contains all the configuration of your Django installation.](https://docs.djangoproject.com/en/3.0/topics/settings/)

Deploying Django to production:

[Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04)
