from setuptools import setup, find_packages
import codecs
import os
import re

long_description = open(
    os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name="httpbin",
    version="0.3.0",
    description="HTTP Request and Response Service",
    long_description=long_description,

    # The project URL.
    url='https://github.com/ugurarpaci/httpbin.git',

    # Author details
    author='Ugur ARPACI',
    author_email='ugurarpaci@gmail.com',

    # Choose your license
    license='MIT',

    classifiers=[
         'Development Status :: 5 - Production/Stable',
         'Intended Audience :: Developers',
         'Natural Language :: English',
         'License :: OSI Approved :: MIT License',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2.7',
         'Programming Language :: Python :: 3.4',
    ],
    packages=find_packages(),
    include_package_data = True, # include files listed in MANIFEST.in
    install_requires=['Flask','MarkupSafe','decorator','itsdangerous','six'],
)
