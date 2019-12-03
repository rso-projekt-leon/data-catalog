# data-catalog

## Development
- `docker-compose up -d --build`
- `docker-compose exec data-catalog python manage.py recreate_db`
- `docker-compose exec data-catalog python manage.py seed_db`