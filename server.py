"""
Final Project: AI-Based Web Application Development and Deployment
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("AI Watson")

@app.route('/')
def home():
    """
    go to homepage
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def get_emotion():
    """
    get the emotion response through text
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        response = "Invalid text! Please try again!"
    else:
        response = (f"For the given statement, the system response is "
        f"'anger': {result[0]['anger']}, 'disgust': {result[0]['disgust']}, "
        f"'fear': {result[0]['fear']}, 'joy': {result[0]['joy']} and "
        f"'sadness': {result[0]['sadness']}. "
        f"The dominant emotion is {result[0]['dominant_emotion']}.")
    return response

if __name__ == "__main__":
    app.run(debug=True)
