import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram as specto
from scipy.misc import imsave
from soundfile import read as readsf
from scipy.io import wavfile
import os
import sys 
def specto_to_file(*files):
    for f in files:
        file1,fs = readsf(f)
        f,t,y = specto(file1,fs,nperseg=128)
        with open(str(files)+'.txt','w') as image:
            image.write(str(np.shape(y)))
def spectro(*files):
    for f in files:
        file1,fs = readsf(f)
        file1 = np.pad(file1,fs*2,'constant',constant_values=0)
        f,t,y = specto(file1,fs,nperseg=128)
        #imsave(str(files)+'.png',np.log(y))
        fig,ax = plt.subplots(1)
        fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
        ax.axis('off')
        im=ax.pcolormesh(t,f,np.log10(y))
        fig.savefig('sp_xyz.png', dpi=1000, frameon='false')
        #plt.savefig('sp_xyz.png')
        #plt.show()
def spect(*files):
    for f in files:
        #data, rate = readsf(f)
        rate, data = wavfile.read(f)
        data = np.pad(data,rate*2,'constant',constant_values=0)
        fig,ax = plt.subplots(1)
        fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
        ax.axis('off')
        pxx, freqs, bins, im = ax.specgram(x=data, Fs=rate, noverlap=384, NFFT=512)
        ax.axis('off')
        fig.savefig('sp_xyz.png', dpi=300, frameon='false')

specto_to_file('1.wav')   


