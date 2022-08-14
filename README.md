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

### server

#### 필요한 패키지 설치

_\*python3, docker, docker-compose가 설치되어있다면 건너뛰어도 괜찮습니다._

```bash
sudo chmod +x requirement
sudo ./requirement
```

_실행 권한 부여 및 실행_

####
