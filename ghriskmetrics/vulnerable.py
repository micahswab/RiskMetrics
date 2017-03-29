#!/usr/bin/python

import sys, getopt

from datetime import datetime


if len(sys.argv) < 4:
	print ('usage: vulnerable.py vendor_name product_name version')
	sys.exit(2)

part = 'a'
vendor = sys.argv[1]
product = sys.argv[2]
version = sys.argv[3]
update = '-'
edition = '-'
language = '-'

cpe = 'cpe:/a:' + vendor + ':' + product + ':' + version

vulnerable = False
start_year = 2002
end_year = datetime.now().year

filename = 'nvd/nvdcve-2.0-%d.xml'

while not vulnerable:
	for year in range(start_year, end_year + 1):
		with open(filename.replace('%d', str(year)), 'r') as nvd:
			for line in nvd:
				if cpe in line:
					vulnerable = True
					break

