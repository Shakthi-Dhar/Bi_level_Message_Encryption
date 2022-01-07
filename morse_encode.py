# importing the required libraries
# pygame and pydub are the audio toolkit in python that we have used for our project
import time
import pygame
from pydub import audio_segment

# creating a dictionary for all characters
ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

# path to audio files for each character
PATH = "morse_audio_wav/"


# function to check if the given string can be translated
def verify(string):
    keys = list(ENGLISH_TO_MORSE.keys())
    for char in string:
        if char not in keys and char != " ":
            print(f"The character {char} cannot be translated.")
            raise SystemExit


# function to convert text to morse audio file
def morse_encode():
    # input the text message
    print("\"English to Morse Code Audio Converter\"")
    print("Enter your message in English: ")
    message = input("-> ").upper()

    # calling the verify function to check for invalid characters in the sentence
    verify(message)
    pygame.init()
    # initializing an empty audio file to concatenate the characters
    combined = audio_segment.AudioSegment.empty()

    # character wise encoding of the message through for loop
    for char in message:
        if char == " ":
            # Separate the words with space sound
            print(" " * 3, end=" ")
            time.sleep(1.5)  # s
            sleep = audio_segment.AudioSegment.silent(500)  # ms
            combined = combined + sleep
        else:
            print(ENGLISH_TO_MORSE[char.upper()], end=" ")
            pygame.mixer.music.load(PATH + char + '_morse_code.wav')
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play()
            time.sleep(1)  # s
            # calling the audio file from the path
            sound = audio_segment.AudioSegment.from_file(PATH + char + '_morse_code.wav', format="wav")
            sleep = audio_segment.AudioSegment.silent(250)  # ms
            # concatenating all audio files
            combined = combined + sound + sleep

    combined.export("morse_encoded.wav", format="wav")
    print("\nThe given text message has completed first stage of encryption [Morse Encryption].")


# calling the function to convert text to morse audio encrypted wav file
morse_encode()
