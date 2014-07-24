from setuptools import setup
import os


VERSION = '1.0.0'


setup(
    author='Hassaan Ali Wattoo',
    author_email='hassaanaliw@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 2.7',

    ],
    description='Get information about a repository at Github.com',
    entry_points={
        'console_scripts': 'gitinfo=gitinfo:gitinfo',
    },
    include_package_data=True,
    keywords='analytics python github repo statistics',
    license='GPL',
    long_description=(
        open('README.rst').read() + '\n' + 
        open(os.path.join('docs', 'HISTORY.txt')).read() + '\n' +
        open(os.path.join('docs', 'CONTRIBUTORS.txt')).read()
    ),
    name='gitinfo',
    py_modules=[
        'gitinfo',
    ],

    url='https://github.com/hassaanaliw/gitinfo',
    version=VERSION,
    zip_safe=True,
)
