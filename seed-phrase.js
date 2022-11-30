const ethers = require('ethers');
const fs = require('fs');

const { FormatTypes } = require('ethers/lib/utils');

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

const targetAddress = '0xC399bd88A3471bfD277966Fef8e5110857e827Fc'

/// loop through every unique 12 word phrase that can be used as an ethereum seed phrase
/// without ever using the same word twice

const providerURL = "https://eth-mainnet.g.alchemy.com/v2/7hOvTTdNWW7ngDBuxt0RI4h91giaqhxP";
const provider = new ethers.providers.JsonRpcProvider(providerURL);

const generate = async () => { 
    /// create 50k unique combos of 12 words
    for (let i = 0; i < 400000000; i++) {
        let seed = [];
        let used = [];
        for (let j = 0; j < 12; j++) { 
            let word = words[Math.floor(Math.random() * words.length - 1)];

            /// if already used, try again
            if (used.includes(word)) {
                j--;
                continue;
            }

            seed.push(word);
            used.push(word);
        }

        try {
            // create a wallet with phrase
            let wallet = ethers.Wallet.fromMnemonic(seed.join(' '));

            console.log(wallet.address)

            if(wallet.address.toLocaleLowerCase() === targetAddress.toLocaleLowerCase())
                fs.writeFileSync('seed.txt', seed.join(' '))
        } catch(e) { 
            // console.log('Invalid', e);
        }
    }
}

generate();

