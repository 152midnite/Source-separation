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

epochs = 100
samplerate, signals, sample = ff('/home/dante/order/fuw/licencjat/kod/procd_data/')
batch_size = 1
song_size = 9*samplerate


encoding_dim = 15
input_img = Input(shape=(song_size,))
encoded = Dense(encoding_dim,kernel_initializer='uniform', activation='relu')(input_img)
decoded = Dense(song_size,kernel_initializer='uniform', activation='sigmoid')(encoded)
model = Model(input_img, decoded)
model.compile(optimizer='sgd', loss='binary_crossentropy')

#print(np.shape(next(gb(signals,1,song_size))))
s = next(gb(signals,1,song_size))
print('this is a ',type(s))
print(np.array(s).shape)
print(np.array(s)[:,:,0:10])


model.fit_generator(gb(signals,1,song_size),steps_per_epoch=10,epochs=epochs)

model.save('my_model.h5')
print('reporting model saved')
del model
