if True:
	import numpy as np
	from keras.models import Sequential as seq
	from keras.layers import LSTM
	from keras.layers import Input
	from keras import Model
	from keras.layers import Dense
	from keras.layers import RepeatVector
	from keras.layers import TimeDistributed
	from keras.utils import plot_model
	from data_feeder import trackLoader as tl,file_finder as ff, generate_batches as gb

epochs = 1
samplerate, signals, sample = ff('/home/dante/order/fuw/licencjat/kod/procd_data/')
batch_size = 1
song_size = 9*samplerate


encoding_dim = 32
input_img = Input(shape=(song_size,))
encoded = Dense(encoding_dim, activation='relu')(input_img)
decoded = Dense(song_size, activation='sigmoid')(encoded)
model = Model(input_img, decoded)
model.compile(optimizer='adadelta', loss='binary_crossentropy')


model.fit_generator(gb(signals,1,song_size),steps_per_epoch=1,epochs=1)

model.save('my_model.h5')
del model
