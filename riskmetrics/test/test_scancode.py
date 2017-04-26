# SPDX-License-Identifier: MIT

from os import path, remove
from riskmetrics import scancode as sc

def test_install():
	sc.install()

	par_dir = path.dirname(path.realpath(__file__))
	gpa_dir = path.dirname(par_dir)
	project_dir = str(path.dirname(gpa_dir)) + '/'
	scancode = 'scancode-toolkit-1.6.0'
	assert path.exists(project_dir + scancode) == True


def test_scan():
	sc.scan(__file__)
	assert path.exists('info.json')
	remove('info.json')

		