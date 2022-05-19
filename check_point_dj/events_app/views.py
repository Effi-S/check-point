"""Here we hold views to our events api
"""
from django.http import JsonResponse

from .models import EventItem
from django.views.decorators.csrf import csrf_exempt


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
                         'time_stamp': f'{bool(item.time_stamp)}'},
                        status=201)


@csrf_exempt  # [Note: This removes csrf for showcase]
def get_stats(request) -> JsonResponse:
    """Get the merged stats for the last 'interval' seconds"""
    interval = int(request.GET['interval'])
    return JsonResponse({'dummy': 'dummy',
                         'interval': interval},
                        status=200)
