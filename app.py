from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sentence = request.form['sentence']
        if sentence:
            sa = pipeline('sentiment-analysis', model='CAMeL-Lab/bert-base-arabic-camelbert-mix-sentiment')
            result = sa(sentence)
            return render_template('index.html', result=result, sentence=sentence)
        else:
            return render_template('index.html', error='Please provide a sentence')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
