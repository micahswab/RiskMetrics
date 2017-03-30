# SPDX-License-Identifier: MIT

import os, json

from unittest import mock


def test_riskmetrics():
	par_dir = os.path.dirname(os.path.realpath(__file__))
	gpa_dir = os.path.dirname(par_dir)
	ggp_dir = os.path.dirname(gpa_dir)
	path = str(ggp_dir) + '/scancode-toolkit-1.6.0'

	with mock.patch('builtins.input', return_value=path):
		with mock.patch('builtins.input', return_value='microsoft'):
			with mock.patch('builtins.input', return_value='internet_explorer'):
				with mock.patch('builtins.input', return_value='6'):
					os.chdir('../')
					from riskmetrics import riskmetrics
					assert os.path.exists('info.json')

