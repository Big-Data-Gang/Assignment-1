#!/usr/bin/env python3
  
#from operator import itemgetter
import sys
  
current_hour = None
current_count = 0
hour = None
  
# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # slpiting the data on the basis of tab we have provided in mapper.py
    try:
        hour, count = line.split(' ', 1)
    except:
        continue
    # convert count (currently a string) to int
    try:
        count = int(count.strip())
        hour = int(hour.strip())
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
  
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: hour) before it is passed to the reducer
    if current_hour == hour:
        current_count += count
    else:
        if current_hour:
            # write result to STDOUT
            print(f"{current_hour} {current_count}")
        current_count = count
        current_hour = hour
  
# do not forget to output the last hour if needed!
if current_hour == hour:
    print(f"{current_hour} {current_count}")