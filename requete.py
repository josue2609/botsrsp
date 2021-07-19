import pymysql
from app import app
from db_config import mysql


class Requete:
    def __init__(self):
        self.conn = mysql.connect()
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        

    def getMenu(self):
        req = '''
                SELECT MENU, COUNT(MENU) as nombre FROM menu
                '''
        self.cursor.execute(req)
        return self.cursor.fetchall()

    def getMenubyID(self, IDMenu):
        req = '''
                SELECT MENU FROM menu WHERE ID_MENU= %s
                '''
        self.cursor.execute(req, (IDMenu))
        return self.cursor.fetchall()

    def getNatureMenu(self, IDMenu):
        req = '''
                   SELECT n.TYPE_NATURE
                   FROM appartenir a, nature n, menu m
                        WHERE a.ID_NATURE = n.ID_NATURE
                            AND a.ID_MENU = %s 
	                        AND m.ID_MENU = %s
                 '''
        self.cursor.execute(req, (IDMenu,IDMenu))
        return self.cursor.fetchall()
    
    def getNatureMenubyID(self, IDMenu):
        req = '''
                   SELECT n.TYPE_NATURE, COUNT(n.TYPE_NATURE) as nb
                   FROM appartenir a, nature n, menu m
                        WHERE a.ID_NATURE = n.ID_NATURE
                            AND a.ID_MENU = %s 
	                        AND m.ID_MENU = %s
                 '''
        self.cursor.execute(req, (IDMenu,IDMenu))
        return self.cursor.fetchall()

    def getNatureID(self, Typenature):
        req = '''
                SELECT n.ID_NATURE FROM nature n WHERE TYPE_NATURE = %s
                '''
        self.cursor.execute(req, (Typenature))
        return self.cursor.fetchone()

    def getNaturePiece(self, IDNature):
        req = '''
                SELECT DISTINCT p.PIECE, p.NOMBRE_PIECE 
                FROM contenir c, piece p, nature n, menu m, appartenir a
                    WHERE c.ID_NATUREC = %s
                        AND n.ID_NATURE = %s
                        AND c.ID_PIECEC = p.ID_PIECE
                '''
        self.cursor.execute(req, (IDNature,IDNature))
        return self.cursor.fetchall( )
    
    def getNatureCondition(self, IDNature):
        req = '''
                SELECT DISTINCT c.CONDITIONS
                FROM posseder p, nature n, conditions c, appartenir a
                    WHERE p.ID_NATURE = %s
                        AND n.ID_NATURE = %s
                        AND p.ID_CONDITIONS = c.ID_CONDITIONS
                '''
        self.cursor.execute(req, (IDNature,IDNature))
        return self.cursor.fetchall( )
    
    def getNatureDescripition(self, IDNature):
        req = '''
                SELECT n.DESCRIPTION 
                FROM nature n 
                    WHERE ID_NATURE = %s
                '''
        self.cursor.execute(req, (IDNature))
        return self.cursor.fetchall( )

    def getNatureDurée(self, IDNature):
        req = '''
                SELECT n.DUREE_TRAITEMENT
                FROM nature n
                    WHERE ID_NATURE = %s
                '''
        self.cursor.execute(req, (IDNature))
        return self.cursor.fetchall()

    def getNatureBeneficiaire(self, IDNature):
        req = '''
                SELECT DISTINCT c.BENEFICIAIRE
                FROM beneficier b, nature n, beneficiaire c
                    WHERE b.ID_NATURE = %s
                        AND n.ID_NATURE = %s
                        AND b.ID_BENEFICIAIRE = c.ID_BENEFICIAIRE
                '''
        self.cursor.execute(req, (IDNature, IDNature))
        return self.cursor.fetchall()
    
    def getNatureContact(self, IDNature, IDLIAISON):
        req = '''
                SELECT DISTINCT c.CONTACT, c.MAIL
                FROM liaison b, nature n, contact c, joindre j
                    WHERE n.ID_NATURE = %s
                        AND j.ID_NATURE = %s
                        AND j.ID_LIAISON = %s
                        AND c.ID_LIAISON = %s
                '''
        self.cursor.execute(req, (IDNature, IDNature, IDLIAISON, IDLIAISON))
        return self.cursor.fetchall()

    def getNatureContactID(self, LIEU):
        req = '''
                SELECT c.ID_LIAISON FROM liaison c WHERE LIEU=%s
                '''
        self.cursor.execute(req, (LIEU))
        return self.cursor.fetchone()

    def _close(self):
        self.conn.close()