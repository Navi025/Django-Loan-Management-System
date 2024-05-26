
"""
from django.apps import AppConfig


class DashboardConfig(AppConfig):
    name = 'dashboard'
"""

    # dashboard/apps.py

from django.apps import AppConfig

class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'
