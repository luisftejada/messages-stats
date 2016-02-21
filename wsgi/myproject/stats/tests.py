from django.test import TestCase
from django.db.models import Count
from django.http import HttpRequest

from django.core.urlresolvers import resolve
from stats.views import get_stats1, get_stats2
from stats.models import Messages, Stats
import json

class StatsUrlUnitTests(TestCase):

    def test_url_resolve_stats_get1(self):
        found = resolve('/stats/get1')
        self.assertEqual(found.func, get_stats1)

    def test_url_resolve_stats_get2(self):
        found = resolve('/stats/get2')
        self.assertEqual(found.func, get_stats2)

    def test_stats_get1_return_valid_json(self):
        request = HttpRequest()
        response = get_stats1(request)
        obj = json.loads(response.content)
        pass

    def test_stats_get2_return_valid_json(self):
        request = HttpRequest()
        response = get_stats2(request)
        obj = json.loads(response.content)
        pass

class StatsGetStatsTests(TestCase):
    def setUp(self):
        self.num_states = 2
        self.num_cities_per_state = 5
        self.num_users = 10
        for istate in range(self.num_states):
            for icity in range(self.num_cities_per_state):
                for iuser in range(self.num_users):
                    Messages.objects.create(
                        state='state-{istate}'.format(istate=istate),
                        city='city-{icity}'.format(icity=icity),
                        username='user-{user}'.format(user=iuser),
                        message='msg-{s}-{c}-{u}'.format(s=istate, c=icity, u=iuser)
                    )
        Stats.update()

    def test_stats_get1_check_cities(self):
        num_cities = Messages.objects.all().values('state','city')\
            .annotate(Count('pk')).count()
        request = HttpRequest()
        response = get_stats1(request)
        obj = json.loads(response.content)
        self.assertEqual(obj['cities'], num_cities)
        self.assertEqual(num_cities, self.num_cities_per_state*self.num_states)

    def test_stats_get2_check_cities(self):
        num_cities = Messages.objects.all().values('state','city')\
            .annotate(Count('pk')).count()
        request = HttpRequest()
        response = get_stats2(request)
        obj = json.loads(response.content)
        self.assertEqual(obj['cities'], num_cities)
        self.assertEqual(num_cities, self.num_cities_per_state*self.num_states)

    def test_stats_get1_check_users(self):
        num_users = Messages.objects.all().values('username')\
            .annotate(Count('pk')).count()
        request = HttpRequest()
        response = get_stats1(request)
        obj = json.loads(response.content)
        self.assertEqual(obj['users'], num_users)
        self.assertEqual(num_users, self.num_users)

    def test_stats_get2_check_users(self):
        num_users = Messages.objects.all().values('username')\
            .annotate(Count('pk')).count()
        request = HttpRequest()
        response = get_stats2(request)
        obj = json.loads(response.content)
        self.assertEqual(obj['users'], num_users)
        self.assertEqual(num_users, self.num_users)

    def test_stats_get1_fails_no_records_in_db(self):
        Stats.objects.all().delete()
        request = HttpRequest()
        response = get_stats1(request)
        obj = json.loads(response.content)
        self.assertTrue(obj.has_key('error'))
        self.assertEqual(obj['result'], 'error')

    def test_stats_get2_does_not_fail_if_no_records_in_db(self):
        Stats.objects.all().delete()
        Messages.objects.all().delete()
        request = HttpRequest()
        response = get_stats2(request)
        obj = json.loads(response.content)
        self.assertFalse(obj.has_key('error'))
        self.assertEqual(obj['result'], 'success')
        self.assertEqual(obj['users'],0)
        self.assertEqual(obj['cities'],0)
