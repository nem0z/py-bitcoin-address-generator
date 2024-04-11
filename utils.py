from Cryptodome.Hash import SHA256, RIPEMD160

def checksum(payload: bytes) -> bytes:
    return SHA256.new(SHA256.new(payload).digest()).digest()[:4]


def hash160(payload: bytes) -> bytes:
        sha256hash = SHA256.new(payload).digest()
        return RIPEMD160.new(sha256hash).digest()