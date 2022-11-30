import random
import sys
import time

from itertools import permutations
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
    "obey",
    "couple",
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

# shuffle the two lists
random.shuffle(words_first_half)
random.shuffle(words_second_half)

combinations_first_half = list(permutations(words_first_half, 6))
combinations_second_half = list(permutations(words_second_half, 6))

count_first_half, count_second_half = len(combinations_first_half), len(combinations_second_half)

targetAddress = '0xC399bd88A3471bfD277966Fef8e5110857e827Fc'

time_started = time.time()

w3 = Web3()

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def get_combinations_lazy():
    for i in range(count_first_half):
        for j in range(count_second_half):
            yield i, j

def main():
    # get player arg from command line
    players = 3
    its_per_player = count_first_half * count_second_half / players

    attempt = 0

    print(f'First half: {count_first_half} ({factorial(len(words_first_half))})')
    print(f'Second half: {count_second_half} ({factorial(len(words_second_half))})')

    print('Calculating combinations...')

    combinations = get_combinations_lazy()

    print('Running simulation...')

    with tqdm(total=its_per_player) as pbar:
        for i, j in combinations:
            attempt += 1
            if attempt % 50000 == 0:
                pbar.update(50000)

            seed_phrase = ' '.join(combinations_first_half[i] + combinations_second_half[j])
            address = w3.toChecksumAddress(Web3.toHex(Web3.keccak(text=seed_phrase))[-40:])

            if address == targetAddress:
                print(f'Found it! {seed_phrase}')
                print(f'Attempts: {attempt}')
                print(f'Time elapsed: {time.time() - time_started}')
                sys.exit(0)

if __name__ == '__main__':
    main()
