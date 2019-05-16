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


epochs = 10
samplerate, signals, sample = ff('/home/dante/order/fuw/licencjat/kod/procd_data/')
batch_size = 1
song_size = 9*samplerate

x_train = np.zeros(shape=(5358, 300, 54))
y_train = np.zeros(shape=(5358, 1))

input_layer = Input(shape=(batch_size,song_size))
lstm = LSTM(10)(input_layer)
dense1 = Dense(20, activation='relu')(lstm)
dense2 = Dense(song_size, activation='sigmoid')(dense1)

model = Model(inputs=input_layer, outputs=dense2)
model.compile("adam", loss='binary_crossentropy')

for layer in model.layers:
    print(layer.output_shape)
#exit()

model.fit_generator(gb(signals,1,song_size),steps_per_epoch=batch_size, epochs=epochs)
model.save('my_model.h5')
del model
