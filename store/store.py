from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def home():
    return render_template('home.html')

@app.get('/clothes/')
def clothes():
    return render_template('clothes.html')

@app.get('/footwear/')
def footwear():
    return render_template('footwear.html')

@app.get('/jackets/')
def jackets():
    return render_template('jackets.html')

if __name__ == '__main__':
    app.run(debug=True)