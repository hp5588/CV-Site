#!/usr/bin/env python

from setuptools import setup

setup(name='cv-site-powen.kao',
      version='1.0',
      description='CV site built on django',
      author='Po-Wen Kao',
      author_email='hp5588@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      install_requires=[
            "Django==3.0.7",
            "django-cors-headers==3.4.0",
            "Pillow==8.2.0",
            "django-cleanup==5.0.0",
      ]
      )
