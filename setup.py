from distutils.core import setup

long_description = open('README.rst', 'r').read()

setup(
    name='esoreader',
    py_modules=['esoreader'],  # this must be the same as the name above
    version='1.1.0',
    description='A module for parsing EnergyPlus *.eso files',
    #long_description=long_description,
    author='Daren Thomas',
    author_email='dthomas.ch@gmail.com',
    url='https://github.com/architecture-building-systems/esoreader',
    download_url='https://github.com/architecture-building-systems/esoreader/tarball/1.1',  # noqa
    keywords=['simulation', 'parsing', 'energyplus', 'pandas'],  # arbitrary keywords  # noqa
    classifiers=[],
)
