# A Python Django Example

This repo is intended for use with [Gitpod](httpsL//gitpod.io).

## Basics
When opening a new gitpod with this repo you should:
1. Automatically get a docker container that creates a DB and starts pgAdmin on the port 7000.
1. Credentials for the database can be found in the pgadmin.json file.
1. Additionally, pip should be upgraded on init, and requirements.txt should be used to install `psycopg2` and `Django` among other packages.

## Changing the Django PROJECT name
1. The current project name is `myproject`. If you would like to change that name you will need to change the directory name as well as all the references to that project throughout the files in the project. That might be worth the time.

## Django Admin
The CSRF_TRUSTED_ORIGINS setting in settings.py should be set to allow `https://*.gitpod.io` for a trusted CSRF token.
