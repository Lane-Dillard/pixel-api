#!/bin/bash

rm db.sqlite3
rm -rf ./pixelapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations pixelapi
python3 manage.py migrate pixelapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

