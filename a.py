import requests

all_flag = requests.get("http://20.214.111.189:1105/?token=token").text
all_flag_lst = all_flag.split("_")

db_flag = all_flag_lst[0]
server_flag = all_flag_lst[1]

print(db_flag)
print(server_flag)
