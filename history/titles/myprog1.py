import sys
import re
import glob

input = "\n\tholder=3"
titleToChange = "e_horasia"
searchFor = "liege=" + titleToChange
nextTier = []
nextTier2 = []

f = open(titleToChange + ".txt", 'r')
content = f.read()
f.close()
x = content.find("1060.1.1={")
content = content[:x+10] + input + content[x+10:]
f = open(titleToChange + ".txt", 'w')
f.write(content)
f.close

for filename in glob.glob('*.txt'):
	f = open(filename, 'r')
	content = f.read()
	if searchFor in content:
		nextTier.append(filename)
		f.close()
		x = content.find("1060.1.1={")
		content = content[:x+10] + input + content[x+10:]
		f = open(filename, 'w')
		f.write(content)
		f.close

for file in nextTier:		
	for filename in glob.glob('*.txt'):
		f = open(filename, 'r')
		content = f.read()
		searchForNew = "liege=" + file[:-4]
		if searchForNew in content:
			nextTier2.append(filename)
			f.close()
			x = content.find("1060.1.1={")
			content = content[:x+10] + input + content[x+10:]
			f = open(filename, 'w')
			f.write(content)
			f.close
			
for file in nextTier2:		
	for filename in glob.glob('*.txt'):
		f = open(filename, 'r')
		content = f.read()
		searchForNew = "liege=" + file[:-4]
		if searchForNew in content:
			f.close()
			x = content.find("1060.1.1={")
			content = content[:x+10] + input + content[x+10:]
			f = open(filename, 'w')
			f.write(content)
			f.close
		
print nextTier
print nextTier2
