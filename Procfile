release: python src/manage.py migrate
web: gunicorn --pythonpath=src/ core.wsgi:application --preload --workers 1