
import matplotlib.pyplot as plt, numpy as np
import soundfile as sf
import sys
import glob
import re


def slice(data,name,tresh=0.003,step=50,limit=2000):

    def cutter2(data,maximum,ans,step=100,padding=2):
        sums = np.zeros(int(len(data)/step))
        if len(sums)<=2*padding:
            return data
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


    with open(data,'rb') as file1:
        signal, samplerate = sf.read(file1)
    avg = np.std(signal)
    tresh = avg*tresh
    num = 1
    start = -1
    stop = 0
    for i in range(len(signal)):
        if not i%step == 0:
            continue
        elif np.sum(np.abs(signal[i:i+step]))>tresh:
            if start == -1:
                start = i
                #print('set start')
                continue
            else:
                #print('theres start already')
                continue
        elif np.sum(np.abs(signal[i:i+step]))<tresh: # maybe else?
            if start == -1:
                continue
            else:
                stop = i
                if (stop-start)/samplerate > 1 and (stop-start)/samplerate < 9 :
                    with sf.SoundFile(name+str(num)+'.wav','wb',samplerate,1) as file1:
                        try:
                            file1.write(signal[start:stop])
                        except:
                            file1.write(np.sum(signal[start:stop],axis=1))
                    #sf.write(name+str(num)+'.wav',signal[start:stop],samplerate)
                    num+=1
                    #print('found signal in '+ name+str(num)+'.wav')
                elif (stop-start)/samplerate>9:
                    ans = []
                    padding = 1000
                    answers = cutter2(signal[start:stop],9*samplerate,ans,step,padding)
                    for answer in answers:
                        try:
                            with sf.SoundFile(name+str(num)+'.wav','wb',samplerate,1) as file1:
                                file1.write(answer)
                        except:
                            with sf.SoundFile(name+str(num)+'.wav','wb',samplerate,1) as file1:
                                file1.write(np.sum(answer,axis=1))
                        num+=1
                start =-1
                stop = 0
        if num>limit:
            break


waves = glob.glob('/home/dante/order/fuw/licencjat/kod/dane/*.wav')
regx = '[a-z0-9_]+.wav$'
data = []
for i in waves:
    data.append(re.search(regx,i).group(0))
folder = '/home/dante/order/fuw/licencjat/kod/dane/'
print(data)
for i in data:
    print (folder+i,i)

    slice(folder+i,i)
    print_open_files()
