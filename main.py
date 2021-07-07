from flask.wrappers import Response
from app import app
from flask import jsonify
from flask import flash, request
from requete import Requete
from Keys import facebook_bot_page_access_token
from pymessenger.bot import Bot

#Token pour valider la liasion Facebook
PAGE_ACCESS_TOKEN = facebook_bot_page_access_token
VERIFY_TOKEN = 'botsrsp'

#Initiailisation du module pymessenger pour la réception et envoie de messsage
bot = Bot(PAGE_ACCESS_TOKEN)

# Initialisation de la requete
req = Requete()

#Traitement pour l'orchestration des services 
def process_message(text):
    formatted_message = text.lower()
    if formatted_message == "test":
        response = "Test Successful"
    elif formatted_message == "What are you doing":
        response = "Changing my life for better"
    else:
        response = "Make your life easier"
    return response

@app.route('/', methods = ["GET","POST"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return "Problème liaison avec Facebook!"
    elif request.method == "POST":
        payload = request.json
        event = payload['entry'][0]['messaging']
        for msg in event:
            text = msg['message']['text']
            sender_id = msg['sender']['id']
            response = process_message(text)
            bot.send_text_message(sender_id, response)
        return "Message received"
    else:
        return "200"

# def botsrsp():
#     rows = req.getNatureDescripition(1)
#     resp = jsonify(rows)

#     return resp


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