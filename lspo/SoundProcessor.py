import numpy as np 
import soundfile as sf

class sopro(object):
	"""docstring for songs processing (so-pro) class

	sound processing class."""
	
	def __init__(self, sounds):
		fss = np.zeros(len(sounds))

		sounds_dict = {}
		N = 0
		for sound_number,sound in enumerate(sounds):
			print('hi ',sound,' hi ',sound_number)
			sounds_dict[sound], fss[sound_number] = self.read_song(sounds[sound_number])
			if N < len(sounds_dict[sound]):
				N = len(sounds_dict[sound])
		signals = np.zeros([len(sounds),N])
		for sound_number, key in enumerate(sounds_dict):
			signals[sound_number,:len(sounds_dict[key])] = self.to_monaural(sounds_dict[key])

		self._signals = signals
		self._shape = np.shape(signals)
		self._N = self._shape[-1]
		self.fs = fss
		self._t = self.N/self.fs
		self._T = np.linspace(0,self.t,self.N)
		self._vocal = signals[0]
		self._track = signals[1]

	@property
	def signals(self):
		return self._signals
	@property
	def vocal(self):
		return self.signals[0]
	@property
	def track(self):
		return self.signals[1]
	@property
	def N(self):
		return len(self.signals[0])
	@property
	def shape(self):
		return np.shape(self.signals)
	@property
	def t(self):
		return self.N/self.fs
	@property
	def T(self):
		return np.linspace(0,self.t,self.N)

	def to_monaural(self,signal):
		if len(signal.shape)>1:
			return np.mean(signal,axis=1)
		else:
			return signal

	def read_song(self,sound):
		with open(sound,'rb') as file1:
		    signal, fs = sf.read(file1)
		return signal, fs

	def in_phase(self):
		max_power = self.max_window()
		print (max_power)
		

	def cut_border_silence(self,window_len=1000):
		'''If vocal starts later than the whole song 
		there is no need for the beginning (or end).

		This function takes window length to measure it's
		signal power and determine whether or not to cut signal shorter,
		both vocal and full track.

		window_len=1000 - number of samples in window to measure power of, more
		means more precision, poorer performance.

		This function works in place.'''
		tresh = np.max(np.abs(self.vocal))*0.0003
		step = int(np.floor(len(self.vocal)/window_len))
		i=0
		while np.sum(np.abs(self.vocal[step*i:step*(i+1)]))<tresh:
			i+=1
		i=1
		while np.sum(np.abs(self.vocal[step*i*-1-1:step*i*-1]))<tresh:
			i+=1
		self._signals = np.vstack([self._signals[0,:step*i*-1],self._signals[1,:step*i*-1]]) 

	def windows_power(self,window_len=0.5,noverlap=0.25):
		'''divides vocal into windows, calculates their overall power, returns
		that as a list, size of a step and indexes of middles of those windows.'''
		window_len, noverlap = window_len*self.fs[0], noverlap*self.fs[0]
		print(self.fs)
		step = int(np.floor(window_len-noverlap))
		sums = np.zeros(int(len(np.floor(self.vocal)/(step))))
		for i in range(len(sums)):
			sums[i] = np.sum(np.abs(self.vocal[i*(step):(i+1)*(step)]))
		return sums, step, np.arange(1,len(sums))*step

	def min_window(self,window_len=0.5,noverlap=0.25):
		'''Returns index lowest power part of a vocal
		window_len = 0.5 - in seconds, number of samples to measure power of
		noverlap = 0.25 - in seconds, how much two neighbor windows should overlap'''
		sums, step, middles = self.windows_power(window_len=0.5,noverlap=0.25)
		return (np.argmin(sums[1:-1])+1)*(step)

	def max_window(self,window_len=0.5,noverlap=0.25):
		sums, step, middles = self.windows_power(window_len=0.5,noverlap=0.25)
		return (np.argmax(sums[1:-1])+1)*(step)

	def cut_in_two(self):
		pass

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




