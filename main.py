from app import app
from flask import jsonify
from flask import flash, request
from requete import Requete


req = Requete()

@app.route('/')
def botsrsp():
    rows = req.getNature()
    resp = jsonify(rows)

    return resp

# @app.route('/nature')
# def nature():
#     try:
#         conn = mysql.connect()
#         cursor = conn.cursor(pymysql.cursors.DictCursor)
#         cursor.execute("SELECT * FROM nature")
#         rows = cursor.fetchall()
#         resp = jsonify(rows)
#         resp.status_code = 200
#         return resp
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()

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