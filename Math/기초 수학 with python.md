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

