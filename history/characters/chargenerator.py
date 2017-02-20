#!/usr/bin/python
#Written by Raikin, June 2016

import csv
import re

title_starts = "1020.1.1"

titlepath = "C:/Users/Rayan/Documents/Paradox Interactive/Crusader Kings II/mod/DSA/history/titles/"

outfile = 'auto_chars.txt'

def applytitle(id,title):

    try:
        if len(title) == 1:
            event = "\n\tholder = " + id
            newcontent = title_starts + " = {" + event + "\n}\n"
            
            
            with open(titlepath + title[0] + ".txt", "r") as f:
                content = f.read()
                x = content.find(title_starts)

            if x == -1:
                with open(titlepath + title + ".txt", "a") as f:
                    f.write(newcontent)
            else:
                with open(titlepath + title + ".txt", "w") as f:
                    re.sub(title_starts + r' = {\n\t.+\n}\n', newcontent, content)
                    f.write(content)
                    
        elif len(title) == 2:
            titlename = title[0]
            date = title[1]
            
            event = "\n\tholder = " + id
            newcontent = date + " = {" + event + "\n}\n"
            
            
            with open(titlepath + titlename + ".txt", "r") as f:
                content = f.read()
                x = content.find(date)

            if x == -1:
                with open(titlepath + titlename + ".txt", "a") as f:
                    f.write(newcontent)
            else:
                with open(titlepath + titlename + ".txt", "w") as f:
                    pattern = date + r' = {\n\t.+\n}\n'
                    content = re.sub(pattern, newcontent, content)
                    f.write(content)
        else:
            print "something went wrong"
            
    except:
        with open("titlesnotfound.txt", "a") as f:
            f.write("The title " + title[0] + " could not be found.\n")
            
    return None

personlist = []

with open('charsDef.csv', 'rb') as f:
    reader = csv.reader(f,delimiter=';')
    for row in reader:
        person = row
        personlist.append(person)

counter = False
        
with open(outfile, 'w') as f:
    for person in personlist:
        if counter == True:
            id = person[0]
            print person[1]
            name = person[1]
            religion = person[2]
            culture = person[3]
            female = person[4]
            dynasty = person[5]
            titles = person[6]
            birth = person[7]
            death = person[8]
            father = person[9]
            mother = person[10]
            traits = person[11]
            martial = person[12]
            diplo = person[13]
            intrigue = person[14]
            steward = person[15]
            learning = person[16]
            health = person[17]
            fertility = person[18]
            dna = person[19]
            properties = person[20]
            occluded = person[21]
            other = person[22]
            comments = person[23]
            
            f.write('%s = {\n\tname = \"%s\"'%(id,name))
            
            if female == 'yes':
                f.write("\n\tfemale = yes")
                
            f.write("\n\treligion = %s \n\tculture = %s"%(religion,culture))
            
            if len(dynasty) >= 1:
                f.write("\n\tdynasty = %s"%(dynasty))
                
            if len(father) >= 1:
                f.write("\n\tfather = %s"%(father))
                
            if len(mother) >= 1:
                f.write("\n\tmother = %s"%(mother))
                
            if len(traits) >= 1:
                traits = traits.split()
                for trait in traits:
                    f.write("\n\tadd_trait = %s"%(trait))
                    
            if len(martial) >= 1:
                f.write("\n\tmartial = %s"%(martial))
                
            if len(diplo) >= 1:
                f.write("\n\tdiplomacy = %s"%(diplo))
            
            if len(intrigue) >= 1:
                f.write("\n\tintrigue = %s"%(intrigue))
            
            if len(steward) >= 1:
                f.write("\n\tstewardship = %s"%(steward))
            
            if len(learning) >= 1:
                f.write("\n\tlearning = %s"%(learning))
                
            if len(health) >= 1:
                f.write("\n\thealth = %s"%(learning))
                
            if len(fertility) >= 1:
                f.write("\n\tfertility = %s"%(fertility))
                
            if len(dna) >= 1:
                f.write("\n\dna = %s"%(dna))
                
            if len(properties) >= 1:
                f.write("\n\tproperties = %s"%(properties))
                
            if occluded == 'yes':
                f.write("\n\toccluded = %s"%(occluded))
                
            f.write("\n\t%s = {birth=yes}"%(birth))
            
            if other >= 1:
                f.write("\n\t" + other)
            
            f.write("\n\t%s = {death=yes}"%(death))
            
            if comments >= 1:
                comments = comments.split()
                for comment in comments:
                    f.write("\n\t#" + comment)
            
            f.write("\n}\n\n")
            
            if len(titles) >= 1:
                titles = titles.split()
                for title in titles:
                    title = title.split(":")
                    applytitle(id,title)
            
            
            
        counter = True