import unittest
from modleepkg.language import sentiment

class TestSentiment(unittest.TestCase):

	def test_sentiment(self):
		self.assertEqual(sentiment("Hello"), [{'label': 'NEGATIVE', 'score': 0.6614580154418945}])

unittest.main()
