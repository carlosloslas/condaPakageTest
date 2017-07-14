#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='condaPackageTest',
    packages=['condaPackageTest'],
    version='0.1',
    description='testing how to make an anaconda package',

    author='Carlos Losada',
    author_email='losadalastra.carlos@gmail.com',
    url='https://github.com/carlosloslas/condaPakageTest',
    license='MIT',
    python_requires='>=3',
    entry_points={'console_scripts': ['condaPackageTest = condaPackageTest:main']},
    zip_safe=False,
    classifiers=[
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish (should match 'license' above)
     'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3'
    ]
     )
