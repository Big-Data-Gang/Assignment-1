import json
file = open("temp.json", "r").readlines()
count = 0
maxFields = 0
minFields = 1500
for i in file:


    count += 1
    dick = json.loads(i)
    if len(dick) > maxFields:
        maxFields = len(dick)
    if len(dick) < minFields:
        minFields = len(dick)
    # print(dick)
print(count, maxFields, minFields)
#! 145330, 43, 43
#! No fields missing