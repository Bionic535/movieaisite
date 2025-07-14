#!/usr/bin/env bash
# Exit on error
set -o errexit



# Convert static asset files
python manage.py collectstatic --no-input


python manage.py makemigrations
# Apply any outstanding database migrations
python manage.py migrate

# Start the Django development server
python manage.py runserver



