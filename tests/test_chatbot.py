# tests/test_chatbot.py

import unittest
from src.chatbot import CryptoBuddy

class TestCryptoBuddy(unittest.TestCase):
    def setUp(self):
        self.bot = CryptoBuddy()

    def test_greeting(self):
        response = self.bot.respond("hi")
        self.assertIn("How can I help you today?", response)

    def test_trending(self):
        response = self.bot.respond("Which crypto is trending?")
        self.assertTrue("trending" in response or "Currently no" in response)

    def test_sustainability(self):
        response = self.bot.respond("eco-friendly")
        self.assertIn("sustainability score", response)

    def test_unknown(self):
        response = self.bot.respond("flibble flabble")
        self.assertIn("I'm not sure I understand", response)

if __name__ == '__main__':
    unittest.main()
