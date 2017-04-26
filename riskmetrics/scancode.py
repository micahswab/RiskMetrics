# SPDX-License-Identifier: MIT

import requests

from os import path, remove
from subprocess import call

def install():
	"""
	Downloads and unzips nexB's ScanCode if it is not already installed.
	"""

	url = ('https://github.com/nexB/scancode-toolkit/releases'
		   '/download/v1.6.0/''scancode-toolkit-1.6.0.zip')

	parent_dir = path.dirname(path.realpath(__file__))
	project_dir = str(path.dirname(parent_dir)) + '/'
	scancode = 'scancode-toolkit-1.6.0'

	if path.exists(project_dir + scancode):
		print ('scancode-toolkit-1.6.0 already installed')
	else:
		print ('Downloading scancode-toolkit-1.6.0...')

		r = requests.get(url, stream=True)
		zipfile = project_dir + scancode + '.zip'
		with open(zipfile, 'wb') as fd:
			for chunk in r.iter_content(chunk_size=1024):
				fd.write(chunk)

		print ('Successfully downloaded')
		print ('Unzipping...')

		call(['unzip', zipfile])
		remove(zipfile)

		print ('Sucessfully unzipped')
		print ('scancode-toolkit-1.6.0 successfully installed')

		call([project_dir + scancode + '/scancode', '--help'])


def scan(filepath):
	"""
	Scan a directory with ScanCode.

	Args:
		filepath (str): The filepath to the directory to scan.
	"""
	par_dir = path.dirname(path.realpath(__file__))
	gpa_dir = path.dirname(par_dir)
	scancode = str(gpa_dir) + '/scancode-toolkit-1.6.0/scancode'

	call([scancode, '--format', 'json', filepath, 'info.json'])

