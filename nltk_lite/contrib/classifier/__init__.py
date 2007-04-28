# Natural Language Toolkit
#
# Author: Sumukh Ghodke <sumukh dot ghodke at gmail dot com>
#
# URL: <http://nltk.sf.net>
# This software is distributed under GPL, for license information see LICENSE.TXT
from nltk_lite.contrib.classifier.exceptions import invaliddataerror as inv
from nltk_lite.contrib.classifier import instances as ins, format

class Classifier:
    def __init__(self, training, attributes, klass, format):
        self.attributes = attributes
        self.klass = klass
        self.training = training
        self.format = format
        self.validate_training()
        
    def validate_training(self):
        if not self.training.are_valid(self.klass, self.attributes): 
            raise inv.InvalidDataError('Training data invalid.')
        if not self.can_handle_continuous_attributes() and self.attributes.has_continuous_attributes(): 
            raise inv.InvalidDataError('One or more attributes are continuous.')
    
    def test(self, path, printResults=True):
        raise AssertionError()
    
    def verify(self, path):
        raise AssertionError()
    
    def can_handle_continuous_attributes(self):
        return False


    