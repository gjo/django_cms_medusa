#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='django_cms_medusa',
    description='django_medusa renderer for django_cms',
    version='0.1',
    packages=find_packages(),
    url='',
    license='BSD',
    author='OCHIAI, Gouji',
    author_email='gjo.ext@gmail.com',
    install_requires=('django_cms', 'django_medusa'),
)
