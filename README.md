# Bi_level_Message_Encryption

Data and information are extremely important in a variety of industries, such as military operations, and they demand high security. The main goal of this project is to tackle this problem by encoding specific text messages into an audio signal using Morse encoding. However, ordinary Morse encoding will not give the requisite security, therefore we will use Steganography techniques as a second level of encryption.

The entire process can be visualized in the below graph showing the original music/ audio file and the 1st level encoded morse audio file being merged (steganography) and the end result plot seems exactly the same as the original with the naked eyes, and also the sound is exactly the same as the original sound. However, decrypted this end result will give us the embedded message signal.
![Entire signal plot](https://github.com/Shakthi-Dhar/Bi_level_Message_Encryption/blob/master/plots/Encoding.png)

The Encrypted signal after processing the text message through morse encoding is as shown below:
![Encoded signal plot](https://github.com/Shakthi-Dhar/Bi_level_Message_Encryption/blob/master/plots/Encoded_signal.png)

The Decrypted signal after the 2nd step of steganography and obtaining the morse audio through decryption is as shown below:
![Decoded signal plot](https://github.com/Shakthi-Dhar/Bi_level_Message_Encryption/blob/master/plots/Decrypted_signal.png)
