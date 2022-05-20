"""Here we hold views to our events api
"""
from django.http import JsonResponse
from django.utils import timezone

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
    interval = int(request.GET.get('interval', 0))
    # --0-- if no interval retrieving all stats
    # --1-- Establish the start time to search from then forward
    start = dt.now() - timedelta(seconds=interval)

    # --2-- Query the model
    events = EventItem.objects.filter(time_stamp__gte=start)
    print(len(events))

    if not events:
        return JsonResponse({'message': f'No Event was found created '
                                        f'after: {interval} seconds ago'},
                            status=204)

    # --3-- Merge the dictionaries
    merged = dict(x for e in events for x in e.stats.items())
    return JsonResponse(merged, status=200)
