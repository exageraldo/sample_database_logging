import os

default_url = 'postgresql://user:password@host/database'
url_database = os.environ.get('URL_DATABASE', default_url)
