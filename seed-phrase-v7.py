from web3 import Web3

w3 = Web3()

w3.eth.account.enable_unaudited_hdwallet_features()

seed_phrase = "please usage mobile genuine control when reflect duck burden gun entry donate"

account_path = "m/44'/60'/0'/0/0"

account = w3.eth.account.from_mnemonic(seed_phrase, account_path=account_path)

private_key = account.privateKey.hex()

print(private_key)

# address

address = account.address

print(address)

