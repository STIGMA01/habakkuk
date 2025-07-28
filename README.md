# HABAKKUK Project
하박국 3:2 - "여호와여 주는 주의 일을 이 수년 내에 부흥하게 하옵소서"  
하나님의 부흥의 역사를 위한 웹사이트를 만들고자 하였습니다.  

* 부흥 소식
* 세계 각지 교회 소식
* 부흥에 대한 제보


## 아키텍쳐
- **DB:** PostgresSQL
- **BE:** Django(DRF)
- Axios
- **FE:** Vue.js + Naive UI
- Nginx, Docker


## 구성

### .env
ENV: 실행 모드 분기 옵션. dev, local, prod 중에 택해야 하며, entrypoint에 따라 실행 모드가 조절된다.


## 실행
```
# In WSL(Windows Linux Subsystem)
# WSL에서는 도커 Daemon을 직접 실행해주어야 함.
sudo service docker start
```
