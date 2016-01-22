import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-field_notebook',
    version='0.1',
    packages=['notebook'],
    include_package_data=True,
    license='BSD',  # example license
    description='A simple Django app for storing digital field objects.',
    long_description=README,
    url='https://github.com/andriesd/field-notebook.git',
    author='Daina Andries',
    author_email='andriesd@umich.edu',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Humanities and Social Science Researchers',
        'License :: OSI Approved :: BSD License', 
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2.7.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)