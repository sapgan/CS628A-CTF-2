# For File Generation
#!/bin/python
import random, string
def xor(a, b):
	return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))


lines = open("MSG",'r').readlines()
lines = [l.strip() for l in lines]


key = "$flag"
# print key

f =  open("encrypted.txt",'wb')

for l in lines:
	f.write(xor(key,l).encode('hex'))
	f.write("\n")
f.close()
