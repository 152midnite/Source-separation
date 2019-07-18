from lspo.SoundProcessor import sopro
from lspo import withNoName
import matplotlib.pyplot as plt 
import os.path



path = os.getcwd()
parent = os.path.abspath(os.path.join(path, os.pardir))
sample = sopro([parent + '/chandelier.wav',parent + '/test.wav'])
print ('number of samples is: {}\ntime in seconds is: {}\nand shape: {}'
	.format(sample.N, sample.t,sample.shape))
#plt.plot(sample.T[-120000:-1],sample.vocal[-120000:-1],alpha=1)
sample.cut_border_silence()
plt.plot(sample.T,sample.vocal,alpha=0.6)
print ('\n\nnumber of samples is: {}\ntime in seconds is: {}\nand shape: {}'
	.format(sample.N, sample.t,sample.shape))
#plt.axvline(sample.min_window(2,1)/sample.fs)
plt.show()