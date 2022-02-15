import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()
s = 'I am happy sheep!'

print(sid.polarity_scores(s))