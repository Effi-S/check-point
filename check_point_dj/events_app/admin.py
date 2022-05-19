"""
This module is for internal development and debugging.
Models are registered here to the 'admin-site'.
"""
from django.contrib import admin

from .models import EventItem

admin.site.register(EventItem)  # registering our Event Model
