#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 00:01:10 2020

@author: kevin
"""



import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
# read the contents of requirements.txt
with open('requirements.txt',encoding='utf-8') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="SCBert", 
    version="0.0.2a",
    author="Kevin Ferin",
    author_email="siktime92@gmail.com",
    description="A small package to do Sentence Clustering with BERT (SCBert)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KevinFerin/SCB",
    include_package_data=True,
    keywords=['sentence clustering', 'bert', 'keyword extraction',
              'sentence embedding', 'neural networks', 'flaubert', 'camembert'],
    packages=['SCBert'],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
