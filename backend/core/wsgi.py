import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()

# Add Whitenoise for static files
from whitenoise import WhiteNoise
application = WhiteNoise(application, root="staticfiles")
