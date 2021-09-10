#!/usr/bin/env python3

import json
import sys

curr_state = None
curr_city = None
city_count = 0
state_count = 0

for line in sys.stdin:
    line = line.strip()

    # Each line will have location and count seperated by a tab. Ex: MA-Brewster       1 
    loc, count = line.split('\t', 1)

    # loc will be of the format state-city. Splitting it into state and city Ex: MA-Brewster 
    state, city = loc.split('-', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    # The outputs from mapper will be sorted based on key which is loc.
    # And as loc is of the format state-city, the sorting will first be based on state then city
    # All lines of same state will get clubbed together and in that further clubbings will be present based on city

    # First check state
    if state == curr_state:
        if city == curr_city:
            city_count += count
            state_count += count
        
        # If only city has changed, print the prev city's count and update city. Reset city count
        else:
            print(curr_city, city_count)
            curr_city = city 
            city_count = count
            state_count += count
    
    # If state itself has changed
    else:
        # If there was a prev state, the state and its total count
        if curr_state:
            print(curr_state, state_count)
        
        # Then update the state and city as well. Also reset the counts for both state and city
        curr_state = state
        curr_city = city 
        state_count = count
        city_count = count

        # When new state starts print it 
        print(state)       