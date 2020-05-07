#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 00:01:10 2020

@author: kevin
"""

from setuptools import setup
from os import path

setup( name='SCB',
version='0.1',
description='Testing installation of Package globally',
url='#',
author='kferin',
packages=['SCB'],
zip_safe=False)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
# read the contents of requirements.txt
with open('requirements.txt',encoding='utf-8') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="SCB", # Replace with your own username
    version="0.0.1",
    author="Kevin Ferin",
    description="A small package to do Sentence Clustering with BERT (SCB)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KevinFerin/SCB",
    include_package_data=True,
    keywords=['sentence clustering', 'bert', 'keyword extraction',
              'sentence embedding', 'neural networks', 'flaubert', 'camembert'],
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
