#Imports
import jsonlines
from PIL import Image
import os
import numpy as np

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms=None):
        global lst
        self.annotation_file=annotation_file
        self.transforms=transforms
        with jsonlines.open(annotation_file, 'r') as jsonl_f:
            lst = [obj for obj in jsonl_f]
        
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
     

    def __len__(self):
        i=0
        for obj in lst[0]:
            i=i+1
        return i
        '''
            return the number of data points in the dataset
        '''

    
    def __getann__(self, idx):
        self.idx=idx
        list =[]
        for i in range(len(idx)):
            for obj in range(len(lst)):
                for id in lst[obj]:
                    if id == idx[i]:
                        list.append(lst[obj][id])
        return list
        '''
            return the data items for the index idx as an object
        '''
        

    def __transformitem__(self, path):
        self.path=path
        '''
            return transformed PIL Image object for the image in the given path
        '''