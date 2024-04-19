import hashlib

def checksum(payload: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]


def hash160(payload: bytes) -> bytes:
        sha256hash = hashlib.sha256(payload).digest()
        return hashlib.new('ripemd160', sha256hash).digest()