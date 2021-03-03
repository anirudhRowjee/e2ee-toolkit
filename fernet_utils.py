import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def get_key(string):
    # function to get a fernet key from a given string

    # usually we would use an OS-generated salt for this, to keep it
    # cryptographically secure, but since we want the key generated to be the
    # same across multiple function calls in different object instances, I've
    # just generated a salt with os.urandom(16) (what would usually be called)
    salt = b"\xfcN\x85`\xf9p{V*\xce\xa7U\xbeY\xc8\xa8"

    key_derivation_function = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=salt, iterations=10000
    )

    # convert string to bytes
    # print(string)
    bytes_string = bytes(string, encoding="utf-8")
    # print(bytes_string)
    my_key = base64.urlsafe_b64encode(key_derivation_function.derive(bytes_string))
    # print(f"Key Generated => {my_key}")
    return my_key
