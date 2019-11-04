#! /bin/python

from vampl.SoundProcessor import sopro
import matplotlib.pyplot as plt 
import os.path

path = os.getcwd()
parent = os.path.abspath(os.path.join(path, os.pardir))
sample = sopro(['{}/chandelier.wav'.format(parent),'{}/chandelier_track.wav'.format(parent)])
#sample.cut_border_silence()
print ('number of samples is: {}\ntime in seconds is: {}\nand shape: {}'
        .format(sample.N, sample.t,sample.shape))
#corr,middle = sample.minimal_difference(3)
sample.phase_shift('chandelier_shifted')
#plt.plot(corr)
#plt.show()

