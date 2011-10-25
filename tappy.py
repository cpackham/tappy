"""
TAP producer for Python unittest framework

Usage in test script:

    if __name__ == "__main__":
        unittest.main(testRunner=tappy.TapTestRunner)
"""

import unittest
import sys
import time

class TapTestResult(unittest.TestResult):
    """A test result class that produces TAP compliant output.
    
    Used by TapTestRunner."""

    def __init__(self, stream, descriptions, verbosity):
        super(TapTestResult, self).__init__()
        self.stream = stream

    def startTest(self, test):
        super(TapTestResult, self).startTest(test)
        self.startTime = time.time()

    def addSuccess(self, test):
        super(TapTestResult, self).addSuccess(test)
        self.stream.write("ok %d - %s\n" % (self.testsRun, str(test)))

    def addFailure(self, test):
        super(TapTestResult, self).addFailure(test)
        self.stream.write("not ok - %d %s\n" % (self.testsRun, str(test)))

    def addError(self, test):
        super(TapTestResult, self).addError(test)
        self.stream.write("not ok %d - %s # ERROR\n" % (self.testsRun, str(test)))

    def addExpectedFailure(self, test, err):
        super(TapTestResult, self).addExpectedFailure(test, err)
        self.stream.write("not ok %d - %s # TODO known breakage\n" % (self.testsRun, str(test)))

    def addUnexpectedSuccess(self, test):
        super(TapTestResult, self).addUnexpectedSuccess(test)
        self.stream.write("ok %d - %s # TODO known breakage\n" % (self.testsRun, str(test)))

    def addSkip(self, test, reason):
        super(TapTestResult, self).addSkip(test, reason)
        self.stream.write("ok %d - %s # skip %s\n" % (self.testsRun, str(test), reason))

class TapTestRunner(unittest.TextTestRunner):
    """A test runner class that produces TAP compliant output."""

    resultclass = TapTestResult

    def __init__(self, stream=sys.stderr, descriptions=True, verbosity=1):
        super(TapTestRunner, self).__init__(stream, descriptions, verbosity)

    def _makeResult(self):
        return self.resultclass(self.stream, self.descriptions, self.verbosity)

    def run(self, test):
        self.stream.write("TAP version 13\n")
        self.stream.write("1..%d\n" % test.countTestCases())
        return super(TapTestRunner, self).run(test)

