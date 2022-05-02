"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='alieninvasion',
    version=1.0,
    description='Alien Invasion Game Project',
    long_description=long_description,
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/pypa/sampleproject',  # Optional
    author='Piyu Tiwari',
    author_email='piyumishra@gmail.com',
    packages=find_packages(exclude=['test']),  # Required
    install_requires=[
        'requests',
        'pandas',
        'pyodbc',
        'sqlalchemy'
    ],
    extras_require={
        'test': ['pytest', 'ipdb', 'coverage', 'pytest-cov', 'pytest-pep8'],
    }
)
