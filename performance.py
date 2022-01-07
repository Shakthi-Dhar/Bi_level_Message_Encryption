# importing the required libraries
from scipy.io import wavfile
import matplotlib.pyplot as plt

sr_me, data_me = wavfile.read("morse_encoded.wav")
sr_oa, data_oa = wavfile.read("morse_decrypted.wav")
error = []

for i in range(0, len(data_me)):
    if data_me[i] != 0:
        error.append(abs((data_oa[i]-data_me[i])/data_me[i]))
    else:
        error.append(abs(data_oa[i]))

print(sum(error)/len(error))
plt.plot(error, label='Error ratio',  color="red")
plt.title("Error Ratio")
plt.xlabel("Frames")
plt.ylabel("Error")

plt.show()
