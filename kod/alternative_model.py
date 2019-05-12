import matplotlib.pyplot as plt
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import RMSprop



model = Sequential()
model.add(Dense(output_dim=512, input_dim=x_test_VAD.shape[1], init='uniform'))
model.add(Activation('relu')) #relu softplus
model.add(Dropout(0.2))
model.add(Dense(output_dim=256, init='uniform'))#512
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(output_dim=128, init='uniform'))#256
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(output_dim=x_test_VAD.shape[1]))
model.add(Activation('sigmoid'))
    
model.compile(loss='binary_crossentropy', optimizer=RMSprop(lr = 0.001))
