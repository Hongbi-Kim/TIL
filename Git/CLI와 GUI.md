# CLI와 GUI

![img](https://hphk.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff889708b-b1fb-4087-bffb-8253c6f007df%2FUntitled.png?table=block&id=fee83bdf-078e-4b7b-a60e-02875544268b&spaceId=daa2d103-3ecd-4519-8c30-4f55e74c7ef4&width=1550&userId=&cache=v2)

왼쪽이 GUI, 오른쪽이 CLI

## 정의

- CLI란? (Graphic User Interface)

​	 	: 터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식

- GUI란? (Command Line Interface)

​      : 그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식

- Interface(인터페이스) 

  : 인터페이스란 원래 서로 다른 개체끼리 맞닿아 있는 면을 뜻합니다. 여기에서는 <u>사용자와 컴퓨터가 서로 소통하는 접점</u>이라고 이해하도록 합시다.

---



## 경로

1. 루트, 홈 디렉토리

   (1) 루트 디렉토리 (Root Directory, `/`)

   - 모든 파일과 폴더를 담고 있는 최상위 폴더이다.
   - Windows의 경우 보통은 `c 드라이브`를 의미한다.

   (2) 홈 디렉토리 (Home Directory, `~`)

   - `Tilde(틸드)`라고도 부르며, 현재 로그인 된 사용자의 홈 폴더를 의미한다.
   - Windows의 경우 `C:/사용자(Users)/현재 사용자 계정`을 의미한다.



2. 절대 경로와 상대 경로

   (1) 절대 경로 : 루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것

   - 윈도우 바탕 화면의 절대 경로 `/c/Users/khb16` : pwd로 확인
   
   (2) 상대 경로 : 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것
   
   - `./` : 현재 작업하고 있는 폴더.
   - `../` : 현재 작업하고 있는 폴더의 부모 폴더.
   
   

3. 터미널 명령어	

   (1) `touch` : 파일을 생성

   ```bash
   $ touch a.txt
   ```

   

   (2) `mkdir`(make directory) : 새 폴더를 생성

   ```bash
   $ mkdir CLI
   $ mkdir 'happy hacking' #폴더 이름 사이에 공백 넣을 때
   ```

   

   (3) `ls`(list segment) : 현재 작업 중인 디렉터뢰의 폴더/파일 목록을 보여줌.

   -  `-a` : all 옵션. 숨김 파일까지 모두 보여 줌.
   - `-1` : long 옵션. 용량, 수정 날짜 등 파일 정보를 자세히 보여줌.

   ```bash
   $ ls # 기본 사용
   $ ls -a # all 옵션
   $ ls -a -l # all, long 옵션 함께 적용
   $ ls -al # 여러 옵션 축약 가능
   ```

   

   (4) `mv` (move) : 

   - 폴더/파일을 다른 폴더 내로 이동 하거나 이름을 변경
   - 단, 다른 폴더로 이동할 때는 작성한 폴더가 반드시 있어야 한다. 없으면 이름이 바뀜.

   ```bash
   # text.txt를 folder 폴더 안에 넣을 때
   $ mv text.txt folder
   
   # text1.txt의 이름을 text2.txt로 바꿀 때
   $ mv text1.txt text2.txt
   ```

   

   (5) `cd` (chane directory) : 현재 작업 중인 디렉토리를 변경

   - `cd ~` 를 입력하면 홈 디렉토리로 이동. (단순히 `cd` 라고만 입력해도 동일.)
   - `cd ..` 를 입력하면 부모 디렉토리로 이동. (위로 가기)
   - `cd -` 를 입력하면 바로 전 디렉토리로 이동. (뒤로 가기)

   ```bash
   # 현재 작업 중인 디렉토리에 있는 folder 폴더로 이동
   $ cd folder
   
   # 절대 경로를 통한 디렉토리 변경
   $ cd C:/Users/kyle/Desktop
   
   # 상대 경로를 통한 디렉토리 변경
   $ cd ../parent/child
   ```

   

   (6) `rm` (remove) : 폴더/파일 영구 삭제.

   - `*(asterisk, wildcard)`를 사용해서 `rm *.txt` 라고 입력하면 txt 파일 전체를 다 지운다.
   - `-r` : recursive 옵션. 폴더를 지울 때 사용.

   ```bash
   $ rm a.txt
   $ rm -r folder
   ```

   

   (7) `start` : 폴더/파일을 연다.

   ```bash
   $ start test.txt
   ```

   

   (8) 유용한 단축키

   - `위, 아래 방향키` : 과거에 작성했던 명령어 조회
   - `tab` : 폴더/파일 이름 자동 완성
   - `ctrl + a` : 커서가 맨 앞으로 이동
   - `ctrl + e` : 커서가 맨 뒤로 이동
   - `ctrl + w` : 커서가 앞 단어를 삭제
   - `ctrl + l` : 터미널 화면을 깨끗하게 청소 (스크롤 올리면 과거 내역 조회 가능)
   - `ctrl + insert` : 복사
   - `shift + insert` : 붙여넣기

   


