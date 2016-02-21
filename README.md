Stats Test
==========

Executing the app
-----------------

1) create virtualenv

2) clone the repo
> git clone https://github.com/luisftejada/messages-stats.git

3) Install python requirements
> pip install -r wsgi/myproject/requirements.txt

4) cd to project folder
> cd messages-stats/wsgi/myproject

5) Setup the Django cache
> python manage.py  createcachetable

6) Run the server
> python manage.py runserver


Available URLs
--------------

- http://localhost:<port>/admin
> Access to django admin app ( user:admin / passwd:admin )

- http://localhost:<port>/get_stats1
> Get the stats using os cron functionality

- http://localhost:<port>/get_stats2
> Get the stats using django cache
