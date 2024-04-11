from wallet import Wallet

if __name__ == '__main__':
    wallet = Wallet()
    print(wallet.private_key)
    print(f"P2PKH addr : {wallet.P2PKH()}")
    print(f"Compressed P2PKH addr : {wallet.P2PKH(True)}")
    print(f"P2SH addr : {wallet.P2SH()}")
    print(f"SegWit bench32 addr : {wallet.bench32()}")