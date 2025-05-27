import random, string, hashlib, hmac
from datetime import datetime, timedelta

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def sign(text, key):
    return hmac.new(key.encode(), text.encode(), hashlib.sha256).hexdigest()

# Cookie reale
cookie_value = "not_admin"
server_signature = "18b06c1dfa10650941f4674fd7ba11dbfdf039ebc1169811229764013ff486b6"
uptime_sec = 711492

# Ora attuale in UTC
now = datetime.utcnow()
start_time = now - timedelta(seconds=uptime_sec)

# Brute-force ±2 minuti
for delta in range(-120, 120):
    guess_time = start_time + timedelta(seconds=delta)
    seed_str = guess_time.strftime('%Y-%m-%d %H:%M:%S')

    random.seed(seed_str)
    key = get_random_string(32)

    test_signature = sign(cookie_value, key)

    if test_signature == server_signature:
        print(f"[+] Chiave trovata: {key}")
        print(f"[+] Seed: {seed_str}")
        print(f"[+] Firma per 'admin': {sign('admin', key)}")
        break
else:
  print("[-] Chiave non trovata")