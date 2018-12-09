#!/usr/bin/env python
import logging
import time
import sys
from logging import handlers

log = logging.Logger('test')
log.setLevel(logging.INFO)
handler = handlers.RotatingFileHandler('/var/log/test.log', 'a', 10 * 1024 * 1024, 2)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter("[%(levelname)s] %(asctime)s,%(lineno)4d,%(filename)s : %(message)s", '%Y-%m-%d %H:%M:%S'))
log.addHandler(handler)

print(log, id(log), logging.getLogger("test"), id(logging.getLogger("test")))
print(logging.getLogger("test").level)
print(logging._handlers)
logging.getLogger("test").setLevel(logging.DEBUG)
print(logging.getLogger("test").level, log.isEnabledFor(logging.INFO),log.isEnabledFor(logging.DEBUG))
log.debug("Before change log level to DEBUG.")

d ={1:"test", 2: "log test"}
log.setLevel(logging.DEBUG)
print(log.isEnabledFor(logging.DEBUG))
log.info("hello world")
log.debug(d)
log.debug("This is test log for filebeat on c1-app113")

import json
import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])
pprint.pprint(stuff)
print(stuff)
print(pprint.pformat(stuff, indent=4))
import json
raw_data="""{
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "cmdb",
        "USER": "xyz_cmdb",
        "PASSWORD": "HV13gsFElnuEgzjD",
        "HOST": "10.143.248.119",
        "PORT": "10001",
        "CHARSET": "utf-8",
        "ATOMIC_REQUESTS": true
    }
}"""
jsondata = json.loads(raw_data)
pprint.pprint(jsondata)
print(pprint.pformat(jsondata))
log.info(pprint.pformat(jsondata))
