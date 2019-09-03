from setuptools import setup
import sys,os

setup(
    name = 'rishi_requests',
    version = '0.1.0',
    description = 'Python test package',
    license='GPL v3',
    author = 'test',
    py_modules=['rishi_requests.py','config.py'],
    entry_points={
        'console_scripts': [
            'rishi_requests=rishi_requests:main'
        ]
    },
    classifiers = ['Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
)
