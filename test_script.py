from lspo.SoundProcessor import sopro
from lspo import withNoName


sample = sopro(['network_result.wav','test.wav'])
print (sample.N, sample.t,sample.shape)
print (sample.idk())
