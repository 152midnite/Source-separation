#!/usr/bin/python
import glob 
import sys
import os
if sys.argv[1] in ['h','help']:
    print ('''this is a preprocessing script\
            takes folder path as a folder of\
            data to pass (with files of *.wav\
            format.''')

dirname = os.getcwd()
parent_dir = os.path.abspath(os.path.join(dirname, os.path.pardir))
data_directory = sys.argv[1]

