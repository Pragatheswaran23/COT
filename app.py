from flask import Flask, render_template, request
from summarizer import extractive_summary
from sentiments import analyze_sentiment
from keyword_extraction import get_keywords
from paraphrasing import paraphrase_text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['GET', 'POST'])
def summarize():
    summary = ""
    text = ""
    if request.method == 'POST':
        text = request.form['text']
        num_sentences = int(request.form['num_sentences'])
        summary = extractive_summary(text, num_sentences)

    return render_template('summarize.html', summary=summary, text=text)

@app.route('/sentiment', methods=['GET', 'POST'])
def sentiment():
    sentiments = ""
    text = ""
    if request.method == 'POST':
        text = request.form['text']
        sentiments = analyze_sentiment(text)

    return render_template('sentiment.html', sentiments=sentiments, text=text )

@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    keywords = ""
    text = ""
    if request.method == 'POST':
        text = request.form['text']
        num_sentences = int(request.form['num_sentences'])
        keywords = get_keywords(text, num_sentences)

    return render_template('keyword.html', keywords=keywords, text=text)

@app.route('/paraphrase', methods=['GET', 'POST'])
def paraphrase():
    paraphrased = ""
    text = ""
    if request.method == 'POST':
        text = request.form['text']
        paraphrased = paraphrase_text(text)

    return render_template('paraphraser.html', paraphrased=paraphrased, text=text)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
