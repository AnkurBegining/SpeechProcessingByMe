import matplotlib.pyplot as plt

from scipy.fftpack import fft
from scipy.io import wavfile # get the api

print("Enter the digit for the different Sound wave")
i=input('Enter your choice')
fs, data = wavfile.read('Sound/leftByAnkur1.wav')
if i== '1':
    fs, data = wavfile.read('Sound/leftByAnkur1.wav')
elif i== '2':
    fs, data = wavfile.read('Sound/leftByAnkur2.wav')
elif i== '3':
    fs, data = wavfile.read('Sound/leftByAnkur3.wav')
elif i== '4':
    fs, data = wavfile.read('Sound/leftByAnkur4.wav')

# load the data


# this is a two channel soundtrack, I get the first track
a = data.T[0]

# this is 8-bit track, b is now normalized on [-1,1)
b=[(ele/2**8.)*2-1 for ele in a]

# calculate fourier transform (complex numbers list)
c = fft(b)
# you only need half of the fft list (real signal symmetry)
d = len(c)/2
plt.ylabel("Magnitude")
plt.xlabel("frequency")
plt.title("Left Sample " + i)
plt.plot(abs(c[:int((d-1))]),'r')
plt.show()