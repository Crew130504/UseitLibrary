#!/usr/bin/env bash
# Build script for Render.com

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Generating and applying migrations..."
python manage.py makemigrations --merge --noinput
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput
