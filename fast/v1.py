# Convert a 12-Word BIP-39 Mnemonic into a NumberPermalink

# Now let’s look at how we can convert a 12-word mnemonic into a number.

# First we need to convert each word into a number representing the index in the BIP-39 english wordlist:

# 20648817991329908116119611685044581221341

# Then we convert each number into a 11-bit binary number:

# 000110011100011110100011100000111101001100010111000110010010001001111101010010001010100000111111000001110010101001100010100101010101

# We then concatenate all of these binary numbers together to get a 132-bit number:

# 00011001110001111010001110000011110100110001011100011001001000100111110101001000101010000011111100000111001010100110001010010101

# We can get the last 4 bits (the checksum) by calculating the SHA-256 hash of this value and taking the first 4 bits of the result. In this case we get a checksum of 0101.

# We then compare the checksum we calculated to the checksum that was appended to the end of the mnemonic. If they match then we know that the mnemonic is valid.

# Finally we can convert this 128-bit number into a decimal number:

# 34,267,283,446,455,273,173,114,040,093,663,453,845

# This is how we can map any 12-word mnemonic to a number. This step only costs us 1 SHA-256 calculation.

import hashlib

indexes = [
    1,2,3,4,5,6,7,8,9,10,11,12
]

def binary(x):
    return '{0:011b}'.format(x)

def indexes_to_binary_string(indexes):
    return ''.join([binary(index) for index in indexes])

# binary_string = indexes_to_binary_string(indexes)
binary_string = "00011001110001111010001110000011110100110001011100011001001000100111110101001000101010000011111100000111001010100110001010010101"

# We can get the last 4 bits (the checksum) by calculating the SHA-256 hash of this value and taking the first 4 bits of the result. In this case we get a checksum of 0101.


def checksum(binary_string):
    sha256 = hashlib.sha256()
    sha256.update(binary_string.encode('utf-8'))
    return sha256.hexdigest()[:4]

# We then compare the checksum we calculated to the checksum that was appended to the end of the mnemonic. If they match then we know that the mnemonic is valid.

# print(checksum(binary_string))

# Finally we can convert this 128-bit number into a decimal number:

def binary_string_to_decimal(binary_string):
    return int(binary_string, 2)

print(binary_string_to_decimal(binary_string))

# This is how we can map any 12-word mnemonic to a number. This step only costs us 1 SHA-256 calculation.