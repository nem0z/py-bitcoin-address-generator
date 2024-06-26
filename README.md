# py-bitcoin-address-generator

This project is mainly educational, as it's a practical application of what I'm learning / understanding about the bitcoin protocol and address through my own research.

Currently supported address format : 

### P2PKH
P2PKH (Pay to Public key Hash) is the legacy type of bitcoin address. It works by deriving the address from the public key (itself derived from the private key). To spend an output assigned to this address, all you need to do is sign your spending transaction with the private key used to generate the address, to prove that you're the owner.

## SegWit
SegWit (Segregated Witness) is a Bitcoin improvement that addresses transaction malleability and block size limitations. It separates transaction data (signatures and witness data) from the core transaction, making them more compact and allowing for more transactions per block.

### P2SH
A P2SH (Pay to Script Hash) address is an address secured by a redeem script. This script acts like a set of conditions that must be met in order to spend the funds. P2SH addresses are commonly used for multi-signature protection, but they can also be employed for timelock transactions.

### P2WPKH (bech32)
Pay to Witness Public Key Hash is the main type of SegWit address, easy to recognize because it starts with "bc1" for the main network address.

### P2TR (bech32m)
A Pay to Taproot address, also called a Bech32m address, is a type of address used in Bitcoin transactions to send payments to receivers who wish to be paid using a native witness v0 output. It's used to reduce the size of complexe transaction (ex: multisig) and improve privacy.

This project is inspired by <a href="https://github.com/BRO200BS/Bitcoin-Address-Generator" target="_blank">Bitcoin-Address-Generator</a> by BRO200BS.
Tools used for this project : <a href="https://cointools.org/valid-address-checker/" target="_blank">cointools.org/valid-address-checker/</a>