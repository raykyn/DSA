#!/usr/bin/python
#Written by Raikin, June 2016

import csv

outfile = 'auto_dynasties.txt'

dynastylist = []

with open('dynastyDef.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        dynasty = row
        dynastylist.append(dynasty)
        
counter = False

with open(outfile, 'w') as f:
    for dynasty in dynastylist:
        if counter == True:
            id = dynasty[0]
            name = dynasty[1]
            culture = dynasty[2]
            
            f.write("%s = {\n\tname = \"%s\""%(id, name))
            
            if len(culture) >= 1:
                f.write("\n\tculture = %s"%(culture))
                
            f.write("\n\tused_for_random = no\n}\n\n")
            
            
        counter = True