## client

### 계정 생성 및 계정 값 변경 과정

https://github.com/kwon99/KWCTF/blob/137d87a83c7d4500271317e064a0576f8504d9e0/client/client.sql#L2-L3
_user, passwd 변경_
<br /><br />

https://github.com/kwon99/KWCTF/blob/13efbeb754ad11607c0d6c19c88d7adcd32871b3/client/client.py#L3-L5
_team, user, passwd를 변경 (단, user, passwd는 위의 user, passwd와 동일함)_
<br /><br />

```bash
service mysql start
mysql
source /client/client.sql
```

&nbsp;_mysql 시작 및 변경 내용 적용_

<br />

```bash
service cron restart
```

&nbsp;_crontab 시작_

```
challenges 삭제 시 db 생성이 안되는 오류
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
