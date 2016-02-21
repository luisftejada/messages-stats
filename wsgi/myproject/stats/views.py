from django.shortcuts import render
from django.http import HttpResponse
from stats.models import Stats, Messages
from django.views.decorators.cache import cache_page

def get_stats1(request):
    """Get the statistics from the Stats Table"""
    try:
        stats = Stats.get_stats()
        ret = ('{{ "users": {users}, "cities": {cities}, '
               '"ts": "{ts}", "result": "success" }}').format(
                **stats.__dict__)
    except Exception, err:
        ret = '{{ "result": "error", "error": "{err}" }}'.format(err=err)

    return HttpResponse(ret, content_type="application/json")

@cache_page(60)
def get_stats2(request):
    """Get the statistics from the Messages Table, but using the cache"""
    try:
        stats = Messages.get_stats()
        stats['ts']
        ret = ('{{ "users": {users}, "cities": {cities}, '
               '"ts": "{ts}", "result": "success" }}').format(
                **stats)
    except Exception, err:
        ret = '{{ "result": "error", "error": "{err}" }}'.format(err=err)

    return HttpResponse(ret, content_type='application/json')
