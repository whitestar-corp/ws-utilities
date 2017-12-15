"""

This script extracts the jsons 

"""

import os 
import json
import time
from pprint import pprint

files = os.listdir("events")
fields = ['first_name','last_name','company','title','email_address','subscribe','dummy','_matched_characters','code','message','_matched_records','operation']

f = open('wizardreg.csv', 'w')

for field in fields:
    f.write(field)
    f.write(', ')
f.write('log_file')
f.write(', ')
f.write('created')
f.write(', ')
f.write('CR')
f.write(', ')
f.write('\n')

for file in files:
    #print(file)
    filenamepath="events/" + file

    parsed_data = json.load(open(filenamepath))
    #pprint(parsed_data)
    for field in fields:
        print(field, ",")
        f.write(parsed_data[0][field])
        f.write(', ')
    print
    f.write(file)
    f.write(', ')
    s=os.stat(filenamepath)
    f.write(str(s.st_mtime))
    f.write(', ')
    f.write(time.ctime(s.st_mtime))
    f.write('\n')

f.close()
