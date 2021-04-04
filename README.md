# Zerodha Assignment
This project includes following apps.
* bhav - This app provides a cron job to capture Bhav data every day, and API is provided to access data stored in Redis.
* frontend - Table to visualise data 

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

[A Django settings file contains all the configuration of your Django installation.](https://docs.djangoproject.com/en/3.0/topics/settings/)

Deploying Django to production:

[Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04)