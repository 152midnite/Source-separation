from lspo.SoundProcessor import sopro
from lspo import withNoName
import matplotlib.pyplot as plt 
import os.path
import numpy as np

path = os.getcwd()
parent = os.path.abspath(os.path.join(path, os.pardir))
sample = sopro([parent + '/chandelier.wav',parent + '/chandelier_track.wav'])
sample.cut_border_silence()
print ('number of samples is: {}\ntime in seconds is: {}\nand shape: {}'
	.format(sample.N, sample.t,sample.shape))



test_vocal = sample.vocal
test_track = sample.track
test_signal = 0.8*np.random.normal(size=len(test_vocal))
test_track = test_vocal+test_signal




plt.plot(test_track)
plt.show()

