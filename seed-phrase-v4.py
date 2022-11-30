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

targetAddress = '0xC399bd88A3471bfD277966Fef8e5110857e827Fc'.lower()

time_started = time.time()

global_attempt = 0


def generate_bip39s():
    while True:
        seed = []
        for i in range(12):
            if i < 6:
                seed.append(random.choice(words_first_half))
            else:
                seed.append(random.choice(words_second_half))

        yield ' '.join(seed)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    global global_attempt

    with tqdm(total=factorial(12)) as pbar:
        for bip39 in generate_bip39s():
            global_attempt += 1

            if global_attempt % 100000 == 0:
                pbar.update(global_attempt)

            try:
                hex = '0x' + Web3.toHex(Web3.keccak(text=bip39))[24:]

                if hex.lower() == targetAddress:
                    print('found it!')
                    print(bip39)
                    sys.exit(0)
            except Exception as e:
                return None

if __name__ == '__main__':
    main()
