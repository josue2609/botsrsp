from flask.wrappers import Response
from threading import Thread
from app import app
from flask import jsonify, request
from requete import Requete
from Keys import facebook_bot_page_access_token
from pymessenger.bot import Bot, NotificationType

#Token pour valider la liasion Facebook
PAGE_ACCESS_TOKEN = facebook_bot_page_access_token
VERIFY_TOKEN = 'botsrsp'

#Initiailisation du module pymessenger pour la réception et envoie de messsage
bot = Bot(PAGE_ACCESS_TOKEN)

# Initialisation de la requete
req = Requete()

#Traitement pour l'orchestration des services 
def solde_liste(sender_id):
    data_reply = []
    rows1 = req.getNatureMenu('1')
    for row1 in rows1:
        response = row1.get('TYPE_NATURE')
        #bot.send_text_message(sender_id, response)
        #bot.send_quick_reply(sender_id, CONDITIONS = True)
        data_reply.append(
            {
                "content_type": "text",
                "title": response,
                "payload": response.upper()
            }
        )
        print(response)
    bot.send_quick_reply(
        sender_id,
        'Choisissez la nature: ',
        data_reply
    )
    return

def active_liste(sender_id):
    data_reply = []
    rows1 = req.getNatureMenu('2')
    for row1 in rows1:
        response = row1.get('TYPE_NATURE')
        data_reply.append(
            {
                "content_type": "text",
                "title": response,
                "payload": response.upper()
            }
        )
        print(response)
    bot.send_quick_reply(
        sender_id,
        'Choisissez la nature: ',
        data_reply
    )
    return

def retraite_liste(sender_id):
    data_reply = []
    rows1 = req.getNatureMenu('3')
    for row1 in rows1:
        response = row1.get('TYPE_NATURE')
        data_reply.append(
            {
                "content_type": "text",
                "title": response,
                "payload": response.upper()
            }
        )
        print(response)
    bot.send_quick_reply(
        sender_id,
        'Choisissez la nature: ',
        data_reply
    )
    return

def liste_solde(sender_id):
    liste = []
    rows1 = req.getNatureMenu('1')
    for row1 in rows1:
        response = row1.get('TYPE_NATURE')
        liste.append(response)
    return liste 

def liste_active(sender_id):
    liste = []
    rows1 = req.getNatureMenu('2')
    for row1 in rows1:
        response = row1.get('TYPE_NATURE')
        liste.append(response)
    return liste 

def liste_retraite(sender_id):
    liste = []
    rows1 = req.getNatureMenu('3')
    for row1 in rows1:
        response = row1.get('TYPE_NATURE')
        liste.append(response)
    return liste 

def nature_solde(sender_id, message):
    rowsm = req.getNatureID(message)
    for rowsi in rowsm:
        idm = rowsm.get('ID_NATURE')
        resp = req.getNatureDescripition(idm)
        for re in resp:
            response = re.get('DESCRIPTION')
            bot.send_text_message(sender_id,response)
    return

def nature_active(sender_id, message):
    rowsm = req.getNatureID(message)
    for rowsi in rowsm:
        idm = rowsm.get('ID_NATURE')
        resp = req.getNatureDescripition(idm)
        for re in resp:
            response = re.get('DESCRIPTION')
            bot.send_text_message(sender_id,response)
    return

def nature_retraite(sender_id, message):
    rowsm = req.getNatureID(message)
    for rowsi in rowsm:
        idm = rowsm.get('ID_NATURE')
        resp = req.getNatureDescripition(idm)
        for re in resp:
            response = re.get('DESCRIPTION')
            bot.send_text_message(sender_id,response)
    return

def details_nature(sender_id,message):
    deta = message.split(":")
    if deta[0] == 'CONDITIONS':
        # alaina aloha ny ID raha deta[2] ny type_nature
        #
        #dia alaina lay ID dia jerena ilay condition
        #
        id_n = deta[1]
        maka_id = req.getNatureID(id_n)
        for makaid in maka_id:
            id_naka = maka_id.get('ID_NATURE')
            maka = req.getNatureCondition(id_naka)
            for valiny in maka:
                response = valiny.get('CONDITIONS')
                bot.send_text_message(sender_id,response)
            bot.send_text_message(sender_id, "Tapez CONDITIONS/BENEFICIAIRE/PIECE/CONTACT:TYPE NATURE Pour voir les détails")
    elif deta[0] == 'PIECE':
        id_n = deta[1]
        maka_id = req.getNatureID(id_n)
        for makaid in maka_id:
            id_naka = maka_id.get('ID_NATURE')
            maka = req.getNaturePiece(id_naka)
            for valiny in maka:
                response = valiny.get('PIECE')
                bot.send_text_message(sender_id,response)
            bot.send_text_message(sender_id, "Tapez CONDITIONS/BENEFICIAIRE/PIECE/CONTACT:TYPE NATURE Pour voir les détails")
    elif deta[0] == 'BENEFICIAIRE':
        id_n = deta[1]
        maka_id = req.getNatureID(id_n)
        for makaid in maka_id:
            id_naka = maka_id.get('ID_NATURE')
            maka = req.getNatureBeneficiaire(id_naka)
            for valiny in maka:
                response = valiny.get('BENEFICIAIRE')
                bot.send_text_message(sender_id,response)
            bot.send_text_message(sender_id, "Tapez CONDITIONS/BENEFICIAIRE/PIECE/CONTACT:TYPE NATURE Pour voir les détails")
    elif deta[0] == 'CONTACT':
        id_n = deta[1]
        maka_id = req.getNatureID(id_n)
        for makaid in maka_id:
            id_naka = maka_id.get('ID_NATURE')
            print(id_naka)
            lieu = deta[2]
            print(lieu)
            makalieu_id= req.getNatureContactID(lieu)
            for makalieuid in makalieu_id:
                lieux = makalieu_id.get('ID_LIAISON')
                maka = req.getNatureContact(id_naka,lieux)
                print(maka)
                for valiny in maka:
                    print(valiny)
                    response = valiny.get('CONTACT')
                    reponse1 = valiny.get('MAIL')
                    print(response)
                    print(reponse1)
                    bot.send_text_message(sender_id,response)
                    bot.send_text_message(sender_id,reponse1)
            bot.send_text_message(sender_id, "Tapez CONDITIONS/BENEFICIAIRE/PIECE/CONTACT:TYPE NATURE Pour voir les détails")
    elif deta[0] == 'DUREE':
            id_n = deta[1]
            maka_id = req.getNatureID(id_n)
            for makaid in maka_id:
                id_naka = maka_id.get('ID_NATURE')
                maka = req.getNatureDurée(id_naka)
                for valiny in maka:
                    response = valiny.get('DUREE_TRAITEMENT')
                    bot.send_text_message(sender_id,response)
                bot.send_text_message(sender_id, "Tapez CONDITIONS/BENEFICIAIRE/PIECE/CONTACT:TYPE NATURE Pour voir les détails")
    return

def process_message(sender_id, message):
    message = message.strip()
    if message == 'MENU':
        rows = req.getMenu()
        for rowd in rows:
            it = rowd.get('nombre')
            it = int(it)
            data_reply = []
            for i in range (it+1):
                re = req.getMenubyID(i)
                for resp in re:
                    response = resp.get('MENU')
                    # bot.send_text_message(sender_id, response)
                    print(response)
                    # pour ne pas faire planter l'API Messenger,
                    # Si la response est vide, on passe au suivant
                    if response.strip() == '': continue
                    data_reply.append(
                        {
                            "content_type": "text",
                            "title": response,
                            "payload": response.upper()
                        }
                    )
            bot.send_quick_reply(
                sender_id,
                'Saisissez votre menu: ',
                data_reply
            )     
        return 

    elif message == 'SOLDE':
        solde_liste(sender_id)    
        return 
    elif message == "AGENTS DE L'ETAT EN ACTIVITÉ":
        active_liste(sender_id)
        return
    elif message == 'AGENTS DE L\'ETAT RETRAITÉS':
        retraite_liste(sender_id)
    else:
        ma_liste = liste_solde(sender_id)
        ma_liste1 = liste_active(sender_id)
        ma_liste2 = liste_retraite(sender_id)
        if message in ma_liste:
            nature_solde(sender_id,message)
            # "Tapez CONDITIONS/BENEFICIAIRE/PIECE/CONTACT:TYPE NATURE Pour voir les détails"
            bot.send_quick_reply(
                sender_id,
                'Voir les details: ',
                [  
                    {
                        "content_type": "text",
                        "title": response,
                        "payload": response.upper() # a completer poru differencer le type.
                    } for response in ('CONDITIONS', 'BENEFICIAIRE', 'PIECE', 'CONTACT')
                ]
            )
        elif message in ma_liste1:
            nature_active(sender_id,message)
            bot.send_quick_reply(
                sender_id,
                'Voir les details: ',
                [  
                    {
                        "content_type": "text",
                        "title": response,
                        "payload": response.upper() # a completer poru differencer le type.
                    } for response in ('CONDITIONS', 'BENEFICIAIRE', 'PIECE', 'CONTACT')
                ]
            )
        elif message in ma_liste2:
            nature_retraite(sender_id,message)
            bot.send_quick_reply(
                sender_id,
                'Voir les details: ',
                [  
                    {
                        "content_type": "text",
                        "title": response,
                        "payload": response.upper() # a completer poru differencer le type.
                    } for response in ('CONDITIONS', 'BENEFICIAIRE', 'PIECE', 'CONTACT')
                ]
            )
        else:
            details_nature(sender_id,message)

            # A mettre sii aucun conditions n est verifié
            # c a d il faut mettre dans le else.
            bot.send_quick_reply(
                sender_id,
                'Afficher...',
                [  
                    {
                        "content_type": "text",
                        "title": 'MENU',
                        "payload": 'MENU' # a completer poru differencer le type.
                    }
                ]
            )
        return
    

@app.route('/', methods = ["GET","POST"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return "Problème liaison avec Facebook!"

    elif request.method == "POST":
        # recuperena le json nalefany facebook
        body = request.get_json()
        # alefa any amn processus afa manao azy
        run = Thread(target=analyse, args=[body])
        run.start()
    return 'OK'

def analyse(body):
    for event in body['entry']:
        messaging = event['messaging']
        for message in messaging:
            if message.get('message'):
                print(message)
                sender_id = message['sender']['id']
                if message['message'].get('quick_reply'):
                    process_message(
                        sender_id,
                        message['message'].get('quick_reply').get('payload')
                    )
                elif message['message'].get('text'):
                    process_message(sender_id, message['message'].get('text'))


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