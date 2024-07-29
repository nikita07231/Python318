import sqlite3
import time
import math


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_posts_annonce(self):
        try:
            self.__cur.execute("SELECT id, title, price, text FROM curs")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статей из БД " + str(e))
        return []

    def add_curs(self, title, price, text):
        try:
            self.__cur.execute("INSERT INTO curs VALUES(NULL, ?, ?, ?)", (title, price, text))
            self.__db.commit()
            return True
        except sqlite3.Error as e:
            print("Ошибка добавления статьи в БД " + str(e))
            return False
