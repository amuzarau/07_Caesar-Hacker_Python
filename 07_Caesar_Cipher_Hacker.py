"""Caesar Cipher Hacker
This program hacks messages encrypted with the Caesar cipher by doing
a brute force attack against every possible key.
More info at:
https://en.wikipedia.org/wiki/Caesar_cipher#Breaking_the_cipher"""

print('Caesar Cipher Hacker')

# Let the user specify the message to hack:
print('Enter the encrypted Casear cipher message to hack.')
message = input('> ')

# Every possible symbol that can be encrypted/decrypted:
# (This must match the SYMBOLS used when encrypting the message.)

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)): # Loop through every possible key.
    translated = ''

    # Decrypt each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)  # Get the number of the symbol.
            num -= key

            num = num - key # Decrypt the number.

            #Handle the wrap-around if num is less than 0:
            if num < 0:
                num += len(SYMBOLS)

            # Add decrypted number's symbol to translated:
            translated += SYMBOLS[num]
        else:
            # Just add the symbol without decrypting:
            translated += symbol

    # Display the key being tested, along with its decrypted text:
    print(f'Key #{key}: {translated}')
