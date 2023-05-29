#!/bin/sh

if [ "$POSTGRES_DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $HOST $PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

echo "IJFRIJFIJRI"

python3 manage.py makemigrations
python3 manage.py migrate

exec "$@"

