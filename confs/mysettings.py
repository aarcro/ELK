from storyville.conf.logcfg.common import *

LOGSTASH_HOST = '192.168.56.102'
LOGSTASH_PORT = 5959

# Setup the logstash formatter
LOGGING['formatters']['formatter_logstash'] = {
    '()': 'storyville.core.logging.logstash.LogstashFormatter',
    'program': 'medley',
}

# Setup the logstash handler
LOGGING['handlers']['handler_logstash'] = {
    'class': 'storyville.core.logging.logstash.LogstashHandler',
    'host': LOGSTASH_HOST,
    'port': LOGSTASH_PORT,
    'formatter': 'formatter_logstash',
    'level': 'DEBUG',
    'filters': ['request_filter'],
}

LOGGING['loggers']['']['handlers'].append('handler_logstash')

from celery import signals
from storyville.core.logging.logstash import CeleryLogstashSignalReceiver

receiver = CeleryLogstashSignalReceiver(
    host=LOGSTASH_HOST,
    port=LOGSTASH_PORT,
    config={
        "enabled": True,
        "level": "INFO",
        "queues": [
            "externalfeeds",
            "pagegen",
        ]
    }
)

signals.after_setup_logger.connect(receiver.after_setup_logger)
