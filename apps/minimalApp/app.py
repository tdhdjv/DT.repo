from flask import Flask, render_template, url_for, request, redirect
from fuzzywuzzy import process
import pandas as pd


df = pd.read_csv(r'D:\Python\DT\apps\minimalApp\laboratory_equipment.csv')
history = {}
app = Flask(__name__)


def text_matching(name):
    correct_phrases = df['name'].to_list()
    
    # Use extractBest to find the closest match
    matched_phrase, score = process.extractOne(name, correct_phrases)


    # Set a threshold score to determine if it's a good match
    threshold = 50  # You can adjust this threshold
    if score >= threshold:
        return matched_phrase
    return name 

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        search = request.form.get('search')
        return redirect(url_for('search',name=search))
    return render_template('home.html')

@app.route('/search/<name>', methods = ['POST', 'GET'])
def search(name):
    row = df.loc[df['name'] == name]
    new_name = text_matching(name)
    if new_name != name:
        return redirect(url_for('search',name=new_name))
    history[name] = f'/search/{name}'
    image = ''
    text = ''
    name = ''
    location = ''
    ref_vid = ''
    inventory = 0
    if not row.empty:
        name = row['name'].values[0]
        image = row['img'].values[0]
        text = row['text'].values[0]
        location = row['room'].values[0]
        ref_vid = row['ref_video'].values[0]
        inventory = row['inventory'].values[0]

    return render_template('result.html', 
        image = image,
        name = name,
        text = text,
        location=location,
        ref_vid = ref_vid,
        inventory = inventory
    )

@app.route('/camera', methods = ['POST', 'GET'])
def camera():
    return render_template('camera.html')

@app.route('/list', methods = ['POST', 'GET'])
def list():
    print(history)
    return render_template('list.html', history = history)
if __name__ == '__main__':
    app.run(debug=True)