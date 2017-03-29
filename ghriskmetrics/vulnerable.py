# SPDX-License-Identifier: MIT

import sys, getopt

from os import path
from datetime import datetime

def search(args):		

	part = 'a'
	vendor = args[1]
	product = args[2]
	version = args[3]
	update = '-'
	edition = '-'
	language = '-'

	cpe = 'cpe:/a:' + vendor + ':' + product + ':' + version

	par_dir = path.dirname(path.realpath(__file__))
	gpa_dir = path.dirname(par_dir)
	nvd_dir = str(gpa_dir) + '/nvd/'
	filename = 'nvdcve-2.0-%d.xml'

	start_year = 2002
	end_year = datetime.now().year
	
	for year in range(start_year, end_year + 1):
		print ('searching %s' % filename.replace('%d', str(year)))
		with open(nvd_dir + filename.replace('%d', str(year)), 'r') as nvd:
			for line in nvd:
				if cpe in line:
					return True

	return False

