import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotion(unittest.TestCase):
    def test_emotion_detection(self):
        statement_1 = 'I am glad this happened'
        self.assertEqual(emotion_detector(statement_1)[0]['dominant_emotion'], 'joy')
        
        statement_2 = 'I am really mad about this'
        self.assertEqual(emotion_detector(statement_2)[0]['dominant_emotion'], 'anger')
        
        statement_3 = 'I feel disgusted just hearing about this'
        self.assertEqual(emotion_detector(statement_1)[0]['dominant_emotion'], 'disgust')
        
        statement_4 = 'I am so sad about this'
        self.assertEqual(emotion_detector(statement_1)[0]['dominant_emotion'], 'sadness')
        
        statement_5 = 'I am really afraid that this will happen	'
        self.assertEqual(emotion_detector(statement_1)[0]['dominant_emotion'], 'fear')
    
    if __name__ == '__main__':
        unittest.main()