# user class

import random
import uuid
import math
import hashlib
import base64
from cryptography.fernet import Fernet
from fernet_utils import get_key

class User:
    """
    Represents a user taking part in the chat
    """

    def __init__(self, name, pre_shared_secret_base, pre_shared_secret_modulus):
        """
        @param name => name of the user
        @param pre_shared_secret_base must be a large number
        @param pre_shared_secret_modulus must be a large prime number
        """
        self.name = name
        self.psk_base = pre_shared_secret_base
        self.psk_mod = pre_shared_secret_modulus

        self.PRIVATE_KEY_BIT_LIMIT = 2000
        # cryptographically secure random number
        self.private_key = random.getrandbits(self.PRIVATE_KEY_BIT_LIMIT)
        self.public_key = None

        # set the shared encryption key to avoid redoing expensive computation
        # TODO this is not good practice. In multi-user situations, this might
        # not be feasible, but since we are considering a 2-user situation,
        # this works well.
        self.shared_secret = None
        # set the encryption object (Frenet instance)
        self.encryptor = None

    def get_fernet_key(self, shared_key):
        # returns the fernet key we can use to encode and decode with fernet
        # TODO this is breaking, fix it with one of the answers mentioned here
        # https://stackoverflow.com/questions/44432945/generating-own-key-with-python-fernet
        return base64.urlsafe_b64encode(bytes(str(shared_key), encoding="utf-8"))

    def get_public(self):
        # return the key that will be transported
        if not self.public_key:
            # self.public_key = (self.psk_base) ** self.private_key % self.psk_mod
            self.public_key = pow(self.psk_base, self.private_key, self.psk_mod)
        return self.public_key

    def get_private(self):
        return self.private_key

    def get_shared_secret(self, other_public_key):
        # take the other person's shared secret and generate the shared secret
        # not stored as an attribute of self, as we use this to encrypt and
        # decrypt messages
        # return (other_public_key) ** self.private_key % self.psk_mod
        if not self.shared_secret:
            self.shared_secret = pow(other_public_key, self.private_key, self.psk_mod)
        if not self.encryptor:
            self.encryptor = Fernet(get_key(str(self.shared_secret)))
        return self.shared_secret

    def encrypt(self, message):
        # return an encrypted version of a message
        if not self.encryptor:
            raise AttributeError(
                "Encrtyptor is not Defined  - has the shared key been generated?"
            )
        else:
            return self.encryptor.encrypt(message)

    def decrypt(self, ciphertext):
        # return an encrypted version of a message
        if not self.encryptor:
            raise AttributeError(
                "Encrtyptor is not Defined  - has the shared key been generated?"
            )
        else:
            return self.encryptor.decrypt(ciphertext)

    def send_message(self, message):
        # functon to return a message object which is to be appended to the
        # message array, with encryption
        return {
            "sender": self.name,
            "message": self.encrypt(bytes(message, encoding="utf-8")),
        }

    def send_public_key_as_message(self):
        return {"sender": self.name, "message": self.get_public()}

    def decrypt_message_object(self, message_object):
        # decrypt a message dict and replace self name with "me"

        new_mo = {}

        if message_object["sender"] == self.name:
            new_mo["sender"] = "me"
        else:
            new_mo["sender"] = message_object["sender"]

        new_mo["message"] = self.decrypt(message_object["message"])
        return new_mo

    def decrypt_array(self, message_array):
        # Decrypt an array of messages with the private key
        decrypted_messages = list(map(self.decrypt_message_object, message_array[2:]))
        return decrypted_messages

