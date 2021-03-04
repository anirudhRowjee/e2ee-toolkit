from main import Session
import unittest


class TestSession(unittest.TestCase):
    """
    base test class for session initialization
    """

    def test_session_initialization(self):
        Session()


if __name__ == "__main__":
    unittest.main()
