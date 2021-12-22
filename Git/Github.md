# Github

## 1. 원격 저장소 (Remote Repository)

### 1. 원격 저장소 생성

- New repository Create



### 2. 로컬 저장소와 원격 저장소 연결

1. 저장소의 주소 복사

![img](https://hphk.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F798d21e0-9c40-4995-b5ed-fc77b9e75bb1%2F%EA%B7%B8%EB%A6%BC5.png?table=block&id=945b1a67-f799-4b86-a09e-466327b33e27&spaceId=daa2d103-3ecd-4519-8c30-4f55e74c7ef4&width=1280&userId=&cache=v2)



2. 홈 디렉토리의 원하는 폴더로 가서 vscode를 연다.



3. `git init` 을 통해 해당 폴더를 로컬 저장소로 만들어준다. (여기선 TIL 폴더)

   ```bash
   $ git init
   ```



4. `git remote` 

- 로컬 저장소에 원격 저장소를 `등록, 조회, 삭제`할 수 있는 명령어

  (1) 원격 저장소 등록

  - `git remote add <이름> <주소>` 형식으로 작성.

    ```bash
    $ git remote add origin https://github.com/edukyle/TIL.git
    ```
  
  
  
  (2) 원격 저장소 조회
  
  - `git remote -v`
  
    ```bash
    $ git remote -v
    ```
  
    
  
  (3) 원격 저장소 연결 삭제
  
  - 로컬과 원격 저장소의 연결을 끊는 것이지, 원격 저장소 자체 삭제x
  
  - `git remote rm <이름>` 혹은 `git remote remove <이름>` 으로 작성
  
    ```bash
    $ git remote rm origin
    $ git remote remove origin
    
    
    [풀이]
    git 명령어를 작성할건데, remote(원격 저장소)와의 연결을 rm(remove, 삭제) 한다.
    그 원격 저장소의 이름은 origin이다.
    ```
  
    

## 3. 원격 저장소에 커밋 업로드

1. 로컬 저장소에서 커밋 생성

   ```bash
   # 현재 상태 확인
   
   $ git status
   ```

   ```bash
   $ git add day1.md
   ```

   ```bash
   $ git commit -m "Upload TIL Day1"
   ```

   ```bash
   # 커밋 확인
   
   $ git log --oneline
   ```



2. `git push`

- 로컬 저장소의 커밋을 원격 저장소에 업로드하는 명령어

- `git push <저장소 이름> <브랜치 이름>` 형식으로 작성.

- `-u` 옵션을 사용하면, 두 번째 커밋부터는 `저장소 이름, 브랜치 이름`을 생략 가능.

  ```bash
  $ git push origin master
  
  [풀이]
  git 명령어를 사용할건데, origin이라는 이름의 원격 저장소의 master 브랜치에 push.
  
  ------------------------------------------------
  
  $ git push -u origin master
  이후에는 $ git push 라고만 작성해도 push가 된다.
  ```

  



