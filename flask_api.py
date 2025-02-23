from flask import Flask, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    sentiment_score = analyzer.polarity_scores(text)['compound']
    sentiment = "positive" if sentiment_score > 0.05 else "negative" if sentiment_score < -0.05 else "neutral"
    return jsonify({"sentiment": sentiment})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
