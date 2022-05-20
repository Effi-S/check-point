"""Here we hold views to our events api
"""
from collections import Counter

from django.http import JsonResponse

from .models import EventItem
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime as dt, timedelta


@csrf_exempt  # [Note: This removes csrf for showcase]
def post(request) -> JsonResponse:
    """post an event by providing 'data'
    The time_stamp is automatically  generated."""
    # --1-- Validating input
    if not request.body:
        return JsonResponse({'message': f'Empty request'},
                            status=204)

    # --2-- Adding an EventItem
    item = EventItem.objects.create(data=request.body)

    # --3-- Responding
    return JsonResponse({'message': f'Event Item created!',
                         'data': item.data.decode("utf-8"),
                         'time_stamp': f'{item.time_stamp}'},
                        status=201)


@csrf_exempt  # [Note: This removes csrf for showcase]
def get_stats(request) -> JsonResponse:
    """Get the merged stats for the last 'interval' seconds"""
    # --1-- Establish the start time to search from then forward
    interval = int(request.GET['interval'])
    start = dt.now() - timedelta(seconds=interval)

    # --2-- Query the model
    events = EventItem.objects.filter(time_stamp__gte=start)
    print(len(events))

    if not events:
        return JsonResponse({'message': f'No Event was found created '
                                        f'after: {interval} seconds ago'},
                            status=204)

    # --3-- Merge the dictionaries
    # Counter cleans up boiler-plate
    # Any value not found in Counter defaults to 0.
    # ( => we don't have to check if key exists before updating it's value)
    counter = Counter()
    for event in events:
        for k, v in event.stats.items():
            counter[k] += v

    return JsonResponse(counter, status=200)
