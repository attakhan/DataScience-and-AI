# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 21:01:03 2018

@author: muhammad.atta
"""

import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

seed = 7 
np.random.seed(seed)
dataframe = pd.read_csv("sonar.csv", header=None)
dataset = dataframe.values

X = dataset[:,0:60].astype(float)
Y = dataset[:,60]


le = LabelEncoder()                
fitY = le.fit(Y)
transformY = le.transform(Y)


def create_baseline():
    model = Sequential()
    model.add(Dense(30,activation='relu',input_shape = ((X.shape[1],))))
    model.add(Dense(30, activation='relu'))
    model.add(Dense(1,activation='sigmoid'))
    model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])
    return model


''' without standardized '''
estimator = KerasClassifier(build_fn=create_baseline, epochs=100, batch_size=5, verbose=0)
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(estimator, X, transformY, cv=kfold)
print("Results: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))

scaler = StandardScaler()
print(scaler.fit(X))
print(scaler.transform(X))


''' with standardized '''
np.random.seed(seed)

estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasClassifier(build_fn=create_baseline, epochs=100, batch_size=5, verbose=0)))
pipeline = Pipeline(estimators)
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(pipeline, X, transformY, cv=kfold)
print("Standardized: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
