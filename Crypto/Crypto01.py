from Crypto.Util.number import long_to_bytes

a = '666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d'
a = int(a, 16)

a = long_to_bytes(a)

print(a.decode())

