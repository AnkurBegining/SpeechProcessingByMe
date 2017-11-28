from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# read audio samples
print("Enter the digit for the different Sound wave")
i=input('Enter your choice')
input_data = read("Sound/upByAnkur1.wav")
if i== '1':
    input_data = read("Sound/upByAnkur1.wav")
elif i== '2':
    input_data = read("Sound/upByAnkur2.wav")
elif i== '3':
    input_data = read("Sound/upByAnkur3.wav")
elif i== '4':
    input_data = read("Sound/upByAnkur4.wav")


audio = input_data[1]
# plot the first 1024 samples
plt.plot(audio[0:1024])
# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time (samples)")
# set the title
plt.title("Up Sample " + i)
# display the plot
plt.show()