"""
This module holds data related Statistics of name occurrences.

Each Stat holds:
-----
    1) 'data' - The event data in JSON format.
    2) 'time_stamp' - A timestamp of the time the entry was received.
"""
from django.db import models


class StatItem(models.Model):
    """
    Tally of name occurrences.

    'data' example:
    ----------
        { 'checkpoint': 1,
        'security': 1 }
    """
    data = models.JSONField()
    time_stamp = models.DateTimeField()
