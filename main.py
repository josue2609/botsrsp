from app import app
from flask import jsonify
from flask import flash, request
from requete import Requete


req = Requete()

@app.route('/')
def botsrsp():
    rows = req.getNatureDescripition(1)
    resp = jsonify(rows)

    return resp


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

if __name__ == "__main__":
    app.run(debug=True)