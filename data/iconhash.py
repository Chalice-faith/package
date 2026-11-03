import base64, struct

def murmur3_32(data, seed=0):
    c1 = 0xcc9e2d51; c2 = 0x1b873593
    length = len(data); h1 = seed
    rounded_end = (length & 0xfffffffc)
    for i in range(0, rounded_end, 4):
        k1 = (data[i] & 0xff) | ((data[i+1] & 0xff) << 8) | ((data[i+2] & 0xff) << 16) | (data[i+3] << 24)
        k1 = (k1 * c1) & 0xffffffff
        k1 = ((k1 << 15) | (k1 >> 17)) & 0xffffffff
        k1 = (k1 * c2) & 0xffffffff
        h1 ^= k1
        h1 = ((h1 << 13) | (h1 >> 19)) & 0xffffffff
        h1 = (h1 * 5 + 0xe6546b64) & 0xffffffff
    k1 = 0
    val = length & 0x03
    if val == 3:
        k1 = (data[rounded_end + 2] & 0xff) << 16
    if val in (2, 3):
        k1 |= (data[rounded_end + 1] & 0xff) << 8
    if val in (1, 2, 3):
        k1 |= data[rounded_end] & 0xff
        k1 = (k1 * c1) & 0xffffffff
        k1 = ((k1 << 15) | (k1 >> 17)) & 0xffffffff
        k1 = (k1 * c2) & 0xffffffff
        h1 ^= k1
    h1 ^= length
    h1 ^= h1 >> 16
    h1 = (h1 * 0x85ebca6b) & 0xffffffff
    h1 ^= h1 >> 13
    h1 = (h1 * 0xc2b2ae35) & 0xffffffff
    h1 ^= h1 >> 16
    return h1 - 0x100000000 if h1 & 0x80000000 else h1

data = open(r'G:\GoProject\package\data\octodex-favicon.ico','rb').read()
b64 = base64.b64encode(data).decode()
print('size', len(data))
print('icon_hash', murmur3_32(b64.encode()))
# sanity check against mmh3 known vector
print('sanity', murmur3_32(b'foo'))
