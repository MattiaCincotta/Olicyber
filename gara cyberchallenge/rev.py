import requests

BASE_URL = "http://10.42.0.2:38061"  # Cambia con il tuo URL

def get_seed():
    url = f"{BASE_URL}/api/seed"
    resp = requests.get(url)
    if resp.status_code != 200:
        print(f"Errore GET /api/seed: {resp.status_code}")
        return None
    # Il contenuto è application/x-www-form-urlencoded, es: seed=1234
    data = resp.text.strip()
    if not data.startswith("seed="):
        print("Formato seed inatteso:", data)
        return None
    seed = data.split("=", 1)[1]
    print(f"Seed ottenuto: {seed}")
    return seed

def post_response_json(seed):
    url = f"{BASE_URL}/api/response"
    headers = {
        "Content-Type": "application/json"
    }
    data = {"seed": int(seed)}
    resp = requests.post(url, json=data, headers=headers)
    print(f"POST /api/response status: {resp.status_code}")
    if resp.status_code != 200:
        print("Errore nel POST /api/response:", resp.text)
        return False
    return True


def get_flag():
    url = f"{BASE_URL}/api/flag"
    resp = requests.get(url)
    if resp.status_code != 200:
        print(f"Errore GET /api/flag: {resp.status_code}")
        print("Risposta:", resp.text)
        return None
    print("Flag ottenuta:")
    print(resp.text)
    return resp.text

def main():
    seed = get_seed()
    if not seed:
        return
    if not post_response_json(seed):
        return
    get_flag()

if __name__ == "__main__":
    main()
