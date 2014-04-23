#from setuptools import setup
from distutils.core import setup

long_description = open('README.rst', 'r').read()

setup(
    name='esoreader',
    py_modules=['esoreader'],  # this must be the same as the name above
    version='1.0.0',
    description='A module for parsing EnergyPlus .ESO files',
    long_description=long_description,
    author='Daren Thomas',
    author_email='dthomas.ch@gmail.com',
    url='https://github.com/daren-thomas/esoreader',
    #download_url=
        #'https://github.com/daren-thomas/esoreader/archive/master.tar.gz',
    keywords=['simulation', 'parsing', 'energyplus'],  # arbitrary keywords
    classifiers=[],
)
