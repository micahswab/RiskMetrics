# SPDX-License-Identifier: MIT

from ghriskmetrics import vulnerable

def test_vulnerability_found():
	args = ['', 'microsoft', 'internet_explorer', '6']
	assert vulnerable.search(args) == True

def test_vulnerability_not_found():
	args = ['', 'sadvbu2847v', 'asdkfba2315', '0.1.5']
	assert vulnerable.search(args) == False