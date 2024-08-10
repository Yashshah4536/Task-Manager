#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install project dependencies
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py makemigrations
python manage.py migrate
