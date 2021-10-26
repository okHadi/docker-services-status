# resultant dictionary
# Python program to convert text
# file to JSON
  
  
import json
import re

  
# the file to be converted
filename = 'app/templates/services.txt'

with open(filename, 'r+') as f:
    text = f.read()
    text = re.sub('       ', '   ', text)
    f.seek(0)
    f.write(text)
    f.truncate()

with open(filename, 'r+') as f:
    text = f.read()
    text = re.sub('      ', '   ', text)
    f.seek(0)
    f.write(text)
    f.truncate()

with open(filename, 'r+') as f:
    text = f.read()
    text = re.sub('     ', '   ', text)
    f.seek(0)
    f.write(text)
    f.truncate()

with open(filename, 'r+') as f:
    text = f.read()
    text = re.sub('    ', '   ', text)
    f.seek(0)
    f.write(text)
    f.truncate()
  
# resultant dictionary
dict1 = {}
  
# fields in the sample file 
fields =['ID', 'Image', 'Command', 'Created', 'Status', 'Ports', 'Names']       # editable data

import re




with open(filename) as fh:
    next(fh)
        
      
    # count variable for employee id creation
    l = 1
      
    for line in fh:
        # reading line by line from the text file
        description = list( line.strip().split("  ", 7))
          
        # for output see below
        print(description) 
          
        # for automatic creation of id for each employee
        sno ='Data'+str(l)
      
        # loop variable
        i = 0
        # intermediate dictionary
        dict2 = {}
        while i<len(fields):
              
                # creating dictionary for each employee
                dict2[fields[i]]= description[i]
                i = i + 1
                  
        # appending the record of each employee to
        # the main dictionary
        dict1[sno]= dict2
        l = l + 1
  
  
# creating json file        
out_file = open("c:/Users/Hadi Khan/Desktop/stuff/Coding/test 1/test2.json", "w")
json.dump(dict1, out_file, indent = 4)
out_file.close()