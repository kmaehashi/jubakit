#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

"""
Using Weight Service
====================

This exampel illustrates how to use Weight engine to debug fv_converter
behavior (i.e. `converter` section of the config file).
"""

from jubakit.weight import Weight, Schema, Dataset, Config
from jubakit.loader.csv import CSVLoader

# Load a CSV file.
loader = CSVLoader('shogun.train.csv')

# Create a Dataset; schema will be auto-predicted.
dataset = Dataset(loader)

# Create a Weight Service.
cfg = Config()
weight = Weight.run(cfg)

# Show extracted features (online TF-IDF).
print('==== Features (online TF-IDF) ========================')
for (idx, result) in weight.update(dataset):
  print('Datum:')
  print('\t{0}'.format(dataset[idx]))
  print('Features:')
  for f in result:
    print('\t{0}\t{1}'.format(f.key, f.value))
  print('---------------------------------------')

# Show extracted features (batch TF-IDF)
print('==== Features (batch TF-IDF)  ========================')
for (idx, result) in weight.calc_weight(dataset):
  print('Datum:')
  print('\t{0}'.format(dataset[idx]))
  print('Features:')
  for f in result:
    print('\t{0}\t{1}'.format(f.key, f.value))
  print('---------------------------------------')

# Stop the service.
weight.stop()
