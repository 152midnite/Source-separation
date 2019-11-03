#! /bin/python

from vampl.SoundProcessor import sopro
import matplotlib.pyplot as plt 
import os.path
import numpy as np

path = os.getcwd()
parent = os.path.abspath(os.path.join(path, os.pardir))
sample = sopro(['{}/chandelier.wav'.format(parent),'{}/chandelier_track.wav'.format(parent)])
sample.cut_border_silence()
print ('number of samples is: {}\ntime in seconds is: {}\nand shape: {}'
        .format(sample.N, sample.t,sample.shape))

#sample.in_phase()
plt.plot(sample.partial_corr())
plt.show()

