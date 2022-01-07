# importing the required libraries
# importing wavfile library to interact with .wav files
from scipy.io import wavfile

# initializing the original music or audio file
fs_o, data_o = wavfile.read('original_song.wav')
fs_m, data_m = wavfile.read('morse_encoded.wav')
data_m_scaled = data_m/100

# manipulating/ tampering with the original audio file to hide the message, if mono then no need to specify channel
data_o[0:len(data_m_scaled), 1] = data_m_scaled + data_o[0:len(data_m_scaled), 1]

wavfile.write('output_audio.wav', fs_o, data_o)
print("\nThe given text message has completed second stage of encryption [Steganography].")
