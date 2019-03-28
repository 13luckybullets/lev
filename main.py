import requests

from flask import Flask, request, json

app = Flask(__name__)
app.secret_key = "super secret key"


def get_recognition(file):

    url = 'https://api-2445582032290.production.gw.apicast.io/v1/foodrecognition'

    payload = {'user_key': '38878f9ac39fcc93a420fdc33c1eccc9'}
    headers = {'Content-Type': 'image/jpeg'}

    result = requests.post(url, params=payload, headers=headers, data=file).json()

    return result


@app.route("/",  methods=['POST', 'GET'])
def recognition():
    res = {'err': "nothing to show"}
    if request.method == 'POST':
        f = request.files['file']
        res = {'is_food': get_recognition(f).get('is_food', 'something_go_wrong')}

    response = app.response_class(
        response=json.dumps(res),
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
