#!/usr/bin/env bash
# Build script for Render.com

pip install -r requirements.txt

echo "Running Django migrations..."
python manage.py makemigrations
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating superuser if not exists..."
echo "
from django.contrib.auth import get_user_model
from django.db import connection
User = get_user_model()
tables = connection.introspection.table_names()
if User._meta.db_table in tables and not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123', role='admin')
    print('Superuser created with admin role.')
else:
    print('Superuser already exists or table missing.')
" | python manage.py shell

