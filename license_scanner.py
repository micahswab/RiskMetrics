from collections import OrderedDict
from functools import reduce
from itertools import groupby
import os,json
from pprint import pprint


user_input = raw_input("Please enter the package name output, which has to be matched with the name you put in the cmd ")
directory = os.path.normpath("C:/scancode-toolkit-1.6.0")
for subdir, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(str(user_input).strip()):
            f=open(os.path.join(subdir, file),'r')
            data_json = json.load(f)

all_licenese =  data_json['results']

count_empty_file = 0
license_file =[]
for element in all_licenese:
    if(element['licenses'] == []):
        count_empty_file = count_empty_file +1
    else:
        license_file.append((element))

count_file_with_license = data_json['resource_count'] - count_empty_file

#print("file with license: ", count_file_with_license)
#print("file with No license: ",count_empty_file)


# print out the license
list_of_license = []
for i in range (len(license_file)):
    for keys,values in (license_file[i].items()):
        if (keys == 'licenses'):
            c = values
            for key,value in c[0].items():
                if (key =='short_name'):
                    list_of_license.append(value)

empty_list_license = []
#pprint(list(OrderedDict.fromkeys(list_of_license)))

data = {
    "Number file with license: ":count_file_with_license,
    "Number file without license: ":count_empty_file,
    "Type of license:": list(OrderedDict.fromkeys(list_of_license))
}

jsonData =json.dumps(data,indent = 2)

with open('JSONData.json', 'w') as f:
    f.write(jsonData)
