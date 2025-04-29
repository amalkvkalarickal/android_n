"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

# Add the project root directory to Python path
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')

# Import the Django WSGI application
from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()  # This is the 'app' that Gunicorn is looking for