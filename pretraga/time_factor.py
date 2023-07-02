from math import exp
from datetime import datetime, timedelta
from time import struct_time, mktime
import numpy as np
from konstante import TIME_DECAY_WEIGHTS as tdw
import time


def time_decay(date_of_creation: struct_time, date_now: struct_time = None):
    delta = mktime(date_now) - mktime(date_of_creation) if date_now else time.time() - mktime(date_of_creation)

    if delta < 3600: return tdw.last_hour * tdw.decay_rate**(delta / 3600)

    if delta < 86400: return tdw.today * tdw.decay_rate**(delta / 86400)

    if delta < 604800: return tdw.this_week * tdw.decay_rate**(delta / 604800)

    if delta < 2419200: return tdw.this_month * tdw.decay_rate**(delta / 2419200)

    if delta < 31536000: return tdw.this_year * tdw.decay_rate**(delta / 31536000)

    return tdw.long_time_ago * exp(-delta / 31536000)