# importing the required libraries
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import wave

# plotting the original song
sr_os, data_os = wavfile.read("original_song.wav")
time_os = np.linspace(0, len(data_os) / sr_os, num=len(data_os))
plt.subplot(1, 3, 1)
plt.plot(time_os, data_os)
plt.title("Original Song")

# plotting the morse encoded audio file
sr_me, data_me = wavfile.read("morse_encoded.wav")
time_me = np.linspace(0, len(data_me) / sr_me, num=len(data_me))
plt.subplot(1, 3, 2)
plt.plot(time_me, data_me, color="green")
plt.title("Morse Encoded Audio")

# plotting the encrypted steganos/hidden audio file
sr_oa, data_oa = wavfile.read("output_audio.wav")
time_oa = np.linspace(0, len(data_oa) / sr_oa, num=len(data_oa))
plt.subplot(1, 3, 3)
plt.plot(time_oa, data_oa)
plt.title("Encrypted and Hidden Song")
plt.show()


# plotting the original morse audio file and decrypted audio file
wav_e = wave.open("morse_encoded.wav", "r")
raw_e = wav_e.readframes(-1)
raw_e = np.frombuffer(raw_e, "int16")

wav_d = wave.open("morse_decrypted.wav", "r")
raw_d = wav_d.readframes(-1)
raw_d = np.frombuffer(raw_d, "int16")

plt.plot(raw_e, color="blue")
plt.title("Encoded Morse audio signal")
plt.xlabel("Frames")
plt.show()
plt.plot(raw_d, color="green", alpha=0.5)
plt.title("Decrypted audio signal")
plt.xlabel("Frames")
plt.show()
