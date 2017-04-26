# SPDX-License-Identifier: MIT

from riskmetrics import riskmetrics

def test_construct_cpe():
    cpe = riskmetrics.construct_cpe("vendor", "product", "0.1")
    assert cpe == 'cpe:/a:vendor:product:0.1'


def test_get_latest_version():
    version = riskmetrics.get_latest_version("35g3q", "fq34gf")
    assert version == ""

