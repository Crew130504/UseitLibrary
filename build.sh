#!/usr/bin/env bash
# Build script for Render.com

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Generating and applying migrations..."
python manage.py makemigrations --merge --noinput
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating superuser if not exists or invalid..."
echo "
from django.contrib.auth import get_user_model
from django.db import connection
User = get_user_model()
tables = connection.introspection.table_names()
if User._meta.db_table in tables:
    user = User.objects.filter(username='admin').first()
    if user and user.role != 'admin':
        print('Existing superuser found with wrong role. Deleting...')
        user.delete()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123', role='admin')
        print('Superuser created.')
    else:
        print('Superuser already exists with correct role.')
else:
    print('User table does not exist.')
" | python manage.py shell

