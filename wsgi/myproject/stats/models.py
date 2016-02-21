from django.db import models
from django.utils import timezone
import random

# Create your models here.
class Messages(models.Model):
    state = models.CharField('State', max_length=64)
    city = models.CharField('City', max_length=64)
    username = models.CharField('User', max_length=64)
    message = models.TextField('Message')
    create_time = models.DateTimeField('Date', auto_now_add=True)
    class Meta:
        ordering = ['state', 'city', 'create_time']

    @classmethod
    def get_stats(cls):
        return {
            'cities': Messages.objects.all().values("state", 'city').annotate(
                models.Count('pk')).count(),
            'users': Messages.objects.all().values('username').annotate(
                models.Count('pk')).count(),
            'ts': timezone.now()
        }

class Stats(models.Model):
    stat_id = models.CharField('id', max_length=1)
    cities = models.IntegerField('NumCities')
    users = models.IntegerField('Users')
    ts = models.DateTimeField('ts', auto_now_add=True)

    def __str__(self):
        return '<stat {id}: {c}/{u} ({ts})>'.format(id=self.stat_id,
            c=self.cities, u=self.users, ts=self.ts)

    @classmethod
    def get_stats(cls):
        return Stats.objects.all()[0]

    @classmethod
    def update(cls):
        stats = Messages.get_stats()
        try:
            stats_obj = Stats.objects.get(stat_id="1")
            stats_obj.users = stats['users']
            stats_obj.cities = stats['cities']
            stats_obj.ts = stats['ts']
            stats_obj.save()
        except:
            stats['stat_id'] = '1'
            stats_obj = Stats.objects.create(**stats)


def create(n, cprefix='city', uprefix='user'):
    print 'Creating {num} messages'.format(num=n)
    start = timezone.now()
    for i in range(n):
        if i % 1000 == 0:
            print "   {i} of {num}".format(i=i, num=n)
        state = random.randrange(5)
        city = random.randrange(99)
        user = random.randrange(9999)
        message = random.randrange(1000000)
        Messages.objects.create(
            state='state-{num:02}'.format(num=state),
            city='{cprefix}-{city:02}'.format(cprefix=cprefix, city=city),
            username='{uprefix}-{user:06}'.format(uprefix=uprefix, user=user),
            message='message-{msg:04}'.format(msg=message)
        )
    finished = timezone.now()
    secs = (finished-start).total_seconds()
    rate = float(n) / secs
    print 'created {num} messages at {rate:.2f} messages/second'.format(num=n, rate=rate)
