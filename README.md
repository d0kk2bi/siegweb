<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/kwon99/siegweb">
    <img src="img/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">siegweb</h3>
</div>

## 👨‍💻 Introduction
CTFD 기반의 웹 공방전 설정 프로그램
> 서버에서 생성한 FLAG를 클라이언트에 적용, 각 클라이언트를 해킹하며 점수를 얻는 시스템입니다.
<img src="https://github.com/kwon99/siegweb/blob/main/img/ctfd1.png" width="1000">

## ⚙️ Setting
**클라이언트의 경우 Docker 사용 유무에 따라 나뉩니다.**
> Docker version은 이하의 내용들이 미리 세팅되어있는 Dockerfile을 이용합니다. 
<br/>

**서버의 경우 특별한 분기점은 없습니다.**

### 설치

```bash
git clone https://github.com/kwon99/siegweb.git /siegweb
```

## 💻 Client
> 사용되는 단 하나의 파일 (client.py)는 서버로부터 FLAG를 받아와 클라이언트에 넣어주는 역할을 합니다.

### 시간 설정
```bash
ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
```

### MySQL 계정 및 FLAG DB 생성
> 이미 공방전용 계정이 존재한다면 아래 두 줄을 삭제하고 진행합니다.

https://github.com/kwon99/siegweb/blob/7cb5fa8cdaa1dce43f92c87f73dca50616b25424/client/client.sql#L2-L3
_user, passwd 변경_
<br />
```sql
# sql 로그인 이후 진행 (e.g. mysql -u root -p)
source /siegweb/client/client.sql
```

### FLAG server 생성
```
sudo mkdir /flag && touch /flag/flag
```

### 계정 값 변경
https://github.com/kwon99/siegweb/blob/7cb5fa8cdaa1dce43f92c87f73dca50616b25424/client/client.py#L53-L54
_token, db 정보, 공방전 서버 주소 기입_

### 실행파일 권한 설정
```bash
sudo chmod 600 /siegweb/client/client.py
```

### Crontab 설정
```bash
crontab -e

# 마지막 줄에 추가
0 */3 * * * /usr/bin/python3 /siegweb/client/client.py
```

## 🐳 Client with DOCKER
Docker
## 계정 생성 및 계정 값 변경 과정

https://github.com/kwon99/KWCTF/blob/171b2ce9a77e3de061f29d5ef94d705b0c56e9d6/client/client.py#L54
_token, db 정보, 공방전 서버 주소 기입_
<br /><br />

### crontab 설정

```bash
crontab -e
```

```
* * * * * /usr/bin/python3 /설치한 경로/KWCTF/server/server.py
```

## server

### 필요한 패키지 설치 (python3, docker, docker-compose)

```bash
sudo chmod +x requirement
sudo ./requirement
```

_실행 권한 부여 및 실행_

### 정보 입력

https://github.com/kwon99/KWCTF/blob/dfa1b264344c76cfcf273af214454041ea0fa161/server/json/user.json#L1-L4
_참가자 환경에 맞게 내용 변경 (token은 비밀번호 역할로, 무작위로 생성하셔도 되고, 참가자가 만든 것을 받으셔도 됩니다)_
<br /><br />

### docker-compose 실행

```
sudo docker-compose up -d
```

### ctfd 세팅

_서버에 접속해 대회 세팅 및 유저와 팀 등록 하시면 됩니다_

### DB 연결

https://github.com/kwon99/KWCTF/blob/dfa1b264344c76cfcf273af214454041ea0fa161/server/server.py#L153
_이 부분의 'your_container_name'을 변경합니다._
<br /><br />

```
find /var/lib/docker/overlay2/ -name 'ctfd.db'
```

_여기에 걸린 ctfd 컨테이너의 이름을 긁어와서 붙혀주시면 됩니다. (e.g. 7705646~)_

https://github.com/kwon99/KWCTF/blob/dfa1b264344c76cfcf273af214454041ea0fa161/server/server.py#L8
_ubuntu(linux)를 기준으로 템플릿을 제작했으니 만약 다른 환경일 경우 위 코드의 path 부분을 수정해주시면 됩니다._
<br /><br />

### crontab 설정

```bash
crontab -e
```

```
* * * * * /usr/bin/python3 /설치한 경로/KWCTF/server/server.py
```

_원하는 시간만큼 설정하시면 됩니다._
