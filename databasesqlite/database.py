from importi.importslist import *
import sqlite3
base = sqlite3.connect("database.db")
cur = base.cursor()

# base.execute("CREATE TABLE IF NOT EXISTS users(username VARCHAR(256),userid VARCHAR(300),phonenumber VARCHAR(30), userbio VARCHAR(150))")
# base.execute("CREATE TABLE IF NOT EXISTS reputation(username VARCHAR(256),userid VARCHAR(300),reputation VARCHAR(10000)")
# base.commit()