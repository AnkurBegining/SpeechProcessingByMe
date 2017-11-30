import scipy
from scipy.io.wavfile import read
from scipy.signal import hann
from scipy.fftpack import rfft
import matplotlib.pyplot as plt

# read audio samples
input_data = read("Sound/tabByAnkur1.wav")
audio = input_data[1]

# apply a Hanning window
window = hann(1024)
print(window)
audio = audio[0:1024] * window[1]

# fft
mags = abs(rfft(audio))

# convert to dB
mags = 20 * scipy.log10(mags)

# normalise to 0 dB max
mags -= max(mags)

# plot
plt.plot(mags.any())

# label the axes
plt.ylabel("Magnitude (dB)")
plt.xlabel("Frequency Bin")

# set the title
plt.title("Flute Spectrum")
plt.show()