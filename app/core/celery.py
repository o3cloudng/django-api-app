from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

# app.config_from_object("django.conf:settings", namespace="CELERY")
app.config_from_object("django.conf:settings")

app.autodiscover_tasks()

# from __future__ import absolute_import, unicode_literals
# import os
# from app.celery import Celery

# # setting the Django settings module.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ccore.settings')
# app = Celery('core)
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Looks up for task modules in Django applications and loads them
# app.autodiscover_tasks()
