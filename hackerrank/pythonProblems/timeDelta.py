from datetime import datetime

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
    time1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    time2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    
    timeInterval = int((time1 - time2).total_seconds())
    # return timeInterval
    return str(timeInterval).strip('-') # stripping '-' because if time1 is smaller than time2 then - symbol will be appended

t1 = 'Sun 10 May 2015 13:54:36 -0700'
t2 = 'Sun 10 May 2015 13:54:36 -0000'

print(time_delta(t1, t2))