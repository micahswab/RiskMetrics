# SPDX-License-Identifier: MIT

from riskmetrics import nvd

from os import path, stat
from datetime import datetime

def test_update():
	nvd.update()

	par_dir = path.dirname(path.realpath(__file__))
	gpa_dir = path.dirname(par_dir)
	ggp_dir = path.dirname(gpa_dir)
	nvd_dir = str(ggp_dir) + '/nvd/'
	filename = 'nvdcve-2.0-%d.xml'

	start_year = 2002
	end_year = datetime.now().year

	assert path.exists(nvd_dir) == True
	for year in range(start_year, end_year + 1):
		nvd_file = nvd_dir + filename.replace('%d', str(year))
		assert path.exists(nvd_file)
		assert stat(nvd_file).st_size > 0


def test_succesful_search():
	term = "cpe:/o:linux:linux_kernel:2.6.20.1"
	assert nvd.search(term)


def test_unsuccesful_search():
	term = "*&#^GFKAL(HF#DQAO"
	assert not nvd.search(term)

		