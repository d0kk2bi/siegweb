import sqlite3, hashlib, time

conn = sqlite3.connect("/CTFd/CTFd/ctfd.db")

cur = conn.cursor()

# update all hidden
sql = "update challenges set state='hidden'"
cur.execute(sql)
conn.commit()


# select last id
sql = "select id from challenges order by id desc limit 1"
cur.execute(sql)
try:
    no = (cur.fetchone())[0]
except TypeError:
    no = 0


# insert into challenges visible
teams = ['Team A', 'Team B', 'Team C']

names = [['Tester1', 'Tester2', 'Tester3', 'Tester4'],
         ['Tester5', 'Tester6', 'Tester7', 'Tester8'],
         ['Tester9', 'Tester10', 'Tester11', 'Tester12']]

nicks = [['nickname1', 'nickname2', 'nickname3', 'nickname4'],
         ['nickname5', 'nickname6', 'nickname7', 'nickname8'],
         ['nickname9', 'nickname10', 'nickname11'], 'nickname12']]


sql = "insert into challenges (id, name, description, max_attempts, value, category, type, state) values "

for i in range(3):
    for j in range(4):
        try:
            sql += "(%d, '%s', '%s', 0, %d, '%s', 'standard', 'visible')," % (i*4+j+no+1, names[i][j]+"_server", "http://sinb57.iptime.org:8080/"+nicks[i][j], 80, teams[i])
        except IndexError:
            pass

for i in range(3):
    for j in range(4):
        try:
            sql += "(%d, '%s', '%s', 0, %d, '%s', 'standard', 'visible')," % (i*4+j+no+12, names[i][j]+"_db", "http://sinb57.iptime.org:8080/"+nicks[i][j], 50, teams[i])
        except IndexError:
            pass

sql = sql[:-1]

cur.execute(sql)
conn.commit()



# make flag
now = time.localtime()
hour = now.tm_hour


# select last id
sql = "select id from flags order by id desc limit 1"
cur.execute(sql)
try:
    no = (cur.fetchone())[0]
except TypeError:
    no = 0


sql = "insert into flags (id, challenge_id, type, content) values "

for i in range(3):
    for j in range(4):
        try:
            enc = hashlib.md5()
            key = "hacking_homepage_13st_%s_%s_%s_" % (teams[i], nicks[i][j], "%02d" % hour)
            enc.update((key+"server").encode("utf-8"))
            flag = "flag{" + enc.hexdigest() + "}"
            sql += "(%d, %d, '%s', '%s')," % (i*4+j+no+1, i*4+j+no+1, 'static', flag)
        except IndexError:
            pass


for i in range(3):
    for j in range(4):
        try:
            enc = hashlib.md5()
            key = "hacking_homepage_13st_%s_%s_%s_" % (teams[i], nicks[i][j], "%02d" % hour)
            enc.update((key+"db").encode("utf-8"))
            flag = "flag{" + enc.hexdigest() + "}"

            sql += "(%d, %d, '%s', '%s')," % (i*4+j+no+12, i*4+j+no+12, 'static', flag)
        except IndexError:
            pass

sql = sql[:-1]

cur.execute(sql)
conn.commit()
 
conn.close()