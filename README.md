<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/kwon99/siegweb">
    <img src="img/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">siegweb</h3>
</div>

## 👨‍💻 Introduction
CTFD 기반의 웹 공방전 세팅 프로그램
> 서버에서 생성한 FLAG를 클라이언트에 적용, 각 클라이언트를 해킹하며 점수를 얻는 시스템입니다.

## ⚙️ Setting


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
