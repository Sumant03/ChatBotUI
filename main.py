from flask import Flask, escape, request ,render_template

app = Flask(__name__)

@app.route('/')
def hello():

    return render_template('index.html')

@app.route('/consult')
def consult():

    return render_template('consultation.html')

app.run(debug=True,)
