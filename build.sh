#!/usr/bin/env bash
# Build script for Render.com

python manage.py migrate
python manage.py collectstatic --noinput
