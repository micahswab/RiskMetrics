# SPDX-License-Identifier: MIT

import sys, os, json

from subprocess import run
from datetime import datetime
from collections import OrderedDict

def cpe_search(vendor, product, version):       

    part = 'a'
    vendor = vendor.replace(' ', '_').lower()
    product = product.replace(' ', '_').lower()
    version = version.replace(' ', '_').lower()
    update = '-'
    edition = '-'
    language = '-'

    cpe = 'cpe:/a:' + vendor + ':' + product + ':' + version

    par_dir = os.path.dirname(os.path.realpath(__file__))
    gpa_dir = os.path.dirname(par_dir)
    nvd_dir = str(gpa_dir) + '/nvd/'
    filename = 'nvdcve-2.0-%d.xml'

    start_year = 2002
    end_year = datetime.now().year
    
    for year in range(start_year, end_year + 1):
        with open(nvd_dir + filename.replace('%d', str(year)), 'r') as nvd:
            for line in nvd:
                if cpe in line:
                    return True
    return False

path_to_pkg = input("Please enter the absolute path to the software package to be analyzed: ")
vendor = input("Please enter the vendor name or the highest organization-specific" 
               "label of the organization's DNS (example: cisco from cisco.com): ")
product = input("Please enter the product name: ")
version = input("Please enter the product version number: ")

par_dir = os.path.dirname(os.path.realpath(__file__))
gpa_dir = os.path.dirname(par_dir)
scancode = str(gpa_dir) + '/scancode-toolkit-1.6.0/scancode'

run([scancode, '--format', 'json', path_to_pkg, 'info.json'])

directory = os.path.dirname(os.path.realpath(__file__))
for subdir, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('info.json'):
            with open(os.path.join(subdir, file),'r') as f:
                data_json = json.load(f)

all_licenses =  data_json['results']

count_empty_file = 0
license_file =[]
for element in all_licenses:
    if(element['licenses'] == []):
        count_empty_file = count_empty_file +1
    else:
        license_file.append((element))

count_file_with_license = data_json['resource_count'] - count_empty_file

# print out the license
list_of_license = []
for i in range (len(license_file)):
    for keys,values in (license_file[i].items()):
        if (keys == 'licenses'):
            for element in values:
                for key,value in element.items():
                    if (key =='short_name'):
                        list_of_license.append(value)

data = {
    "Number of files with a license" :count_file_with_license,
    "Number of files without a license" :count_empty_file,
    "Types of licenses" : list(OrderedDict.fromkeys(list_of_license)),
    "CPE located in NVD" : cpe_search (vendor, product, version)
}

jsonData = json.dumps(data, indent = 2)

print ('\nResults:\n')
print (jsonData)
print ('\nNotes:\n')
print ('* A Common Platform Enumeration (CPE) in the National Vulnerability Database (NVD)')
print ('  is not necessarily indicitive of a vulnerable project, nor is a CPE not in the NVD') 
print ('  indicitive of a secure project.\n')
print ('* License information gathered using the scancode-toolkit-1.6.0 from nexB.\n')

