from flask import Flask
# , render_template
import logging
# from flask import Flask, abort, jsonify
import fonctions
app = Flask(__name__)

# @app.route('/')
# def entry_point():
#     return render_template('./app.html')

@app.route('/hello_world')
def hello_world():
    return 'Hello World'

@app.route('/city/stations/')
def station():
    return (city_station())

if __name__ == '__main__':
    app.run(debug=True)
