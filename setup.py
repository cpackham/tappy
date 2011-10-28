from distutils.core import setup

with open('README') as file:
    long_description = file.read().strip()
with open('VERSION') as file:
    version = file.read().strip()

setup(name="Tappy",
    version=version,
    description="TAP producer for Python unittest framework",
    long_description=long_description,
    url="https://github.com/cpackham/tappy/",
    author="Chris Packham",
    author_email="judge.packham@gmail.com",
    license="GPLv2",
    packages=["tappy"],
    package_dir={'tappy':'.'},
    package_data={'tappy':['VERSION']})
