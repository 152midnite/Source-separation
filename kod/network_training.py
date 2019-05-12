from keras.models import Model
from keras.layers import Conv1D, Input
import numpy as np
import soundfile as sf 
from data_feeder import trackLoader as tl
import glob, re


example,samplerate = sf.read('/home/dante/order/fuw/licencjat/kod/prepro/sia_chandelier.wav17.wav')
print('here samplerate is ', samplerate)
batch_size=7
song_size = 9
epochs = 10

waves = glob.glob('/home/dante/order/fuw/licencjat/kod/prepro/*.wav')
regx = '[a-z0-9_.]+.wav'
data = []
for i in waves:
    data.append(re.search(regx,i).group(0))
print(len(data))



myinput = Input(shape=(batch_size, song_size*samplerate)) # shape = (BATCH_SIZE, 1D signal)
output = Conv1D(
    1, # output dimension is 1
    15, # filter length is 15
    padding="same")(myinput)

model = Model(inputs=myinput, outputs=output)

model.compile(loss='mse',
              optimizer='rmsprop',
              metrics=['mse'])

model.fit_generator(tl(waves,batch_size,song_size,samplerate),steps_per_epoch=batch_size, epochs=epochs)
model.save('my_model.h5')
del model
