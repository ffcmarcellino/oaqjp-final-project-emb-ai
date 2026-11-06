from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detection():
    statement = request.args.get("textToAnalyze")
    emotions = emotion_detector(statement)
    return f"For the given statement, the system response is 'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. The dominant emotion is {emotions['dominant_emotion']}."

if __name__ == "__main__":
    app.run()
