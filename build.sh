#!/usr/bin/env bash
#!/usr/bin/env bash
# Build script for Render.com
pip install -r requirements.txt

echo "Running Django migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput
