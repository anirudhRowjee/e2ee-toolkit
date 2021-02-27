class User:
    def __init__(
        self, display_name: str, private_key: str, public_key: str, IP: str
    ) -> None:
        """
        User Class
        holds all the information about a user in the Chat Application.
        """
        self.display_name: str = display_name
        self.private_key: str = private_key
        self.public_key: str = public_key
        self.IP: str = IP

    def generate_shared_key(self, other_user_public_key: str) -> str:
        # function to generate a shared key with someone else's public key
        # we need to perform the Diffie-Hellman key exchange here to generate
        # the shared key.
        pass
