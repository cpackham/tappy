from setuptools import setup

with open('README') as file:
    long_description = file.read().strip()
with open('VERSION') as file:
    version = file.read().strip()

setup(name="Tappy",
    version=version,
    description="TAP producer for Python nosetests framework",
    long_description=long_description,
    url="https://github.com/cpackham/tappy/",
    author="Chris Packham, Tobi Wulff",
    author_email="judge.packham@gmail.com",
    license="GPLv2",
    install_requires = ['nose>=0.11.1'],
    packages=['tappy'],
    entry_points = {'nose.plugins.0.10': ['tappy = tappy.tappy:Tappy']})
