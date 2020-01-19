from sorm_logs.settings import *

DATABASES = {
    'default': {
        'NAME': 'sorm_logs',
        'ENGINE': 'django.db.backends.mysql',
        'USER': '{{ mysql_user }}',
        'PASSWORD': '{{ mysql_password }}',
        'HOST': 'sorm_logs_mariadb',
        'PORT': "3306"
    },
    'clickhouse': {
        'url': 'http://sorm_logs_clickhouse:8123/'
    }
}