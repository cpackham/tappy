"""
Main entry point when run as a module
"""
import sys
import unittest

import tappy

if sys.argv[0].endswith("__main__.py"):
    sys.argv[0] = "python -m tappy"

unittest.main(module=None, testRunner=tappy.TapTestRunner)
