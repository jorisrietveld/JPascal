# Author: Joris Rietveld <jorisrietveld@gmail.com>
# Created: 20-08-2017 13:52
# Licence: GPLv3 - General Public Licence version 3
from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='JPascal',
    version='0.0.1',
    description='An simple Pascal interpreter for educational use.',
    long_description=readme,
    author='Joris Rietveld',
    author_email='jorisrietveld@gmail.com',
    url='https://github.com/jorisrietveld/JPascal',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': [
            'jpascal = jpascal.__main__:main'
        ]
    }
)

