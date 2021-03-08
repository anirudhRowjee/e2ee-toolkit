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

        # Message Array - save for the first 2 messages where they key exchange
        # happens, the rest are encrypted
        self.messages = []

        ## Initialize our users
        self.add_users()

        ## set the shared secrets
        self.perform_key_exchange()

        print(self.messages)

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

    # flask-facing methods
    def add_users(self):
        # TODO see if we can ask the users for the names of the people they
        # want in the char
        self.user_1 = User("Alice", self.pss_base, self.pss_modulus)
        self.user_2 = User("Bob", self.pss_base, self.pss_modulus)

    def perform_key_exchange(self):
        # exchange the public keys first
        self.messages.append(self.user_1.send_public_key_as_message())
        self.messages.append(self.user_2.send_public_key_as_message())
        # set the shared secrets
        self.user_1.get_shared_secret(self.get_pkey_user_2())
        self.user_2.get_shared_secret(self.get_pkey_user_1())

    def send_message_for_user(self, username, message):
        # send messages as a specific user
        users = {user.name: user for user in {self.user_1, self.user_2}}
        try:
            current_user = users[username]
        except KeyError:
            raise AttributeError(f"No User with that username. ({username})")

        self.messages.append(current_user.send_message(message))

    def get_decrypted_messages_for_user(self, username):
        users = {user.name: user for user in {self.user_1, self.user_2}}
        try:
            current_user = users[username]
        except KeyError:
            raise AttributeError(f"No User with that username. ({username})")
        return current_user.decrypt_array(self.messages)

    def get_server_messages(self):
        # return the messages that the server sees
        return self.messages
