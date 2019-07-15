from lspo.SoundProcessor import sopro
from lspo import withNoName
import matplotlib.pyplot as plt 


sample = sopro(['chandelier.wav','test.wav'])
print (sample.N, sample.t,sample.shape)
plt.plot(sample.T,sample.signals[0,:])
plt.axvline(sample.min_window(2,1)/sample.fs)
plt.show()