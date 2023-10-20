# import nltk

# from flask import Flask, render_template, request
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')
# app = Flask(__name__)

# # Initialize the sentiment analyzer
# sia = SentimentIntensityAnalyzer()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/analyze', methods=['POST'])
# def analyze():
#     text = request.form['text']
#     sentiment = get_sentiment(text)
#     return render_template('index.html', text=text, sentiment=sentiment)

# def get_sentiment(text):
#     sentiment_score = sia.polarity_scores(text)
#     if sentiment_score['compound'] >= 0.05:
#         return 'Positive'
#     elif sentiment_score['compound'] <= -0.05:
#         return 'Negative'
#     else:
#         return 'Neutral'

# if __name__ == '__main__':
#     app.run(debug=True)

import nltk

from flask import Flask, render_template, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
app = Flask(__name__)

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    sentiment, score = get_sentiment(text)
    return render_template('index.html', text=text, sentiment=sentiment, score=score)

def get_sentiment(text):
    sentiment_score = sia.polarity_scores(text)
    if sentiment_score['compound'] >= 0.05:
        return 'Positive', sentiment_score['compound']
    elif sentiment_score['compound'] <= -0.05:
        return 'Negative', sentiment_score['compound']
    else:
        return 'Neutral', sentiment_score['compound']

if __name__ == '__main__':
    app.run(debug=True)
