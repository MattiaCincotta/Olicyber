from Crypto.Util.number import bytes_to_long

p = 23915490258985334837
q = 23148527363907102529
n = p*q
print (n)

phi = (p-1)*(q-1)
print(phi)
e = 65537

d = pow(e,-1,phi)
print(d)

stringa = "Shamir"

temp  = bytes_to_long(stringa.encode())
c = pow(temp, e, n)
print (c)

CHIAVE = 0x163c3204a74d482d816312e2192430ae8

result = pow(CHIAVE, d, n)
print (hex(result))

