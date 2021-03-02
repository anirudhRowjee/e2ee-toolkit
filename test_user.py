from main import User
import unittest


class TestUser(unittest.TestCase):
    def test_initialization(self):
        # test the creation of a user
        psk_base = 100
        psk_modulus = 97
        u1 = User("", psk_base, psk_modulus)

    def test_encryption(self):
        # test to make sure both the shared secrets match
        psk_base = 100
        psk_modulus = 2 ** 31 - 1
        user_1 = User("1", psk_base, psk_modulus)
        user_2 = User("2", psk_base, psk_modulus)

        public_user1 = user_1.get_public()
        public_user2 = user_2.get_public()

        private_from_user_1 = user_1.get_shared_secret(public_user2)
        private_from_user_2 = user_2.get_shared_secret(public_user1)
        # print(private_from_user_2, private_from_user_1)
        self.assertEqual(private_from_user_1, private_from_user_2)

        # now check if the messaging works
        m1 = user_1.send_message("hello")
        m2 = user_2.send_message("hello")
        print(m1, m2)
        self.assertEqual(m1["message"], m2["message"])


if __name__ == "__main__":
    unittest.main()
