import random
import sys
import threading

from web3 import Web3

words = [
    "vintage",
    "comic",
    "police",
    "window",
    "latin",
    "dress",
    "curtain",
    "image",
    "picture",
    "forest",
    "mirror",
    "window",
    "badge",
    "roof",
    "stand",
    "prison",
    "regret",
    "danger",
    "doll",
    "uniform",
    "woman",
    "man",
    "photo",
    "art",
    "history",
    "word",
    "image",
    "marriage",
    "wedding",
    "funny",
    "movie",
    "frame",
    "market",
    "laugh",
    "romance",
    "web",
    "unveil",
    "couple",
    "round",
    "old",
    "book",
    "drawing",
    "house",
    "lamp",
    "door",
    "circle",
    "brown"
]

targetAddress = '0xC399bd88A3471bfD277966Fef8e5110857e827Fc'.lower()

attempts = 500000000

global_attempt = 0

def generate():
    for i in range(attempts):
        seed = []
        used = []
        for j in range(12):
            word = words[random.randint(0, len(words) - 1)]

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

        if global_attempt % 1000 == 0:
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
