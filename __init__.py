import sys
from flask import Flask, request
from nudenet import NudeClassifierLite

app = Flask(__name__)

classifier_lite = NudeClassifierLite()

@app.route("/isPorn", methods=['GET'])
def isPorn():
    input = request.args['input']

    result = classifier_lite.classify(input)
    if result[input]['unsafe'] > result[input]['safe']:
        return "1"
    else:
        return "0"


if __name__ == '__main__':
    app.run()
