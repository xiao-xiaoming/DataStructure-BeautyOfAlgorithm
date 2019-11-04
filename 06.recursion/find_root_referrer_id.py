# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

import pymysql

db = pymysql.connect("localhost", "root", "root", "test_db")
cursor = db.cursor()


def find_root_referrer_id(actorId: int, relation=None):
    if relation is None:
        relation = set()
    relation.add(actorId)
    referrerId = cursor.execute(r"select referrer_id from user_info where actor_id = %s", actorId)
    if referrerId in relation or referrerId == None:
        return actorId
    return find_root_referrer_id(referrerId)

find_root_referrer_id(1)

cursor.close()
db.close()
