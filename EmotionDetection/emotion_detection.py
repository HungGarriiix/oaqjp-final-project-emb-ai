import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers=header, json=input)
    result = json.loads(response.text)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        emotions = []
        for emotion in result['emotionPredictions']:
            emotions.append(analyse_emotion(emotion['emotion']))
        return emotions

def analyse_emotion(emotion):
    emotion['dominant_emotion'] = max(emotion, key= lambda x: emotion[x])
    return emotion