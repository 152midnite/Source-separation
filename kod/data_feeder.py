import numpy as np
import soundfile as sf 

print((365700 - 334500)/44100)

def trackLoader(files, batch_size,song_size,samplerate):
    L = len(files) 
    while True:

        batch_start = 0
        batch_end = batch_size
        signals = np.zeros([1,batch_size,song_size*samplerate])
        for i in range(batch_size):
	       	with open(files[i],'rb') as file1:
	       		signal, samplerate = sf.read(file1)
	       		print('samplerate is ',samplerate)
	       	padding = song_size*samplerate-len(signal)
	       	signals[0,i,int(np.ceil(padding/2)):-1*int(np.floor(padding/2))]=signal

	        while batch_start < L:
	            limit = min(batch_end, L)
	            
	            yield [signals,None]
	            batch_start += batch_size   
	            batch_end += batch_size