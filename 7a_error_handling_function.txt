import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, headers=HEADERS, json=input_json)
    if response.status_code == 400:
        return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
                }
    response_json = json.loads(response.text)
    emotions = response_json["emotionPredictions"][0]["emotion"]
    dominant_emotion = ""
    dominant_score = -1
    for emotion, score in emotions.items():
        if score > dominant_score:
            dominant_score = score
            dominant_emotion = emotion
    emotions["dominant_emotion"] = dominant_emotion
    return emotions