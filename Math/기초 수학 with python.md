# 기초 수학 with python



## 1. 방정식과 부등식

### 1. Sympy

- 파이썬에서 기호 수학(symbolic math)을 위한 라이브러리
- 속도와 시각화 등에 필요한 확장 기능
- 대수(algebra) 문제
- 기호변수는 `symbol()` 함수 사용
- `from sympy import Symbol, solve` 처럼 미리 정의



> Sympy 라이브러리를 불러오고, 사용할 기호변수 x 선언

```python
from sympy import Symbol, solve
x = Symbol('x')

equation = 2*x-6
solve(equation)
#[3]
```



> 연립방정식

```
x = Symbol('x')
y = Symbol('y')
equation_3 = 3*x+y-2
equation_4 = x-2*y-3

solve((equation_3, equation_4),dict=True)
#[{x: 1, y: -1}]
```



## 2. 지수와 제곱근

### 1. 거듭제곱근

```python
2**5
#32
```



```python
import math
math.sqrt(9)
#3
```



### 2. 전개

- `from sympy import expand, factor, Symbol`

```python
from sympy import expand, factor, Symbol
x = Symbol('x')
x
#𝑥
```

```python
expand((x+1)*(x+5))
𝑥2+6𝑥+5
```



### 3. 인수분해

```python
factor(x**2 + 6*x + 5)
#(𝑥+1)(𝑥+5)
```



## 3. 지수함수, 로그함수

### 1. 지수함수

> 2의 5 제곱

```python
pow = ma.pow(2,5)
print("pow 결과 : ", pow)
# pow 결과 :  32.0
```



> e의 2 제곱

```python
exp = ma.exp(2)
print("exp 결과 : ", exp)
# exp 결과 :  7.38905609893065
```



### 2. 로그함수

> 밑 : 4, 진수 : 2

```python
ma.log(2,4)
# 0.5
```



> 밑 : 2, 진수 : 4

```python
ma.log(4,2)
# 2
```

