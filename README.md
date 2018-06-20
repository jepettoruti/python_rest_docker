# python_rest_docker
This repo implements the Rest_Framework tutorial for Django, and goes into dockerizing the deployment. Potentially going into deploying to AWS somehow.

The code is based on the results of running through the tutorial at http://www.django-rest-framework.org/tutorial/1-serialization/.

I took the liberty of adding Swagger (OpenAPI) support to the schema, as I wanted to use Swagger for a while.

The docker setup is initially based on https://www.caktusgroup.com/blog/2017/03/14/production-ready-dockerfile-your-python-django-app/ althought the example was not working properly and needed a bit of love.

## How to run

`docker-compose up --build -d`
`docker-compose logs -f`

Navigate to `http://localhost:8000`

Needs the usual trick of creating the user into Django, as the DB is empty. I did that by connecting into the running instance (`docker exec -i -t <TAG> sh` and running `/venv/bin/python manage.py createsuperuser`)
