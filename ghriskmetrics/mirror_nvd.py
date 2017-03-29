#!/usr/bin/python

import requests
import zlib
import os

from datetime import datetime


url = 'https://nvd.nist.gov/feeds/xml/cve/'
base_filename = 'nvdcve-2.0-'
path = 'nvd/'
start_year = 2002
end_year = datetime.now().year

print ('Updating local mirror of National Vulnerability Database.')

if not os.path.exists(path):
    os.makedirs(path)

for year in range(start_year, end_year + 1):

	xml_filename = base_filename + str(year) + '.xml'
	meta_filename = base_filename + str(year) + '.meta'

	gz = requests.get(url + xml_filename + '.gz', stream=True)
	meta = requests.get(url + meta_filename, stream=True)

	lastDateModified = meta.text.split('\n')[0].strip()

	if (os.path.exists(path + xml_filename) 
		and os.path.exists( path + meta_filename)
		and lastDateModified == open(path + meta_filename, 'rt')
			.read().split('\n')[0].strip()):
		print ('Using cached version of %s' % xml_filename)
	else:
		print("Downloading %s" % meta_filename)
		with open(path + meta_filename, 'wb') as fd:
			for chunk in meta.iter_content(chunk_size=1024):
				fd.write(chunk)
		d = zlib.decompressobj(16+zlib.MAX_WBITS)
		print("Downloading %s" % xml_filename)
		with open(path + xml_filename, 'wb') as fd:
			for chunk in gz.iter_content(chunk_size=1024):
				fd.write(d.decompress(chunk))

print ('Local mirror up-to-date.')

