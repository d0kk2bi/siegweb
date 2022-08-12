import pymysql, hashlib, time, os


class Client:
    def __init__(self, user, token, db_id, db_pw):
        # 사용자 이름 및 토큰 정보
        self.user = user
        self.token = token

        # 사용자 DB 정보
        self.db_id = db_id
        self.db_pw = db_pw

        # 시간 정보
        self.time_key = time.localtime().tm_hour

    # 토큰을 기반으로 FLAG 생성
    def generate_flag(self):
        # 키 생성
        key = f"kknock_hacking_defence_{self.user}_{self.token}_{self.time_key}_"

        # 데이터베이스의 FLAG 생성
        enc = hashlib.md5
        enc.update((key + "db").encode("utf-8"))
        self.db_flag = f"flag{{{enc.hexdigest()}}}"

        # 서버의 FLAG 생성
        enc = hashlib.md5()
        enc.update((key + "server").encode("utf-8"))
        self.server_flag = f"flag{{{enc.hexdigest()}}}"

    # 데이터베이스에 FLAG 저장
    def save_flag_db(self):
        db = pymysql.connect(
            host="localhost", user=self.db_id, password=self.db_pw, db="flag"
        )

        cursor = db.cursor()
        sql = f"update flag set flag='{self.db_flag}'"
        cursor.execute(sql)

        db.commit()
        db.close()

    # 서버에 FLAG 저장
    def save_flag_server(self):
        directory = "/flag"

        # 디렉토리가 존재하지 않을 경우
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open("/flag/flag", "w", encoding="UTF-8") as f:
            f.write(f"{self.server_flag}\n")


if __name__ == "__main__":
    client = Client("nickname", "your_token", "your_database_id", "your_database_pw")

    client.generate_flag()
    client.save_flag_db()
    client.save_flag_server()
