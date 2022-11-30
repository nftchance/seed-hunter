import random
import sys
import threading

from web3 import Web3

# 3/6 
# police
# drum
# wedding or marriage or dress (?) (unknown)

# is in a photoshoot setting

words_first_half = [
    "police",
    "drum",
    "wedding",
    "marriage",
    "dress",
    "photo",
    "solider",
    "hat",
    "vintage",
    "mirror",
    "badge",
    "round",
    "obey",
    "vocal",
    "man",
    "woman",
    "uniform",
    "romance",
    "unveil",
    "couple",
    "old",
    "lamp",
    "history",
    "circle",
    "image",
    "picture",
    "badge",
    "roof"
    "doll"
    "comic",
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
    "field",
    "view",
    "open",
    "latin",
    "frame",
    "market",
    "curtain",
    "doll",
    "comic",
]

targetAddress = '0xC399bd88A3471bfD277966Fef8e5110857e827Fc'.lower()

global_attempt = 0

def generate():
    while True:
        seed = []
        used = []
        for j in range(6):
            word = words_first_half[random.randint(0, len(words_first_half) - 1)]

            if word in used:
                j -= 1
                continue

            seed.append(word)
            used.append(word)

        for j in range(6):
            word = words_second_half[random.randint(0, len(words_second_half) - 1)]

            if word in used:
                j -= 1
                continue

            seed.append(word)
            used.append(word)

        try:
            mnemonic = ' '.join(seed)
            hex = '0x' + Web3.toHex(Web3.keccak(text=mnemonic))[24:]
            wallet = Web3.toChecksumAddress(hex)

            if wallet.lower() == targetAddress:
                print('found wallet')
                print('seed: ' + mnemonic)
                sys.exit(0)
        except Exception as e:
            pass

        global global_attempt
        global_attempt += 1

        if global_attempt % 100000 == 0:
            print('attempt: ' + str(global_attempt))


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
