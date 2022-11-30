import random
import sys
import threading
import time

from web3 import Web3

# 4/6 
# police
# drum
# wedding or marriage
# history or vintage


# is in a photoshoot setting

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

def generate_address(mnemonic):
    # generate the address from the seed phrase
        try:
            hex = '0x' + Web3.toHex(Web3.keccak(text=mnemonic))[24:]
            wallet = Web3.toChecksumAddress(hex)

            return wallet.lower()
        except Exception as e:
            return None

def generate():
    while True:
        seed_first = []
        seed_second = []
        for i in range(6):
            seed_first.append(random.choice(words_first_half))
            seed_second.append(random.choice(words_second_half))

            # Prevent duplicate terms
            if len(set(seed_first + seed_second)) != len(seed_first + seed_second):
                seed_first, seed_second = [], []
                continue

        global global_attempt
        global_attempt += 1

        if global_attempt % 100000 == 0:
            print(f'Attempt: {global_attempt}, Time: {time.time() - time_started}, Speed: {global_attempt / (time.time() - time_started)}', flush=True)

        mnemonic = ' '.join(seed_first + seed_second)

        wallet = generate_address(mnemonic)

        if wallet == targetAddress:
            print('found it!')
            print('seed phrase:', mnemonic)
            print('address:', wallet)
            sys.exit(0)

def main():
    threads = []
    ideal_threads = 10
    for i in range(ideal_threads):
        t = threading.Thread(target=generate)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == '__main__':
    main()
