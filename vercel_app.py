import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_vercel_task.settings')  # Asegúrate de que el nombre sea correcto
app = get_wsgi_application()
