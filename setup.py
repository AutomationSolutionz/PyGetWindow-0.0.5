import re
from setuptools import setup, find_packages


version = '0.0.5'
long_description = 'long_description'

setup(
    name='PyGetWindow',
    version=version,
    url='https://github.com/asweigart/pygetwindow',
    author='Al Sweigart',
    author_email='al@inventwithpython.com',
    description=('A simple, cross-platform module for obtaining GUI information on application\'s windows.'),
    long_description='long_description',
    long_description_content_type="text/markdown",
    license='BSD',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    test_suite='tests',
    install_requires=['pyrect'],
    keywords="gui window geometry resize minimize maximize close title",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
)