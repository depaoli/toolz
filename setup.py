#
# Distribution setup file
#
import re
from setuptools import setup, find_packages
from glob import glob


# scripts in bin/ with a shebang containing python will be
# recognized automatically
scripts = []
for fname in glob('bin/*'):
    with open(fname, 'r') as fh:
        if re.search(r'^#!.*python', fh.readline(160)):
            scripts.append(fname)

# if you have any python modules (.py files instead of dir/__init__.py
# packages) list them here:
py_modules = []

args = dict(
    # Application details
    name                = 'DePaoli-Toolz',
    long_description    = open('README.md').readline(160),
    version             = '0.0.1',
    author              = 'Matteo De Paoli',
    author_email        = 'depaoli@',
    url                 = 'https://github.com/depaoli/toolz',

    # Find Packages automatically but don't include those in "test" (ie. unittest)
    packages = find_packages(exclude=('test',)),
    # Define Package/s in test as Test Suite
    test_suite = "test",

    # Tells distribute to look for a MANIFEST.in file
    # and wrap-up all the entries that match inside the package itself
    # (rather than declaring "package_data" arg)
    include_package_data = True
)

setup(**args)
