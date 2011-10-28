"""
TAP producer for Python unittest framework

Tappy builds on top of the standard unittest framework provides
TestRunner and TestResult classes that together produce TAP compliant
output, see http://testanything.org/ for more info on the TAP format. 

Simple usage:

    import unittest
    import tappy

    class MyTestCase(unittest.TestCase):
        ...

    if __name__ == "__main__":
        unittest.main(testRunner=tappy.TapTestRunner)

Tappy can also be used in place of the unittest module on the
commandline.

Instead of typing:

    python -m unittest

You can type:

    python -m tappy

---

Copyright (c) 2011 Chris Packham

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2 as
published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__all__ = ['TapTestResult', 'TapTestRunner']
