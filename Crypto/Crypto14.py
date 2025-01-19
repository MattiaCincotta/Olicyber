import hashlib
from sympy import nextprime, randprime
from Crypto.Util.number import getPrime, isPrime

import hmac
import hashlib

from Crypto.Util import number

# Messaggio da hashare
msg = "hash_me_pls".encode("utf-8")  # Converte il messaggio in byte

# Calcolo dell'hash utilizzando SHA3-384
hash_object = hashlib.sha3_384(msg)
hash_hex = hash_object.hexdigest()  # Ottieni il risultato in esadecimale

print("SHA3-384(msg) =", hash_hex)

print('-------------------------------------------------------------------------------')

# Chiave in esadecimale
key_hex = '2fdaff26902918f531ade039e5b489e867e318af12151ef326d2ceb310d2d94c'
key = bytes.fromhex(key_hex)  # Converte la chiave in formato byte

# Messaggio da autenticare
msg = "La mia integrità è importante!".encode("utf-8")  # Converte il messaggio in byte

# Calcolo dell'HMAC utilizzando SHA-224
hmac_object = hmac.new(key, msg, hashlib.sha224)
hmac_hex = hmac_object.hexdigest()  # Ottieni il risultato in esadecimale

print("HMAC(msg) =", hmac_hex)


from Crypto.PublicKey import DSA
from binascii import unhexlify

# Chiave DSA in formato esadecimale
key_hex = "3082025c0201003082023506072a8648ce380401308202280282010100de9265fb6ca2c4f43f4c185db6a8a0a38a68f4a121c3794d9fa6736422fd37eceef5150b2042f03c1cdcce0a4b65cf82ecb1af71c452b4052b478a06964660afed5e13e1e9c93cfe2eccddc4e8173043c4829ee00fc8ae2567269ff8c61c0de2ea893f9b29786b7b31fb70d4733694300a3b4f22f50ef0f51d10424df1172c2f4d54a6e3b0d831b8bf4b612b5995030abe438441bfe1a4204571b30cc1f6e90b6d14ce6d11b38ea59de23f857216c27734f9f718dc81909dc10a5f9e8ca483ff98630baef7bb2728239ec929a38ee37dfb216b9efd7153396eba109696961728b9cc0a22922fc378e89d8b0f267dcfd572eb0b20875ff41d5204bf3f35cfc1b5021d00f3265437decfeb37c8d04dd3c48af08cec53e5a2d1475d058a958eaf028201007db8fb561302db67ff5d57fba2eb65fbe6b3d63f3855c1edc1043bf2ab58465f23e6b190a40ec006425d64aff7035a4ffa23c13ed2260b869c7edc2f08056ab6e55f8cd0072c3fd4b6d93a09718dff6c6640c5becc4ae66dd4fe54c2bc1a0f8e48131a3c9cec5e7759d41488300c58772e90e5523f591bd75d2a2fec5e5e8a0d6fd6d7e755752b2faa96965efcd81efd3ed99972b08d6849157d6337748cc685cbec6e6c13910e10be039c78b8f5bcb077a5b019bd9bc36eb1f4fa674c3cb84a81761df74c21f4234e468deb6562e72f43b98af7652cce789f455c31844b0f7e665e12f122893a08a522bea75f919b4d5f1c9ac9bcfeb9147f24914e26e3df76041e021c3136596e4a5d3e5c70dcc4a042c9714d06dce9dc23f6e85f2b9f8f92"

# Decodifica la chiave in formato binario
key_bytes = unhexlify(key_hex)

# Importa la chiave DSA
key = DSA.import_key(key_bytes)

# Estrai il valore della chiave pubblica (y)
y = key.y
print(f"Chiave pubblica (y): {y}")

print('-------------------------------------------------------------------------------')

p = key.p
print("p =", p)

print('-------------------------------------------------------------------------------')

q = key.q
print("q=", q)

print('-------------------------------------------------------------------------------')

g = key.g
print("g=", g)

# Genera un numero casuale con esattamente 1802 bit

lower_bound = 2**1801

upper_bound = 2**1802 - 1



# Trova un numero primo nell'intervallo

print('-------------------------------------------------------------------------------')
n = 1788
print(f'prime_n_bits: {getPrime(n)}')

print('-------------------------------------------------------------------------------')

p = 125882200822156039390180815670799922162623159537975750154820584214667631275877710698990173279826946135300905273435655178651185940652112743560010427509275176632622868629292916905189388956687518032203196972772084614576496500384276463501749703731801945379880584988818103052417574936073789115723428702855702975198

print(f'is Prime: {number.isPrime(p)}')
