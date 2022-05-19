"""
This module holds data related to an Event.

Each event holds:
-----
    1) 'data' - The event data in string format.
    2) 'time_stamp' - A timestamp of the event.
"""
from django.db import models


class EventItem(models.Model):
    """ Event Model.
        attributes:
            1) 'data' - The event data in string format.
            2) 'time_stamp' - A timestamp of the event.
    """
    data = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)
