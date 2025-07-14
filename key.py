import re
from collections import defaultdict, Counter
import random


def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text.split()


def build_ngrams(tokens, n=3):
    ngrams = defaultdict(Counter)
    for i in range(len(tokens) - n + 1):
        context = tuple(tokens[i:i+n-1])
        next_word = tokens[i+n-1]
        ngrams[context][next_word] += 1
    return ngrams


def predict_next(ngrams, context):
    context = tuple(context[-(len(list(ngrams.keys())[0])):])
    if context in ngrams:
        return ngrams[context].most_common(1)[0][0]
    return ""


text = "hello there how are you doing today how are you feeling"
tokens = preprocess(text)
ngrams = build_ngrams(tokens, n=3)
print(predict_next(ngrams, ['how', 'are']))