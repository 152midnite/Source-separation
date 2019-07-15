import numpy as np 
import soundfile as sf

class sopro(object):
	"""docstring for songs processing (so-pro) class

	sound processing class."""
	
	def __init__(self, sounds):
		signal0, fs0 = self.read_song(sounds[0])
		signals = np.zeros([len(sounds),len(signal0)])
		fss = np.zeros(len(sounds))
		for sound_number in range(len(sounds)):
			signals[sound_number,:], fss[sound_number] = self.read_song(sounds[sound_number])
		self.shape = np.shape(signals)
		self.N = self.shape[-1]
		self.fs = fss[0]
		self.t = self.N/self.fs
		self.T = np.linspace(0,self.t,self.N)
		self.signals = signals

	def read_song(self,sound):
		with open(sound,'rb') as file1:
		    signal, fs = sf.read(file1)
		return signal, fs

	def phase_zeroing():
		'''Shifting a capella track to match phase 
		of full song.'''
		pass

	def cut_border_silence(self):
		pass


	def windows_power(self,window_len=0.5,noverlap=0.25):
		'''divides vocal into windows, calculates their overall power, returns
		that as a list and indexes of middles of those windows.'''
		window_len, noverlap = window_len*self.fs, noverlap*self.fs
		step = int(np.floor(window_len-noverlap))
		sums = np.zeros(int(len(np.floor(self.signals[0])/(step))))
		for i in range(len(sums)):
			sums[i] = np.sum(np.abs(self.signals[0,i*(step):(i+1)*(step)]))
		return sums, step, range(1,len(sums))*step

	def min_window(self,window_len=0.5,noverlap=0.25):
		sums, step, middles = self.windows_power(window_len=0.5,noverlap=0.25)
		return (np.argmin(sums[1:-1])+1)*(step)

	def cut_in_two(self):
		if len(self.signal[0])<=2*self.fs:
			return self

		sums = np.zeros(int(len(data)/step))
		for i in range(len(sums)):
			sums[i]=np.sum(np.abs(data[i*step:i*step+step]))
		minimal_batch = np.argmin(sums[padding:-1*padding])+padding
		a = data[:step*minimal_batch-1*step]
		b = data[step*minimal_batch:]
		if len(a)>maximum:
			cutter2(a,maximum,ans,100,padding)
		else:
			ans.append(a)
		if len(b)>maximum:
			cutter2(b,maximum,ans,100,padding)
		else:
			ans.append(b)
		return ans




