## client

### 계정 생성 및 계정 값 변경 과정
https://github.com/kwon99/KWCTF/blob/9f17afe931917d0c68c6efc6adaaace64174b7dc/client/client.sql#L2-L3
_USERID, USERPW를 변경_
<br>
https://github.com/kwon99/KWCTF/blob/13efbeb754ad11607c0d6c19c88d7adcd32871b3/client/client.py#L3-L5
_team, user, passwd를 변경 (단, user, passwd는 위의 USERID, USERPW와 동일함)_

```sql
mysql
source /client/client.sql
```
```shell
service cron restart
```