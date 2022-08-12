import sqlite3, hashlib, time, json, random

class Server:

    def __init__(self, path):
        # db 연결
        self.conn = sqlite3.connect(
            f"/var/lib/docker/overlay2/{path}/merged/opt/CTFd/CTFd/ctfd.db"
        )
        self.cur = self.conn.cursor()

        # 계정 정보 불러오기
        with open('user.json', 'r') as f:
            self.user = json.load(f)

        # hidden 방지
        self.cur.execute("update challenges set state='hidden'")
        self.conn.commit()

        # 시간 정보
        self.time_key = time.localtime().tm_hour

    # challenge 혹은 flag의 마지막 번호 찾기
    def select_last(self, condition):
        self.cur.execute(
            f"select id from {condition} order by id desc limit 1"
            )
        try:
            return (self.cur.fetchone())[0]
        except TypeError:
            return 0

    # FLAG 생성
    def generate_flag(self, username, condition):
        enc = hashlib.md5()
        random_key = random.random
        key = f"kknock_hack_def_{str(random_key)}_{self.user[username]}_{self.time_key}"

        enc.update((key + condition).encode("utf-8"))

        return f"flag{{{enc.hexdigest()}}}"

 
if "__name__" == "__main__":
    server = Server()