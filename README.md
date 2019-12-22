[![Build Status](https://travis-ci.org/rso-projekt-leon/data-catalog.svg?branch=master)](https://travis-ci.org/rso-projekt-leon/data-catalog)

# data-catalog

## Development
- `docker-compose up -d --build`
- `docker-compose exec data-catalog python manage.py recreate_db`
- `docker-compose exec data-catalog python manage.py seed_db`

## Production 
- `kubectl apply -f kubernetes/data-catalog-deployment.yaml`