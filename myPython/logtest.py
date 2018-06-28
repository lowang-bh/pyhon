#!/usr/bin/env python
import logging
import time
from logging import handlers

log = logging.Logger('test')
handler = handlers.RotatingFileHandler('/var/log/test.log', 'a', 10 * 1024 * 1024, 2)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter("%(asctime)s,%(lineno)4d,%(filename)s : %(message)s"))
log.addHandler(handler)

while 1:
    log.info("hello world")
    log.debug("This is test log for filebeat on c1-app113")
    time.sleep(60)
