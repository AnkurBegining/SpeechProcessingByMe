from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# read audio samples
print("Enter the digit for the different Sound wave")
i=input('Enter your choice')
input_data = read("Sound/tabByAnkur1.wav")
if i== '1':
    input_data = read("Sound/tabByAnkur1.wav")
elif i== '2':
    input_data = read("Sound/tabByAnkur2.wav")
elif i== '3':
    input_data = read("Sound/tabByAnkur3.wav")
elif i== '4':
    input_data = read("Sound/tabByAnkur4.wav")
else:
    print("Sorry you don't have option other than this")

audio = input_data[1]
# plot the first 1024 samples
plt.plot(audio[0:1024])
# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time (samples)")
# set the title
plt.title("Tab Sample " + i)
# display the plot
plt.show()