6) 가상환경 리눅스 시스템에 인터넷 되게 하는 방법
[전체 과정]
- root 접속
- 리눅스 시작 버튼 클릭
- 시스템 도구 설정 클릭
- 네트워크 클릭
- 유선 켬
- firefox 키고 구글로 접속

- 설정 클릭 >> 네트워크 >> 유선 (켬) 변경 
  - 옆에 위치한 톱니바퀴 클릭 

- 자동으로 연결 클릭>> 적용



7) putty 이용 리눅스 서버 접속하기

   - https://www.putty.org/ 에서 putty 다운
     64-bit x86 다운 

   - oracle VM 버츄얼박스 관리자로 가서 
     메뉴>> 파일>> 호스트 네트워트 관리자 클릭하고 속성을 확인 
     기본적으로 ipv4 주소 : 192.168.56.1

   - /etc/hosts.allow 파일 열어 맨 아래에 아래 내용 적어줌
     sshd:192.168.56.1
     - linux 창에 오른쪽 마우스 >> 터미널 열기

   [root@localhost ~]# cd /etc
   [root@localhost etc]# vi hosts.allow

   - vi 편집기
     - o(편집모드) 아래로 내려가 sshd:192.168.56.1 입력
     - esc(일반모드) 키 누름
     - shift + : >> :wq! 저장하고 나옴

   - oracle vm 설정 >> 네트워크 >> 고급 >> 포트포워딩 
     누르고 ip 주소와 port 번호를 똑같이 적어줌
     - 터미널 창에 ifconfig 입력
       inet 10.0.2.15 확인
     - inet 10.0.2.15 와 192.168.56.1 과 연결

   - 오라클 vm >> 설정 >> 네트워크 >> 고급 >> 포트포워딩 클릭
     - 플러스 버튼 클릭
     - 호스트 ip: 192.168.56.1, 호스트포트:22
       게스트 ip: 10.0.2.15, 게스트포트:22 
     - 액세스 허용

   - putty 실행, host name에 ip 주소 입력 
     - Host Name : 192.168.56.1 >> open
     - accept

   - login as:root 
   login as: root
   root@192.168.56.1's password:
   Last login: Thu Dec 23 01:59:32 2021
   [root@localhost ~]#

   - putty configuration 
     - appearance 클릭 >> change 클릭
     - 글씨 크기: 28

- colour : use system colou