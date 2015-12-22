import sys
import re
import glob

input = "\n\tholder=5"
titleToChange = "e_horasia"
searchFor = "liege=" + titleToChange
nextTier = []
nextTier2 = []

f = open(titleToChange + ".txt", 'r')
content = f.read()
f.close()
content = content.replace(input, "")
f = open(titleToChange + ".txt", 'w')
f.write(content)
f.close

for filename in glob.glob('*.txt'):
	f = open(filename, 'r')
	content = f.read()
	if searchFor in content:
		nextTier.append(filename)
		f.close()
		content = content.replace(input, "")
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
			content = content.replace(input, "")
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
			content = content.replace(input, "")
			f = open(filename, 'w')
			f.write(content)
			f.close
		
print nextTier
print nextTier2
