#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='django_cms_medusa',
    version='0.1',
    description='django_medusa renderer for django_cms',
    long_description='\n\n'.join([
        open('README.rst').read(),
        open('CHANGES.txt').read(),
    ]),
    author='OCHIAI, Gouji',
    author_email='gjo.ext@gmail.com',
    url='https://github.com/gjo/django_cms_medusa',
    license='BSD',
    packages=find_packages(),
    zip_safe=True,
    install_requires=('django_cms', 'django_medusa'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
)
