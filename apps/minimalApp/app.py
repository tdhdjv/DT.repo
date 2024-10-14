from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        search = request.form.get('search')
        return redirect(url_for('search',name=search))
    return render_template('home.html')

@app.route('/search/<name>', methods = ['POST', 'GET'])
def search(name):
    print(name)
    return render_template('result.html')


@app.route('/camera', methods = ['POST', 'GET'])
def camera():
    return render_template('camera.html')

if __name__ == '__main__':
    app.run(debug=True)
    