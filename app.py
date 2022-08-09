from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def Welcome():
    return 'Welcome'


@app.route('/Precipitation')
def Precipitation():
    return render_template()


@app.route('/Stations')
def Stations():
    return render_template()


@app.route('/Monthly_Temperature')
def Monthly_Temperature():
    return render_template()


@app.route('/Statistics')
def Statistics():
    return render_template()