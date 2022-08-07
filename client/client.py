import pymysql, hashlib, time, os

team = ""   # Team name
user = ""   # User name (mysql name)
passwd = "" # User password (mysql password)

now = time.localtime()
hour = now.tm_hour

key = "hacking_homepage_13st_%s_%s_%s_" % (team, user, "%02d" % hour)

# make flags
enc = hashlib.md5()
enc.update((key+"server").encode("utf-8"))
flag1 = "flag{" + enc.hexdigest() + "}"

enc = hashlib.md5()
enc.update((key+"db").encode("utf-8"))
flag2 = "flag{" + enc.hexdigest() + "}"


# save flag1 in server
directory = "/flag"

if not os.path.exists(directory):
    os.makedirs(directory)

with open("/flag/flag", "w", encoding="UTF8") as f:
    f.write(flag1+"\n")


# save flag2 in database
db = pymysql.connect(host="localhost",user=user,password=passwd,db="flag")

cursor = db.cursor()

sql = "update flag set flag='%s'" % flag2

cursor.execute(sql)

db.commit()

db.close()