# hack_py
(Django App)

Steps to setup postgres

1.sudo apt-get update

2.sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib

3.sudo -u postgres psql

4.CREATE DATABASE hnews;

5.CREATE USER root WITH PASSWORD 'root';

6.GRANT ALL PRIVILEGES ON DATABASE hnews TO root;

#Now create a virtual env and rn all migrations file.
