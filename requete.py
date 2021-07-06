import pymysql
from app import app
from db_config import mysql


class Requete:
    def __init__(self):
        self.conn = mysql.connect()
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        

    def getNature(self):
        req = '''
                SELECT * FROM nature
                '''
        self.cursor.execute(req)
        return self.cursor.fetchall()

    # def getNaturePiece(self, natureID):
    #     req = '''
    #             SELECT 
    #             '''
    def _close(self):
        self.conn.close()