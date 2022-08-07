# 새 계정 생성 및 권한 부여
CREATE USER 'user'@'localhost' IDENTIFIED BY 'passwd';
GRANT ALL PRIVILEGES ON *.* to 'user'@'localhost';

# 데이터베이스 생성 및 사용
CREATE DATABASE flag;
USE flag;

# 테이블 생성 및 flag 컬럼과 포맷 추가
CREATE TABLE flag (flag VARCHAR(50));
INSERT INTO flag VALUES ("flag{}");