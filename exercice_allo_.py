import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

#red wav files 
freq_d,sampl_d = wavfile.read("F:/Multimedia/Dali.wav")
freq_s,sampl_s = wavfile.read("F:/Multimedia/Sahar.wav")
#print (len(sampl_s[:,0])/sampl_s)
#create the x axeis
axet_d=np.linspace(0,len(sampl_d)/freq_d,len(sampl_d))
axet_s=np.linspace(0,len(sampl_s)/freq_s,len(sampl_s))
#present the result
plt.subplot(3,1,1)
plt.ylabel("ampl")
plt.xlabel("Time")
plt.plot (axet_d,sampl_d[:,1])
plt.legend("d")
plt.subplot(3,1,3)
plt.xlabel("Time")
plt.ylabel("amplitude")
plt.plot(axet_s,sampl_s)
plt.legend("s")
plt.show()