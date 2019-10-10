from vampl.SoundProcessor import sopro
from vampl import withNoName
import matplotlib.pyplot as plt 
import os.path
import numpy as np

path = os.getcwd()
parent = os.path.abspath(os.path.join(path, os.pardir))
sample = sopro([parent + '/chandelier.wav',parent + '/chandelier_track.wav'])
sample.cut_border_silence()
print ('number of samples is: {}\ntime in seconds is: {}\nand shape: {}'
	.format(sample.N, sample.t,sample.shape))


#sample.in_phase()
plt.plot(sample.partial_corr())


#plt.plot(sample.T,sample.vocal)
#plt.plot(sample.T,sample.track,alpha=0.5)
plt.show()

