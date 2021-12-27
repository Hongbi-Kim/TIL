# Crawling API, Web

- 패키지 설치

```python
!pip install openpyxl
!pip install bs4
!pip install Workbook
```



### 1. 약국정보 서비스 API 

```python
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from openpyxl.workbook import Workbook
```



1. 서비스 사용

- 서비스 Key 발급 받기
- 원하는 오픈 API 결과값 받기

![image-20211227231501916](API Crowling.assets/image-20211227231501916-16406145027951.png)



2. 서비스 인증키 활용

- 참고문서를 보고 호출에 필요한 URL 정보확인

- REST 방식

![image-20211227231640090](API Crowling.assets/image-20211227231640090.png)



![image-20211227232157923](API Crowling.assets/image-20211227232157923.png)



![image-20211227232228281](API Crowling.assets/image-20211227232228281.png)



3. 호출하기

- `BeautifulSoup` : HTML 분석을 위한 파이썬 라이브러리
  - beautifulsoup(html 코드, html 번역선생님)

```python
list_drugs = ['병원명','종별코드명','시도명','주소','전화번호']

for list_drug in list_drugs:
    url = api.format(list_drug, key=apikey)
    req = requests.get(url)    #URL에 대화 시도
    re = req.text              #해당 서버에서 html을 줌
    soup = BeautifulSoup(re, 'html.parser')
    
    # 병원명
    yadmnm = soup.find_all('yadmnm')
    
    # 종별코드명
    sggucdnm = soup.find_all('sggucdnm')
    
    # 시도명
    sido = soup.find_all('sido')
    
    # 주소
    addr = soup.find_all('addr')
    
    # 전화번호
    telno = soup.find_all('telno')
    
print("병원명", yadmnm)
print("종별코드명", sggucdnm)
print("시도명", sido)
print("주소", addr)
print("전화번호", telno)
```



### 2. 네이버 날씨 크롤링

- https://weather.naver.com/today

```python
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
```



1. URL을 `html`형태로 불러오기

```python
html = requests.get("https://weather.naver.com/today")
soup = bs(html.text, "html.parser")
print(soup)
```



![image-20211227233845814](API Crowling.assets/image-20211227233845814.png)

![image-20211227233813526](API Crowling.assets/image-20211227233813526.png)



2. 미세먼지 부분만

```
dustdata_one = soup.find('ul',{'class':'today_chart_list'})
print(dustdata_one)
```

![image-20211227234039566](API Crowling.assets/image-20211227234039566.png)



3. 원하는 부분만 뽑아오기

```python
dustdata_all = dustdata_one.findAll('div')
print(dustdata_all)
```

![image-20211227234125455](API Crowling.assets/image-20211227234125455.png)



```python
dustdata_all[0]
```

![image-20211227234249610](API Crowling.assets/image-20211227234249610-16406161736693.png)



```python
dustdata_all[1]
```

![image-20211227234307425](API Crowling.assets/image-20211227234307425.png)



```python
find_dust_code = dustdata_all[0].find("em",{'class':'level_text'})
find_dust_code
```

![image-20211227234334392](API Crowling.assets/image-20211227234334392-16406162191994.png)



```python
dustdata_all[0].find("em",{'class':'level_text'}).text
```

![image-20211227234408234](API Crowling.assets/image-20211227234408234.png)

