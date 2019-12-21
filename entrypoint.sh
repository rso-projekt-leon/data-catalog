#!/bin/sh
echo "Waiting for postgres..."

while ! nc -z catalog-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"


echo "Starting data-catalog..."
python manage.py run -h 0.0.0.0
