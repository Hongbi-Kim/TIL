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

   

---





# 마크다운(Markdown)

## 정의

1. 마크다운

- 일반 텍스트 기반의 경량 마크업(Markup) 언어

- `.md` 확장자를 가지며, 개발과 관련된 많은 문서는 마크다운 형식으로 작성되어 있다.

- 개발 분야에 있어서 `문서화`는 굉장히 중요한 능력이다. 마크다운은 그 토대가 될 것이다.

	

  (1) 장점
  
   - 문법이 직관적이고 쉽다.
	
   - 관리가 쉽다.
  
   - 지원 가능한 플랫폼과 프로그램이 다양하다.
  
    
  
  (2) 단점
  
   - 표준이 없어 사용자마다 문법이 상이할 수 있다.
  
   - 모든 HTML 마크업 기능을 대신하지는 못한다.
  
     

2. 마크업(Markup)

- 마크업 언어는 말 그대로 마크(Mark)로 둘러싸인 언어.
-  마크(Mark)란 글의 역할을 지정하는 일종의 표시와 같다. 
- 예를 들면 HTML에서 M이 의미하는 것은 Markup 이다. 즉 HTML도 마크업 언어다. HTML에서 제목을 표시할 때는 <h1>제목1</h1> 과 같이 작성한다. 제목1을 둘러싸고 있는 <h1>을 태그(tag)라고 말하며, 마크 역할을 한다. 
- 각각의 글이 제목, 내용, 목록, 인용 등등 어떤 역할을 가지고 있는지 표시하는 것.



## 문법

1. 제목 (Headings)

# 제목 1

## 제목 2

### 제목 3

#### 제목 4

##### 제목 5

###### 제목 6



2. 목록(List)

순서가 없는 목록

- 목록 1
- 목록 2
- 과일
  - 수박
  - 참외
  - 바나나
    - 바나나1



순서가 있는 목록

1. 목록 1

2. 목록 2

   1. 목록 2-1
   2. 목록 2-2

   

3. 강조(스타일링) (Emphasis)

- 기울임(이탤릭체) : *글자*, _글자_

- 굵게(볼드체) : **글자**, __글자__

- 취소선 : ~~글자

  

4. 코드(Code)

- 인라인 코드(=한줄) -> 백틱(backtick) `

​		파이썬에는 `print("Hello World!")` 라고 쓸 수 있음.

- 블록 코드(=여러줄)``` ```

```python
for i in range(10):
	print(i)
```



5. 수평선(Horizontal Rule)

- -, *, _ 3번 연속 작성

---



6. 표(table)

| 동물   | 다리 개수 |
| ------ | --------- |
| 사자   |           |
| 원숭이 |           |
| 앵무새 |           |



7. 인용(Blockquote)

- 주석이나 인용 문구 표현

- `>` 사용

> 인용문을 작성합니다.

> > 중첩된 인용문 1
> >
> > 중첩된 인용문 2



8. 링크(Links)

- `[표시할 글자](이동할 주소)`

```bash
[GOOGLE](https://google.com)을 눌러서 구글로 이동하세요.
```

[GOOGLE](https://google.com)을 눌러서 구글로 이동하세요.



9. 이미지(Images)

- `![대체 택스트](이미지 주소)`
- `대체 텍스트`란 이미지를 정상적으로 불러오지 못했을 때 표시되는 문구.
- Typora에서는 이미지 파일을 끌어와서 놓아도 자동 업로드 된다.

``` bash
Git 로고입니다.
![Git로고](https://git-scm.com/images/logo@2x.png)
```

![Git로고](https://git-scm.com/images/logo@2x.png)

