# session class
import random
import uuid
import math
import hashlib
import base64
from cryptography.fernet import Fernet
from fernet_utils import get_key

from user import User


class Session:
    """
    Represents a chat session
    """

    def __init__(self):

        # make this a random number that is known to both parties as the common
        # base
        self.pss_base = random.getrandbits(200)
        # a large prime number, hence the 31st Mersenne prime has been chosen
        self.pss_modulus = 2 ** 31 - 1

        ## Initialize our users
        self.user_1 = User("Alice", self.pss_base, self.pss_modulus)
        self.user_2 = User("Bob", self.pss_base, self.pss_modulus)

        # Message Array - save for the first 2 messages where they key exchange
        # happens, the rest are encrypted
        self.messages = []

        # exchange the public keys first
        self.messages.append(self.user_1.send_public_key_as_message())
        self.messages.append(self.user_2.send_public_key_as_message())

        # set the shared secrets
        self.user_1.get_shared_secret(self.get_pkey_user_2())
        self.user_2.get_shared_secret(self.get_pkey_user_1())

        print(self.messages)

        self.messages.append(self.user_1.send_message("hello"))
        self.messages.append(self.user_2.send_message("hi"))
        self.messages.append(self.user_1.send_message("how are you"))
        self.messages.append(self.user_2.send_message("fine, thank you!"))

        print("Server sees => ", self.messages)
        print(f"{self.user_1.name} sees => ", self.user_1.decrypt_array(self.messages))
        print(f"{self.user_2.name} sees => ", self.user_2.decrypt_array(self.messages))

    def get_pkey_user_1(self):
        # function to get the public key of user 1
        if not self.messages:
            raise AttributeError(
                "No Messages to get info from - did you initialize the session?"
            )
        else:
            return self.messages[0]["message"]

    def get_pkey_user_2(self):
        # function to get the public key of user 2
        if not self.messages:
            raise AttributeError(
                "No Messages to get info from - did you initialize the session?"
            )
        else:
            return self.messages[1]["message"]
