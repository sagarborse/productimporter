#!/bin/bash
echo "Starting Importer Service"
if [[ ! -e logs/importer.log ]]; then
    mkdir -p logs
    touch logs/importer.log
    chmod +x logs/importer.log
fi
#if [[ ! -e logs/gunicorn-access.logs ]]; then
#    touch logs/gunicorn-access.logs
#    chmod +x logs/gunicorn-access.logs
#fi
#if [[ ! -e logs/gunicorn-errors.logs ]]; then
#    touch logs/gunicorn-errors.logs
#    chmod +x logs/gunicorn-errors.logs
#fi
cd /importerservice/src
ls
pwd
#python -u manage.py makemigrations
#python -u manage.py migrate
#python  manage.py collectstatic --noinput

#gunicorn --workers=${WORKERS} -b 0.0.0.0:${APP_PORT} --access-logfile /commservice/logs/gunicorn-access.logs --error-logfile /commservice/logs/gunicorn-errors.logs core.wsgi
python -u /importerservice/src/manage.py runserver 0.0.0.0:80
