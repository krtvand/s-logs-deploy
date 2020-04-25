from sorm_logs.settings import *

DATABASES = {
    'default': {
        'NAME': 'sorm_logs',
        'ENGINE': 'django.db.backends.mysql',
        'USER': '{{ mysql_user }}',
        'PASSWORD': '{{ mysql_password }}',
        'HOST': '{{ sorm_logs_mariadb_docker_container_name }}',
        'PORT': "3306"
    },
    'clickhouse': {
        'url': 'http://{{ sorm_logs_clickhouse_docker_container_name }}:8123/',
    }
}

SORM_LOGS_BACKUP = {
    'url': 'http://{{ sorm_logs_backup_docker_container_name }}:{{ sorm_logs_backup_port }}/make_clickhouse_backup'
}