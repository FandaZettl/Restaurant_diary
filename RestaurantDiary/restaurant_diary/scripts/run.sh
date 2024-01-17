#!/bin/bash

# Stop and remove existing containers
docker-compose down

# Build and run Docker containers
docker-compose up --build -d

# Apply database migrations
docker-compose run web python manage.py migrate

# Create a superuser
docker-compose run web python manage.py createsuperuser

# Run the development server
docker-compose up
