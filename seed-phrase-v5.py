import random
import sys
import threading
import time

from tqdm import tqdm
from web3 import Web3

# 4/6
# police
# drum
# wedding or marriage
# history or vintage

words_first_half = [
    "police",
    "drum",
    "wedding",
    "marriage",
    "hat",
    "vintage",
    "vocal",
    "man",
    "woman",
    "uniform",
    "old",
    "history",
    "image",
    "gaze",
    "obey"
]

# 4/6
# window
# forest
# mountain
# sun

# previous set had a ton of mirror, mirror is somewhere in here i think it was lost to window this iteration

words_second_half = [
    "mirror",
    "window",
    "frame",
    "light",
    "brush",
    "leaf",
    "scene",
    "sun",
    "forest",
    "mountain",
    "album",
    "flower",
    "escape",
    "room",
    "small",
    "embrace",
    "picture",
    "view",
    "open",
    "latin",
    "frame",
    "market",
    "curtain",
]

targetAddress = '0xC399bd88A3471bfD277966Fef8e5110857e827Fc'

time_started = time.time()

global_attempt = 0

w3 = Web3()

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    global global_attempt

    with tqdm(total=factorial(12)) as pbar:
        while True:
            random.shuffle(words_first_half)
            random.shuffle(words_second_half)

            # create seed phrase of 12 words
            seed_phrase = " ".join((words_first_half + words_second_half)[:12])

            global_attempt += 1

            if global_attempt % 100000 == 0:
                pbar.update(global_attempt)

            # get address from seed phrase
            address = w3.toChecksumAddress(Web3.toHex(Web3.keccak(text=seed_phrase))[-40:])

            if address == targetAddress:
                print(f"Found address in {global_attempt} attempts")
                print(f"Seed phrase: {seed_phrase}")
                print(f"Address: {address}")
                print(f"Time elapsed: {time.time() - time_started}")
                sys.exit()

if __name__ == '__main__':
    main()
