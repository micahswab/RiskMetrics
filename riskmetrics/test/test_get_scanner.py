# SPDX-License-Identifier: MIT

from os import path
from riskmetrics import get_scanner


def test_get_scanner():
	par_dir = path.dirname(path.realpath(__file__))
	gpa_dir = path.dirname(par_dir)
	project_dir = str(path.dirname(gpa_dir)) + '/'
	scancode = 'scancode-toolkit-1.6.0'
	assert path.exists(project_dir + scancode) == True

		