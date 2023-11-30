from datetime import datetime, timedelta
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ORM.settings")
django.setup()

from Shelf.models import Author, Post  

q = Author.objects.all()

print(q)


