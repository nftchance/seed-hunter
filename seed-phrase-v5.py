import random
import sys
import threading

from itertools import permutations
from tqdm import tqdm
from web3 import Web3

print(f'Preparing seed cracking environment...')

targetAddress = '0xC399bd88A3471bfD277966Fef8e5110857e827Fc'

words = [
    [
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
        "obey",
        "couple",
    ],
    [
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
]

words_per_batch = int(12 / len(words))

counts = []
combinations = []

its_per_player = 0

w3 = Web3()

def get_combinations_lazy(counts):
    # loop through all the counts that we have
    for i in range(counts[0]):
        for j in range(counts[1]):
            yield (i, j)

def generate():
    print("Starting generation...")

    attempt = 0

    with tqdm(total=its_per_player) as pbar:
        print('Running simulation...')

        for i, j in get_combinations_lazy(counts):
            attempt += 1
            if attempt % 100000 == 0:
                pbar.update(100000)

            seed_phrase = ' '.join(
                combinations[0][i] + 
                combinations[1][j]
            )

            address = w3.toChecksumAddress(
                Web3.toHex(Web3.keccak(text=seed_phrase))[-40:])

            if address == targetAddress:
                print(f'Found it! {seed_phrase}')
                print(f'Attempts: {attempt}')
                sys.exit(0)

def main():
    print("Aggregating word combinations...")

    for batch in words:
        random.shuffle(batch)

        _combinations = list(permutations(batch, words_per_batch))
        combinations.append(_combinations)

        counts.append(len(_combinations))

    # use the length of combinations to determine the number of combinations
    # we need to iterate through
    unique_combinations = counts[0] * counts[1]

    print(f'Calculating {unique_combinations} combinations...')

    generate()

if __name__ == '__main__':
    main()
