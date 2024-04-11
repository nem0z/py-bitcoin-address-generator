import ecdsa
import base58
import bech32

from utils import checksum, hash160

class Wallet():
    def __init__(self):
        self.private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

    def get_xy(self) -> tuple[bytes, bytes]:
        vk = self.private_key.get_verifying_key()
        return vk.pubkey.point.x(), vk.pubkey.point.y()

    def get_xy_as_hex(self) -> tuple[str, str]:
        vk = self.private_key.get_verifying_key()
        x = vk.pubkey.point.x().to_bytes(32, 'big').hex()
        y = vk.pubkey.point.y().to_bytes(32, 'big').hex()
        return x, y

    def get_public_key(self) -> str:
        x, y = self.get_xy_as_hex()
        return f"04{x}{y}"

    def get_compressed_public_key(self) -> str:
        x,y = self.get_xy()
        prefix = '02' if y % 2 == 0 else '03'
    
    def P2PKH(self, compressed = False) -> str:
        public_key = self.get_compressed_public_key() if compressed else self.get_public_key()
        h160 = hash160(bytes.fromhex(public_key))
        public_key_hash = b'\x00' + h160
        cksum = checksum(public_key_hash)
        p2pkh_address_bytes = public_key_hash + cksum
    
    def P2SH(self) -> str:
        h160 = hash160(bytes.fromhex(self.get_public_key()))
        redeem_script = b'\x24' + h160
        h160 = hash160(redeem_script)
        script_hash = b'\x05' + h160
        cksum = checksum(script_hash)
        return base58.b58encode(script_hash + cksum)
    
