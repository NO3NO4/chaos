# -*- coding:utf-8 -*-

from datetime import datetime
from sqlstore import store

class Subject:

    def __init__(self, id, title, intro="", create_time=datetime.now()):
        self.id = id
        self.title = title
        self.intro = intro
        self.create_time = create_time

    def get(self, id):
        cursor = store.cursor()
        cursor.execute("select id, title, intro, create_time from subject "
        "where id=%s", id)
        id, title, intro, create_time = cursor.fetchone()
        return Subject(id, title, intro, create_time)

    def add(self, id, title, intro=''):
        cursor = store.cursor()
        cursor.execute('insert into subject (id, title, intro) "
        "values (%s, %s, %s)', (id, title, intro))
