import unittest
from src.chatbot import CryptoBuddy

class TestCryptoBuddy(unittest.TestCase):
    def setUp(self):
        self.bot = CryptoBuddy()

    def test_greeting(self):
        response = self.bot.respond("Hello")
        self.assertIn("How can I help you today?", response)

    def test_trending(self):
        response = self.bot.respond("Which crypto is trending?")
        self.assertIn("These cryptos are trending up", response)

    def test_sustainability(self):
        response = self.bot.respond("Which coin is sustainable?")
        self.assertIn("Sustainability score", response)

    def test_default(self):
        response = self.bot.respond("Blah blah")
        self.assertIn("I'm not sure I understand", response)

if __name__ == '__main__':
    unittest.main()
