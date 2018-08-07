# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 12:53:06 2018

@author: muhammad.atta
"""

from keras.datasets import boston_housing
from keras import models
from keras import layers

(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()

print(train_data)