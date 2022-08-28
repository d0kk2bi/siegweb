import json
from flask import Flask, request

app = Flask(__name__)

# 계정 정보 가져오기
with open("json/user.json", "r") as u:
    user_dict = json.load(u)


@app.route("/", methods=["GET"])
def flag():
    token = request.args.get("token")
    user = ""

    # 사용자 정보 찾기
    for key, value in user_dict.items():
        if value[3] == token:
            user = key

    # 값이 제대로 들어갔는지 확인
    if user == "":
        return "Incorrect Token"

    # FLAG 정보 불러오기
    with open("json/flag.json", "r") as f:
        flag_dict = json.load(f)

    return flag_dict[user][0] + "_" + flag_dict[user][1]


if __name__ == "__main__":
    app.run()
