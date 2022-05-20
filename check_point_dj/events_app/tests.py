"""
module that holds all of our tests.
    [Note: Django's test FW is a wrapper for unittest so syntax is similar]
"""
import json

from django.test import TestCase


class URLTests(TestCase):
    """
    Here we will hold all our Domain driven tests.
    [ Note: Django automatically creates a Test DB for these tests.
            This test DB is automatically destroyed on test completion. ]
    """

    def test_events_sanity(self):
        """Here we will test that an event is created in our DB."""
        response = self.client.post('/api/v1/events', {'body': 'This is a test'})
        self.assertEquals(response.status_code, 201)

    def test_stats_sanity(self):
        """
        Here we will test that we can create a event
        and then we get it back through api/v1//stats.
        We set an interval of 10 seconds
        """
        self.client.post('/api/v1/events', data={'body': 'This is a test'})
        response = self.client.get('/api/v1/stats?interval=10')
        self.assertIn(response.status_code, (200, ))

    def test_stats_correct_tally(self):
        """
        Here we will add 2 events and test that the stats are correct for them.
        """
        # --1-- define messages
        messages = (
            'Avanan is a leading Enterprise Solution for Cloud'
            ' Email and Collaboration Security',
            'CheckPoint Research have been observing an enormous rise'
            ' in email attacks since the beginning of 2020'
        )
        # --2-- post messages
        for msg in messages:
            self.client.post('/api/v1/events', data={'body': msg})

        # --3-- Get stats
        response = self.client.get('/api/v1/stats?interval=10')
        # --4-- Testing stats is expected result
        expected = {
            "checkpoint": 1,
            "avanan": 1,
            "email": 2,
            "security": 1
        }
        data = json.loads(response.content)
        self.assertEquals(data, expected)
