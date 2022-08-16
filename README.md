<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/kwon99/siegweb">
    <img src="img/siegweb.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">siegweb</h3>
</div>

## 👨‍💻 Introduction
CTFD 기반의 웹 공방전 설정 프로그램
> 서버에서 생성한 FLAG를 클라이언트에 적용, 각 클라이언트를 해킹하며 점수를 얻는 시스템입니다.
<img src="https://github.com/kwon99/siegweb/blob/main/img/ctfd1.png" width="1000">

<br /><br />

## ⚙️ Setting
**클라이언트의 경우 Docker 사용 유무에 따라 나뉩니다.**
> Docker version은 이하의 내용들이 미리 세팅되어있는 Dockerfile을 이용합니다. 
<br/>

**서버의 경우 특별한 분기점은 없습니다.**

#### 설치

```bash
git clone https://github.com/kwon99/siegweb.git /siegweb
```

<br /><br />

## 💻 Client
> 사용되는 단 하나의 파일 (client.py)는 서버로부터 FLAG를 받아와 클라이언트에 넣어주는 역할을 합니다.

#### 시간 설정
```bash
ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
```

#### MySQL 계정 및 FLAG DB 생성
> 이미 공방전용 계정이 존재한다면 아래 두 줄을 삭제하고 진행합니다.
```sql
# client/client.sql
# https://github.com/kwon99/siegweb/blob/7cb5fa8cdaa1dce43f92c87f73dca50616b25424/client/client.sql#L2-L3
# user, passwd 변경
CREATE USER 'user'@'localhost' IDENTIFIED BY 'passwd'; 
GRANT ALL PRIVILEGES ON *.* to 'user'@'localhost'; 
```

```sql
# sql 로그인 이후 진행 (e.g. mysql -u root -p)
source /siegweb/client/client.sql
```

#### FLAG server 생성
```
sudo mkdir /flag && touch /flag/flag
```

#### 계정 값 변경
```python
# client/client.py
# https://github.com/kwon99/siegweb/blob/7cb5fa8cdaa1dce43f92c87f73dca50616b25424/client/client.py#L53-L54
# token, db 정보, 공방전 서버 주소 기입
client = Client("token", "your_database_id", "your_database_pw", "server_address") 
```

#### 실행파일 권한 설정
```bash
sudo chmod 600 /siegweb/client/client.py
```

#### Crontab 설정
```bash
crontab -e

# 마지막 줄에 추가
0 */3 * * * /usr/bin/python3 /siegweb/client/client.py
```

<br /><br />

## 🐳 Client with DOCKER
> Docker는 위 내용들의 대부분을 설정해둔 상태이므로, 변경 부분만 변경합니다.

#### MySQL 계정 및 FLAG DB 생성
> 이미 공방전용 계정이 존재한다면 아래 두 줄을 삭제하고 진행합니다.
```sql
# client/client.sql
# https://github.com/kwon99/siegweb/blob/7cb5fa8cdaa1dce43f92c87f73dca50616b25424/client/client.sql#L2-L3
# user, passwd 변경
CREATE USER 'user'@'localhost' IDENTIFIED BY 'passwd'; 
GRANT ALL PRIVILEGES ON *.* to 'user'@'localhost'; 
```

#### 계정 값 변경
```python
# client/client.py
# https://github.com/kwon99/siegweb/blob/7cb5fa8cdaa1dce43f92c87f73dca50616b25424/client/client.py#L53-L54
# token, db 정보, 공방전 서버 주소 기입
client = Client("token", "your_database_id", "your_database_pw", "server_address") 
```

<br /><br />


## 🖥 Server

#### 시간 설정
```bash
ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
```

#### 필요한 패키지 설치 (python3, docker, docker-compose)

```bash
# 실행 권한 부여 및 실행
sudo chmod +x /siegweb/server/requirement
sudo cd /siegweb/server && ./requirement
```

#### 정보 입력

```python
# https://github.com/kwon99/siegweb/blob/dfa1b264344c76cfcf273af214454041ea0fa161/server/json/user.json#L1-L4
# server/json/user.json
# 참가자 환경에 맞게 내용 변경 (token은 사용자를 인증하는 역할로, 무작위로 생성하셔도 되고, 참가자가 만든 것을 받으셔도 됩니다)
{
    "userA": [1, "Team A", "server_address", "token"],
    "userB": [2, "Team B", "server_address2", "token2"]
}
```

#### CTFD 및 flask 실행
```
sudo cd /seigweb/server && docker-compose up -d
```

#### ctfd 세팅

_서버에 접속해 대회 세팅 및 유저와 팀 등록 하시면 됩니다_

#### DB 연결
```bash
# 여기에 걸린 컨테이너의 이름 복사 (e.g. 7705656~01)
find /var/lib/docker/overlay2/ -name 'ctfd.db'
```

```python
# server/server.py
# https://github.com/kwon99/siegweb/blob/dfa1b264344c76cfcf273af214454041ea0fa161/server/server.py#L153
# your_container_name을 위에서 복사한 내용으로 변경
server = Server("your_container_name", delete)
```

```python
# server/server.py
# https://github.com/kwon99/siegweb/blob/dfa1b264344c76cfcf273af214454041ea0fa161/server/server.py#L8
# ubuntu(linux)를 기준으로 템플릿을 제작했으니 만약 다른 환경일 경우 ctfd.db의 위치를 찾아서 아래 코드의 path 부분을 수정해주시면 됩니다.
self.conn = sqlite3.connect(
    f"/var/lib/docker/overlay2/{path}/merged/opt/CTFd/CTFd/ctfd.db"
)
```

#### crontab 설정

```bash
crontab -e

# 마지막 줄에 추가
0 */3 * * * /usr/bin/python3 /siegweb/server/server.py
```
