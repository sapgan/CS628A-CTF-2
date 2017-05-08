#!/usr/bin/env python

def xor(s1, s2):
    res = [chr(0)]*8
    for i in range(len(res)):
        q = ord(s1[i])
        d = ord(s2[i])
        k = q ^ d
        res[i] = chr(k)
    res = ''.join(res)
    return res

with open('flag') as f:
    data = f.read()

with open('key') as f:
    key = f.read()

enc_data = ''
for i in range(0, len(data), 8):
    if i+8 <= len(data):
        enc = xor(data[i:i+8], key)
        enc_data += enc
    else:
        enc_data += data[i:]

with open('encrypted.out', 'wb') as f:
    f.write(enc_data)
