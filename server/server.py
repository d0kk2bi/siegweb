import sqlite3, hashlib, time, json, random, sys


class Server:
    def __init__(self, path, delete):
        # db 연결
        self.conn = sqlite3.connect(
            f"/var/lib/docker/overlay2/{path}/merged/opt/CTFd/CTFd/ctfd.db"
        )

        self.cur = self.conn.cursor()

        # 계정 정보 불러오기
        with open("user.json", "r") as f:
            self.user_dict = json.load(f)

        # 이전 문제들 hidden 처리 (삭제와 유사하게 작동하게 됨)
        self.cur.execute("update challenges set state='hidden'")
        self.conn.commit()

        # 이전 문제들 삭제 처리
        if delete == "--delete":
            self.cur.execute("delete from challenges")
            self.conn.commit()

            self.cur.execute("delete from flags")
            self.conn.commit()

        # 시간 정보
        self.time_key = time.localtime().tm_hour

    # challenge 혹은 flag의 마지막 번호 찾기
    def select_last(self, condition):
        self.cur.execute(f"select id from {condition} order by id desc limit 1")
        try:
            return (self.cur.fetchone())[0]
        except TypeError:
            return 0

    # FLAG 생성
    def generate_flag(self, user, condition):
        enc = hashlib.md5()
        random_key = random.random
        key = "kknock_hack_def_%s_%s_%s_" % (
            str(random_key),
            self.user_dict[user],
            self.time_key,
        )

        enc.update((key + condition).encode("utf-8"))

        return f"flag{{{enc.hexdigest()}}}"

    # 사용자 별 FLAG 생성해서 json에 저장
    def flag_save(self):
        # 이후에 db, server에 flag 넣을 때 사용해야 하므로 self 지정
        self.flag_dict = {}

        # 딕셔너리에 데이터베이스, 서버의 FLAG 추가
        for user in self.user_dict:
            self.flag_dict[user] = [
                self.generate_flag(user, "db"),
                self.generate_flag(user, "server"),
            ]

        # json 파일에 쓰기
        with open("flag.json", "w") as f:
            json.dump(self.flag_dict, f, indent=4)

    # challenge 생성
    def db_setting_challenge(self):
        sql = "insert into challenges (id, name, description, max_attempts, value, category, type, state) values "

        # db challenge 생성
        for key in self.user_dict:
            try:
                sql += "(%d, '%s', '%s', 0, %d, '%s', 'standard', 'visible')," % (
                    self.user_dict[key][0] + self.select_last("challenges"),
                    key + "_db",
                    self.user_dict[key][2],
                    100,
                    self.user_dict[key][1],
                )
            except IndexError:
                pass

        # server challenge 생성
        for key in self.user_dict:
            try:
                sql += "(%d, '%s', '%s', 0, %d, '%s', 'standard', 'visible')," % (
                    self.user_dict[key][0]
                    + self.select_last("challenges")
                    + len(self.user_dict),
                    key + "_server",
                    self.user_dict[key][2],
                    300,
                    self.user_dict[key][1],
                )
            except IndexError:
                pass

        # 마지막 쉼표 제거
        sql = sql[:-1]

        # SQL 적용
        self.cur.execute(sql)
        self.conn.commit()

    # FLAG 생성
    def db_setting_flag(self):
        sql = "insert into flags (id, challenge_id, type, content) values "

        # db FLAG 생성
        for key in self.user_dict:
            try:
                sql += "(%d, %d, '%s', '%s')," % (
                    self.user_dict[key][0] + self.select_last("flags"),
                    self.user_dict[key][0] + self.select_last("flags"),
                    "static",
                    self.flag_dict[key][0],
                )
            except IndexError:
                pass

        # server FLAG 생성
        for key in self.user_dict:
            try:
                sql += "(%d, %d, '%s', '%s')," % (
                    self.user_dict[key][0]
                    + self.select_last("flags")
                    + len(self.user_dict),
                    self.user_dict[key][0]
                    + self.select_last("flags")
                    + len(self.user_dict),
                    "static",
                    self.flag_dict[key][1],
                )
            except IndexError:
                pass

        # 마지막 쉼표 제거
        sql = sql[:-1]

        # SQL 적용
        self.cur.execute(sql)
        self.conn.commit()


if __name__ == "__main__":
    # DB 초기화 여부
    delete = sys.argv[1]

    server = Server("your_container_name", delete)

    server.flag_save()

    server.db_setting_challenge()
    server.db_setting_flag()
