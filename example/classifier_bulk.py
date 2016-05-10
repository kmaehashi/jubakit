#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

"""
Bulk Train-Test Classifier
========================================

This example uses bulk train-test method of Classifier.
"""

import sklearn.metrics

from jubakit.classifier import Classifier, Schema, Dataset, Config
from jubakit.loader.csv import CSVLoader

# Load a CSV file.
loader = CSVLoader('iris.csv')

# Define a Schema that defines types for each columns of the CSV file.
schema = Schema({
  'Species': Schema.LABEL,
}, Schema.NUMBER)

# Create a Dataset.
dataset = Dataset(loader, schema).shuffle()
n_samples = len(dataset)
n_train_samples = int(n_samples / 2)

# Create a Classifier configuration.
cfg = Config()

# Bulk train-test the classifier.
result = Classifier.train_and_classify(
  cfg,
  dataset[:n_train_samples],
  dataset[n_train_samples:],
  sklearn.metrics.classification_report
)

print(result)
