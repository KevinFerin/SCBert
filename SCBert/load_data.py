#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:31:45 2020

@author: kevin
"""

import pandas as pd
import pkg_resources

class DataLoader : 
    
    def __init__(self) :
        pass
    

    def load_cls_fr(self):
        stream = pkg_resources.resource_stream(__name__, 'data/CLS-fr.csv')
        return pd.read_csv(stream) 
    