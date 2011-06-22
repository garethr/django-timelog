A simple django middleware that logs request times using the Django 1.3 logging support, and a management command to analyze the resulting data. Once installed and configured you can run a command line these:

<pre>python manage.py analyze_timelog
python manage.py analyze_timelog --noreverse</pre>

And generate useful tabular data like this:

<pre>
+--------------------------+--------+--------+-------+---------+---------+-------+-----------------+
| view                     | method | status | count | minimum | maximum | mean  | stdev           |
+--------------------------+--------+--------+-------+---------+---------+-------+-----------------+
| boxes.viewsBoxDetailView | GET    | 200    | 9430  | 0.14    | 0.28    | 0.21  | 0.0700037118541 |
+--------------------------+--------+--------+-------+---------+---------+-------+-----------------+
| boxes.viewsBoxListView   | GET    | 200    | 66010 | 0.17    | 0.28    | 0.232 | 0.0455415351076 |
+--------------------------+--------+--------+-------+---------+---------+-------+-----------------+
| django.views.staticserve | GET    | 200    | 61295 | 0.00    | 0.02    | 0.007 | 0.0060574669888 |
+--------------------------+--------+--------+-------+---------+---------+-------+-----------------+
</pre>

This project was heavily influenced by the Rails "Request log analyzer":https://github.com/wvanbergen/request-log-analyzer.

h2. Installation

<pre>pip install django-timelog</pre>

Once installed you need to do a little configuration to get things working. First add the middleware to your MIDDLEWARE_CLASSES in your settings file.

<pre>MIDDLEWARE_CLASSES = (
  'timelog.middleware.TimeLogMiddleware',</pre>

Next add timelog to your INSTALLED_APPS list. This is purely for the management command discovery.

<pre>INSTALLED_APPS = (
  'timelog',</pre>

Then configure the logger you want to use. This really depends on what you want to do, the django 1.3 logging setup is pretty powerful. Here’s how I’ve got logging setup as an example:

<pre>TIMELOG_LOG = '/path/to/logs/timelog.log'

LOGGING = {
  'version': 1,
  'formatters': {
    'plain': {
      'format': '%(asctime)s %(message)s'},
    },
  'handlers': {
    'timelog': {
      'level': 'DEBUG',
      'class': 'logging.handlers.RotatingFileHandler',
      'filename': TIMELOG_LOG,
      'maxBytes': 1024 * 1024 * 5,  # 5 MB
      'backupCount': 5,
      'formatter': 'plain',
    },
  },
  'loggers': {
    'timelog.middleware': {
      'handlers': ['timelog'],
      'level': 'DEBUG',
      'propogate': False,
     }
  }
}</pre>

Lastly, if you have particular URIs you wish to ignore you can define them using basic regular expressions in the TIMELOG_IGNORE_URIS list in settings.py:

<pre>TIMELOG_IGNORE_URIS = (
    '^/admin/',         # Ignores all URIs beginning with '/admin/'
    '^/other_page/$',   # Ignores the URI '/other_page/' only, but not '/other_page/more/'.
    '.jpg$',            # Ignores all URIs ending in .jpg
)</pre>
