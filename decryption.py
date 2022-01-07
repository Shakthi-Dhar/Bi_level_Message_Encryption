# importing the required libraries
# importing wavfile library to interact with .wav files
from scipy.io import wavfile

# initializing the original music or audio file
fs_e, data_e = wavfile.read('output_audio.wav')
# initializing the steganos/ hidden output audio file
fs_o, data_o = wavfile.read('original_song.wav')

# backtracking the information and rescaling
data = data_e[:, 1] - data_o[:, 1]
data = data*100

# saving the decrypted morse code message signal as morse_decrypted.wav
wavfile.write('morse_decrypted.wav', fs_o, data)
print("\nThe given audio file has been decrypted.")
