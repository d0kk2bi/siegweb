import pymysql, requests, os


class Client:
    def __init__(self, token, db_id, db_pw, server_addr):
        # 사용자 이름 및 접속 정보
        self.token = token
        self.flag_addr = f"http://{server_addr}/?token={token}"

        # 사용자 DB 정보
        self.db_id = db_id
        self.db_pw = db_pw

    # 서버에서 FLAG 받아오기
    def get_flag(self):
        print(self.flag_addr)
        # 전체 FLAG 받아오기
        all_flag = requests.get(self.flag_addr).text

        # DB FLAG와 서버 FLAG로 나누기
        all_flag_lst = all_flag.split("_")

        # DB FLAG와 서버 FLAG 값 넣기
        self.db_flag = all_flag_lst[0]
        self.server_flag = all_flag_lst[1]

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
    client = Client("token", "your_database_id", "your_database_pw", "server_address",)
    client.get_flag()
    client.save_flag_db()
    client.save_flag_server()
