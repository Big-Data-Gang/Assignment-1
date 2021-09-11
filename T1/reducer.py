#!/usr/bin/env python3
  
import sys
  
current_hour = None
current_count = 0
hour = None
  
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    try:
        hour, count = line.split(' ', 1)
    except:
        continue
    try:
        count = int(count.strip())
        hour = int(hour.strip())
    except ValueError:
        continue

    if current_hour == hour:
        current_count += count
    else:
        if current_hour != None:
            print(f"{current_hour} {current_count}")
        current_count = count
        current_hour = hour
  
if current_hour == hour:
    print(f"{current_hour} {current_count}")