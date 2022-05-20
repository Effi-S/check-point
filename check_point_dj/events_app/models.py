"""
This module holds data related to an Event.

Each event holds:
-----
    1) 'data' - The event data in string format.
    2) 'time_stamp' - A timestamp of the event.
"""
from __future__ import annotations  # in-case python version < 3.9
from django.db import models

BUCKETS = ('checkpoint', 'avanan', 'email', 'security')


class EventItem(models.Model):
    """ Event Model.
        attributes:
            1) 'data' - The event data in string format.
            2) 'time_stamp' - A timestamp of the event.
    """
    data = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True,
                                      )
    stats = models.JSONField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.stats:
            self.stats = self._generate_stats(self.data.decode())

    @staticmethod
    def _generate_stats(data: str) -> dict:
        """
        This method maps each key-word in BUCKETS to the count of occurrences in the given data.

        Note:
        -----
            2) Only Whole words are counted.
                (example:  key-word 'aa' wont be counted on 'baa abb baba')
            1) Case insensitive.
                (example: key-word 'aa' will be counted 3 times on ' BB AA CC Aa DD aA')
        """

        # --1-- making lowercase + splitting into words.
        words = data.lower().split()

        # --2-- counting each keyword.
        ret = {b: words.count(b) for b in BUCKETS}
        return ret

