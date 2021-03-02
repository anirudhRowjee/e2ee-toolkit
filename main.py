"""
Main file for the E2EE Toolkit. This file consists of
1. UI Code
2. Encryption and Decryption Modules
3. Diffie-Hellman Key Exchange Function
"""
import tkinter
import random
import uuid
import math
import hashlib
import cryptography


class User:
    """
    Represents a user taking part in the chat
    """

    def __init__(self, pre_shared_secret_base, pre_shared_secret_modulus):
        """
        @param pre_shared_secret_base must be a large number
        @param pre_shared_secret_modulus must be a large prime number
        """
        # DO NOT MAKE THIS ABOVE 100
        self.PRIVATE_KEY_BIT_LIMIT = 2000
        # cryptographically secure random number
        self.private_key = random.getrandbits(self.PRIVATE_KEY_BIT_LIMIT)
        self.public_key = None
        self.psk_base = pre_shared_secret_base
        self.psk_mod = pre_shared_secret_modulus

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
        return pow(other_public_key, self.private_key, self.psk_mod)


class Session:
    """
    Represents a chat session
    """

    def __init__(self):
        # generate pre-shared secret modulus - this is a mersenne prime for
        # security, by default will be 2^31 - 1
        self.pss_modulus = 2 ** 31 - 1

    def encrypt(self, message, key):
        pass

    def decrypt(self, message, key):
        pass

    def diffie_hellman(self, alice_priv, alice_pub, bob_priv, bob_pub, psk):
        pass


def run_ui():
    # main function to handle the UI
    pass
