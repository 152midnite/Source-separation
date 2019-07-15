import numpy as np 
import soundfile as sf

class sopro(object):
	"""docstring for songs processing (so-pro) class

	sound processing class."""
	
	def __init__(self, sounds):
		signal0, fs0 = self.read_song(sounds[0])
		signals = np.zeros([len(sounds),len(signal0)])
		fss = np.zeros(len(sounds))
		for sound_number in range(len(sounds))[1:-1]:
			signals[sound_number,:], fss[sound_number] = self.read_song(sound[sound_number])
		self.shape = np.shape(signals)
		self.N = self.shape[-1]
		self.fs = fss[0]
		self.t = self.N/self.fs
		self.signals = signals

	def read_song(self,sound):
		with open(sound,'rb') as file1:
		    signal, fs = sf.read(file1)
		return signal, fs

	def phase_zeroing():
		'''Shifting a cappella track to match phase 
		of full song.'''
		pass

	def idk(self):
		return np.mean(self.signals,axis=0)


