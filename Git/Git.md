# 1. Git 기초

## 1. Git 초기 설정

최초 한 번만 설정.

1. 누가 커밋 기록을 남겼는지 확인할 수 있도록 이름과 이메일을 설정

   ```bash
   $ git config --global user.name "이름"
   $ git config --global user.email "메일 주소"
   ```

2. 확인

   ```bash
   $ git config --global -l
   
   또는
   
   $ git config --global --list
   ```

   

## 2. Git 기본 명령어

1. 로컬 저장소

   ![img](https://hphk.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F7142d992-3d01-481c-9d4e-e818c6e185d8%2FUntitled.png?table=block&id=f922af90-788d-4a13-aa3b-75e1b5e2a309&spaceId=daa2d103-3ecd-4519-8c30-4f55e74c7ef4&width=1280&userId=&cache=v2)

- `Working Directory (= Working Tree)` : 사용자의 일반적인 작업이 일어나는 곳
- `Staging Area (= Index)` : 커밋을 위한 파일 및 폴더가 추가되는 곳
- `Repository` : staging area에 있던 파일 및 폴더의 변경사항(커밋)을 저장하는 곳
- Git은 **Working Directory → Staging Area → Repository** 의 과정으로 버전 관리를 수행.



2. git init

- 현재 작업 중인 디렉토리를 Git으로 관리한다는 명령어
- `.git` 이라는 숨김 폴더를 생성하고, 터미널에는 `(master)`라고 표기된다.

```bash
$ git init
```

!! 주의 !!

- git init 중첩 금지!!
- 홈 디렉토리에서 git init 금지
- 터미널의 경로 `~` 인지 확인



3. git status

```bash
$ git status
```

- Working Directory와 Staging Area에 있는 파일의 현재 상태를 알려주는 명령어

- 어떤 작업을 시행하기 전에 수시로 status를 확인하면 좋습니다.

- 상태

  1. `Untracked` : Git이 관리하지 않는 파일 (한번도 Staging Area에 올라간 적 없는 파일)

  2.  `Tracked` : Git이 관리하는 파일

      - `Unmodified` : 최신 상태

     - `Modified` : 수정되었지만 아직 Staging Area에는 반영하지 않은 상태
     
     - `Staged` : Staging Area에 올라간 상태

  ![img](https://hphk.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F67719520-a1d8-4cbb-81dd-49dea429a7f4%2FUntitled.png?table=block&id=c646e753-b20e-4bdb-a77e-00bcd6518f0a&spaceId=daa2d103-3ecd-4519-8c30-4f55e74c7ef4&width=1280&userId=&cache=v2)

  

4. git add

```bash
# 특정 파일
$ git add a.txt

# 특정 폴더
$ git add my_folder/

# 현재 디렉토리에 속한 파일/폴더 전부
$ git add .
```

- Working Directory에 있는 파일을 Staging Area로 올리는 명령어
- Git이 해당 파일을 추적(관리)할 수 있도록 만든다.
- `Untracked, Modified → Staged` 로 상태를 변경.



5. git commit

```bash
$ git commit -m "first commit"
```

- Staging Area에 올라온 파일의 변경 사항을 하나의 버전(커밋)으로 저장하는 명령어
- `커밋 메세지`는 현재 변경 사항들을 잘 나타낼 수 있도록 `의미` 있게 작성하는 것을 권장.
- 각각의 커밋은 `SHA-1` 알고리즘에 의해 반환 된 고유의 해시 값을 ID로 가진다.
- `(root-commit)` 은 해당 커밋이 최초의 커밋 일 때만 표시된다. 이후 커밋부터는 사라짐.



6. git log

```bash
$ git log
```

- 커밋의 내역(`ID, 작성자, 시간, 메세지 등`)을 조회할 수 있는 명령어
- 옵션
  - `--oneline` : 한 줄로 축약
  - `--graph` : 브랜치와 머지 내역을 그래프로
  - `--all` : 현재 브랜치를 포함한 모든 브랜치의 내역
  - `--reverse` : 커밋 내역의 순서를 반대로(최신이 가장 아래)
  - `-p` : 파일의 변경 내용도 같이 보여줌.
  - `-2` : 원하는 갯수 만큼의 내역을 보여줌. (2 말고 임의의 숫자 사용 가능)



7. 한눈에 보는 Git 명령어

![img](https://hphk.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fc86c667a-616f-45b6-892e-15da6a3c494e%2FUntitled.png?table=block&id=64acc3f6-5a25-4342-b6b1-a6a45f61b1f6&spaceId=daa2d103-3ecd-4519-8c30-4f55e74c7ef4&width=1280&userId=&cache=v2)

