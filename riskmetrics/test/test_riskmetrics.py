# SPDX-License-Identifier: MIT

import os, sys, json, subprocess, unittest

from unittest.mock import patch, MagicMock
from contextlib import contextmanager
from io import StringIO

class TestRiskMetrics(unittest.TestCase):

    @contextmanager
    def captured_output():
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    @patch('subprocess.run')
    def test_riskmetrics(self, mock_run):
        mock_run.return_value = MagicMock(json.loads('{"scancode_notice":"Generated...","scancode_version":"1.6.0","resource_count":1,"results":[{"location":"/Users/micahswab/a/scancode-toolkit-1.6.0.zip","copyrights":[],"licenses":[{"key":"apache-2.0","score":100,"short_name":"Apache 2.0","category":"Attribution","owner":"Apache Software Foundation","homepage_url":"http://www.apache.org/licenses/","text_url":"http://www.apache.org/licenses/LICENSE-2.0","dejacode_url":"https://enterprise.dejacode.com/license_library/Demo/apache-2.0/","spdx_license_key":"Apache-2.0","spdx_url":"http://spdx.org/licenses/Apache-2.0","start_line":4,"end_line":4},{"key":"apache-1.1","score":100,"short_name":"Apache 1.1","category":"Attribution","owner":"Apache Software Foundation","homepage_url":"http://www.apache.org/licenses/","text_url":"http://apache.org/licenses/LICENSE-1.1","dejacode_url":"https://enterprise.dejacode.com/license_library/Demo/apache-1.1/","spdx_license_key":"Apache-1.1","spdx_url":"http://spdx.org/licenses/Apache-1.1","start_line":239,"end_line":239},{"key":"apache-2.0","score":100,"short_name":"Apache 2.0","category":"Attribution","owner":"Apache Software Foundation","homepage_url":"http://www.apache.org/licenses/","text_url":"http://www.apache.org/licenses/LICENSE-2.0","dejacode_url":"https://enterprise.dejacode.com/license_library/Demo/apache-2.0/","spdx_license_key":"Apache-2.0","spdx_url":"http://spdx.org/licenses/Apache-2.0","start_line":240,"end_line":240},{"key":"lgpl","score":100,"short_name":"LGPL","category":"Copyleft Limited","owner":"Free Software Foundation (FSF)","homepage_url":"","text_url":"","dejacode_url":"https://enterprise.dejacode.com/license_library/Demo/lgpl/","spdx_license_key":"","spdx_url":"","start_line":246,"end_line":246},{"key":"agpl-1.0","score":100,"short_name":"AGPL 1.0","category":"Copyleft","owner":"Affero","homepage_url":"http://www.affero.org/oagpl.html","text_url":"http://www.affero.org/oagpl.html","dejacode_url":"https://enterprise.dejacode.com/license_library/Demo/agpl-1.0/","spdx_license_key":"AGPL-1.0","spdx_url":"http://spdx.org/licenses/AGPL-1.0","start_line":1281,"end_line":1281},{"key":"agpl-1.0","score":100,"short_name":"AGPL 1.0","category":"Copyleft","owner":"Affero","homepage_url":"http://www.affero.org/oagpl.html","text_url":"http://www.affero.org/oagpl.html","dejacode_url":"https://enterprise.dejacode.com/license_library/Demo/agpl-1.0/","spdx_license_key":"AGPL-1.0","spdx_url":"http://spdx.org/licenses/AGPL-1.0","start_line":1282,"end_line":1282},{"key":"agpl-1.0","score":100,"short_name":"AGPL 1.0","category":"Copyleft","owner":"Affero","homepage_url":"http://www.affero.org/oagpl.html","text_url":"http://www.affero.org/oagpl.html","dejacode_url":"https://enterprise.dejacode.com/license_library/Demo/agpl-1.0/","spdx_license_key":"AGPL-1.0","spdx_url":"http://spdx.org/licenses/AGPL-1.0","start_line":1283,"end_line":1283},{"key":"agpl-2.0","score":100,"short_name":"AGPL 2.0","category":"Copyleft","owner":"Affero","homepage_url":"http://www.affero.org/agpl2.html","text_url":"http://www.affero.org/agpl2.html","dejacode_url":"https://enterprise.dejacode.com/license_library/Demo/agpl-2.0/","spdx_license_key":"","spdx_url":"","start_line":1284,"end_line":1284},{"key":"agpl-2.0","score":100,"short_name":"AGPL 2.0","category":"Copyleft","owner":"Affero","homepage_url":"http://www.affero.org/agpl2.html","text_url":"http://www.affero.org/agpl2.html","dejacode_url":"https://enterprise.dejacode.com/license_library/Demo/agpl-2.0/","spdx_license_key":"","spdx_url":"","start_line":1286,"end_line":1286},{"key":"agpl-3.0","score":100,"short_name":"AGPL 3.0","category":"Copyleft","owner":"Free Software Foundation (FSF)","homepage_url":"http://www.fsf.org/licensing/licenses/agpl-3.0.html","text_url":"http://www.fsf.org/licensing/licenses/agpl-3.0.html","dejacode_url":"https://enterprise.dejacode.com/license_library/Demo/agpl-3.0/","spdx_license_key":"AGPL-3.0","spdx_url":"http://spdx.org/licenses/AGPL-3.0","start_line":1287,"end_line":1287},{"key":"agpl-3.0","score":100,"short_name":"AGPL 3.0","category":"Copyleft","owner":"Free Software Foundation (FSF)","homepage_url":"http://www.fsf.org/licensing/licenses/agpl-3.0.html","text_url":"http://www.fsf.org/licensing/licenses/agpl-3.0.html","dejacode_url":"https://enterprise.dejacode.com/license_library/Demo/agpl-3.0/","spdx_license_key":"AGPL-3.0","spdx_url":"http://spdx.org/licenses/AGPL-3.0","start_line":1291,"end_line":1291}],"packages":[{"type":"plain zip","packaging":"archive","primary_language":"null"}]}]}'))

        par_dir = os.path.dirname(os.path.realpath(__file__))
        gpa_dir = os.path.dirname(par_dir)
        ggp_dir = os.path.dirname(gpa_dir)
        path = str(ggp_dir) + '/scancode-toolkit-1.6.0'

        with patch('builtins.input', return_value=path):
            with TestRiskMetrics.captured_output() as (out, err):
                os.chdir('../')
                from riskmetrics import riskmetrics

        output = out.getvalue().strip()
        self.assertEqual(output, 'Results:\n\n{\n  "Number of files with a license": 1,\n  "Number of files without a license": 0,\n  "Types of licenses": [\n    "Apache 2.0",\n    "Apache 1.1",\n    "LGPL",\n    "AGPL 1.0",\n    "AGPL 2.0",\n    "AGPL 3.0"\n  ],\n  "CPE located in NVD": false\n}\n\nNotes:\n\n* A Common Platform Enumeration (CPE) in the National Vulnerability Database (NVD)\n  is not necessarily indicitive of a vulnerable project, nor is a CPE not in the NVD\n  indicitive of a secure project.\n\n* License information gathered using the scancode-toolkit-1.6.0 from nexB.')
