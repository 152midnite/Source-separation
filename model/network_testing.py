import matplotlib.pylab as P
from keras.models import Model, load_model
from keras.layers import Conv1D, Input
import numpy as np
import soundfile as sf 
from sklearn.utils import shuffle
from sklearn.cross_validation import train_test_split
import os


example,fs = sf.read('/home/dante/order/fuw/licencjat/kod/prepro/22.wav')
example = example[0:100000]


model = load_model('my_model.h5')
x1 = np.reshape(example,(1,100000,1))
x = model.predict(x1)
print(np.shape(x))

sf.write('network_result.wav',np.squeeze(x),fs)
#P.plot(np.squeeze(x))
P.show()