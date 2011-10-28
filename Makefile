#
# Makefile for tappy
#

ifeq ($(V),1)
	Q=
else
	Q=@
endif

all:
	$(Q)python setup.py build

VERSION:
	$(Q)git describe || printf '0.0\n' >$@

README:
	$(Q)printf "import __init__\nprint __init__.__doc__\n" \
		| python >$@

clean:
	$(Q)rm -f *.pyc

dist: VERSION README
	$(Q)python setup.py sdist
	$(Q)python setup.py bdist_rpm

dist-clean: clean
	$(Q)rm -f VERSION
	$(Q)rm -f README
	$(Q)rm -f MANIFEST
	$(Q)rm -rf dist
	$(Q)rm -rf build

.PHONY: all clean dist dist-clean
