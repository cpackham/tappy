tappy
=====

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

See also
--------
* https://github.com/mblayman/tappy
