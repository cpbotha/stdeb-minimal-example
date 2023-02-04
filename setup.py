import os
from setuptools import setup

setup(
    name = "myscript",
    version = "1.1",
    author = "Charl P. Botha",
    author_email = "cpbotha@vxlabs.com",
    description = "Demo of packaging a Python script as DEB",
    license = "BSD",
    url = "https://github.com/cpbotha/stdeb-minimal-example",
    packages=['myscript'],
    entry_points = {
        'console_scripts' : ['myscript = myscript.myscript:main']
    },
    data_files = [
        ('share/applications/', ['vxlabs-myscript.desktop'])
        ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
)

