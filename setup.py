from distutils.core import setup
import os


long_description = 'see the GitHub repository for more information: https://github.com/architecture-building-systems/esoreader'  # noqa
if os.path.exists('README.rst'):
    long_description = open('README.rst').read()


setup(
    name='esoreader',
    py_modules=['esoreader'],  # this must be the same as the name above
    version='1.2.1',
    description='A module for parsing EnergyPlus *.eso files',
    long_description=long_description,
    author='Daren Thomas',
    author_email='thomas@arch.ethz.ch',
    url='https://github.com/architecture-building-systems/esoreader',
    download_url='https://github.com/architecture-building-systems/esoreader/archive/1.2.1.tar.gz',  # noqa
    keywords=['simulation', 'parsing', 'energyplus', 'pandas'],  # arbitrary keywords  # noqa
    classifiers=[],
)
