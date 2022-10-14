import os
import sys

path = '/home/Roilin/todoapp/'

if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'
# then:
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
