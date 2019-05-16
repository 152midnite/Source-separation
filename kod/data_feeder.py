import numpy as np
import soundfile as sf 
import re
from glob import glob
import soundfile as sf

def padarray(A, size):
    t = size - len(A)
    return np.pad(A, pad_width=(0, t), mode='constant')

def generate_batches(files,batch_size,song_size):
   counter = 0
   while True:
     fname = files[counter]
     print(fname)
     counter = (counter + 1) % len(files)
     with open(fname,'rb') as file1:
         signal, samplerate = sf.read(file1) 
     x_train = padarray(signal,song_size)
     y_train = padarray(signal,song_size)
     yield (np.array(x_train,), np.array(y_train,))
     #y_train = y_train.flatten()
     #for cbatch in range(0, X_train.shape[0], batch_size):
         #yield (X_train[cbatch:(cbatch + batch_size),:,:], y_train[cbatch:(cbatch + batch_size)])



def trackLoader(files, batch_size,song_size,samplerate):
    L = len(files) 

    while True:
        batch_start = 0
        batch_end = batch_size
        signals = np.zeros([song_size*samplerate])
        for i in range(batch_size):
	       	with open(files[i],'rb') as file1:
	       		signal, samplerate = sf.read(file1)
	       		print('samplerate is ',samplerate)
	       	padding = song_size*samplerate-len(signal)
	       	signals[int(np.ceil(padding/2)):-1*int(np.floor(padding/2))]=signal

	        while batch_start < L:
	            limit = min(batch_end, L)
	            print(len(signals))
	            yield [signals,signals]
	            batch_start += batch_size   
	            batch_end += batch_size

def file_finder(folder,example=0):
    waves = glob(folder+'*.wav')
    print(waves)
    example,samplerate = sf.read(waves[example])
    regx = '[a-z0-9_.]+.wav'
    data = []
    for i in waves:
        data.append(re.search(regx,i).group(0))
    return samplerate, waves,data


