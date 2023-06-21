from math import exp
from datetime import datetime, timedelta
import numpy as np


def time_decay(date_of_creation: datetime, date_now = datetime.now()):
    return 1/3
    time_delta = date_now - date_of_creation

    delta_ranges = [timedelta(hours=1), timedelta(days=1),
                    timedelta(days=7), timedelta(days=30), timedelta(days=364)]
    
    delta_ranges = dict((), (), (), (), (), ())
    
    div_factor = None
    for i in delta_ranges:
        if delta_ranges[i] < time_delta:
            div_factor = delta_ranges[i]
            continue
        break

    if not div_factor:
        div_factor = timedelta()

    
    
        pass

    return np.exp(-DECAY * time_delta)


    