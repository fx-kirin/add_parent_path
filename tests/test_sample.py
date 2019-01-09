#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 zenbook <zenbook@zenbook-XPS>
#

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
import logzero
import import_parent_dir


def test_pass():
    import_parent_dir.import_parent(2)
    assert os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) in sys.path


if __name__ == "__main__":
    logzero.__name__ = ''
    logzero.setup_logger('')
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    pytest.main([__file__, '-k test_', '-s'])
