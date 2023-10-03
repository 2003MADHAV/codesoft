import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy_emotion(self):
        result = emotion_detector("I am so happy!")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_sadness_emotion(self):
        result = emotion_detector("I am feeling really sad.")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_emotion(self):
        result = emotion_detector("I am afraid of the dark.")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_anger_emotion(self):
        result = emotion_detector("I am angry about this situation!")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_emotion(self):
        result = emotion_detector("This food is disgusting.")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_empty_text(self):
        result = emotion_detector("")
        self.assertIsNone(result, "Emotion detection for empty text should return None")

if __name__ == '__main__':
    unittest.main()
