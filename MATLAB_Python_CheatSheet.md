# MATLAB to Python 빠른 참조 가이드 (Cheat Sheet)

MATLAB 실무 사용자를 위한 Python 전환 가이드

---

## 🔧 필수 설치

```bash
pip install numpy matplotlib scipy pandas
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat, savemat
import pandas as pd
```

---

## 📊 배열/행렬 생성

| MATLAB | Python (NumPy) | 설명 |
|--------|----------------|------|
| `a = [1, 2, 3]` | `a = np.array([1, 2, 3])` | 1D 배열 |
| `A = [1,2; 3,4]` | `A = np.array([[1,2], [3,4]])` | 2D 배열 |
| `b = 1:5` | `b = np.arange(1, 6)` | 1부터 5까지 ⚠️ |
| `c = 0:0.1:1` | `c = np.arange(0, 1.1, 0.1)` | 0.1 간격 |
| `d = linspace(0,10,5)` | `d = np.linspace(0, 10, 5)` | 균등 간격 |
| `Z = zeros(3,4)` | `Z = np.zeros((3, 4))` | 0 행렬 |
| `O = ones(2,3)` | `O = np.ones((2, 3))` | 1 행렬 |
| `I = eye(3)` | `I = np.eye(3)` | 단위 행렬 |
| `R = rand(2,3)` | `R = np.random.rand(2, 3)` | 난수 행렬 |
| `N = randn(2,3)` | `N = np.random.randn(2, 3)` | 정규분포 난수 |

---

## 🎯 인덱싱 (가장 중요!)

### ⚠️ MATLAB은 1부터, Python은 0부터!

| 작업 | MATLAB | Python |
|------|--------|--------|
| 첫 번째 원소 | `arr(1)` | `arr[0]` |
| 마지막 원소 | `arr(end)` | `arr[-1]` |
| 2~4번째 원소 | `arr(2:4)` | `arr[1:4]` ⚠️ 끝 제외 |
| 모든 원소 | `arr(:)` | `arr[:]` |
| 2행 전체 | `A(2, :)` | `A[1, :]` |
| 3열 전체 | `A(:, 3)` | `A[:, 2]` |
| 특정 원소 | `A(2, 3)` | `A[1, 2]` |

### 슬라이싱 예제
```python
# MATLAB: arr(2:5)  -> 2, 3, 4, 5번째 원소
# Python: arr[1:5]  -> 인덱스 1, 2, 3, 4 (5 제외!)

arr = np.array([10, 20, 30, 40, 50, 60])
arr[1:4]  # [20, 30, 40]  (MATLAB의 arr(2:4))
```

---

## ➗ 배열 연산

| 작업 | MATLAB | Python (NumPy) |
|------|--------|----------------|
| 덧셈 | `a + b` | `a + b` |
| 뺄셈 | `a - b` | `a - b` |
| 원소별 곱 | `a .* b` ⚠️ 점 필요 | `a * b` |
| 원소별 나눗셈 | `a ./ b` ⚠️ 점 필요 | `a / b` |
| 원소별 거듭제곱 | `a .^ 2` ⚠️ 점 필요 | `a ** 2` |
| 행렬 곱셈 | `A * B` | `A @ B` 또는 `np.dot(A, B)` |
| 전치 | `A'` | `A.T` |
| 역행렬 | `inv(A)` | `np.linalg.inv(A)` |

### 예제
```python
# MATLAB:
# a = [1, 2, 3];
# b = [4, 5, 6];
# c = a .* b;    % [4, 10, 18]

# Python:
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a * b      # [4, 10, 18] - 점 연산자 불필요!
```

---

## 📐 수학 함수

| MATLAB | Python (NumPy) |
|--------|----------------|
| `sin(x)` | `np.sin(x)` |
| `cos(x)` | `np.cos(x)` |
| `exp(x)` | `np.exp(x)` |
| `log(x)` | `np.log(x)` (자연로그) |
| `log10(x)` | `np.log10(x)` |
| `sqrt(x)` | `np.sqrt(x)` |
| `abs(x)` | `np.abs(x)` |
| `round(x)` | `np.round(x)` |
| `floor(x)` | `np.floor(x)` |
| `ceil(x)` | `np.ceil(x)` |

---

## 📈 통계 함수

| MATLAB | Python (NumPy) |
|--------|----------------|
| `mean(x)` | `np.mean(x)` |
| `median(x)` | `np.median(x)` |
| `std(x)` | `np.std(x)` |
| `var(x)` | `np.var(x)` |
| `max(x)` | `np.max(x)` |
| `min(x)` | `np.min(x)` |
| `sum(x)` | `np.sum(x)` |
| `cumsum(x)` | `np.cumsum(x)` |
| `prod(x)` | `np.prod(x)` |

---

## 🔄 반복문

### for 반복문

```matlab
% MATLAB
for i = 1:5
    disp(i)
end
```

```python
# Python
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i)
```

### 배열 순회

```matlab
% MATLAB
arr = [10, 20, 30];
for val = arr
    disp(val)
end
```

```python
# Python
arr = np.array([10, 20, 30])
for val in arr:
    print(val)
```

### while 반복문

```matlab
% MATLAB
i = 1;
while i <= 5
    disp(i)
    i = i + 1;
end
```

```python
# Python
i = 1
while i <= 5:
    print(i)
    i += 1
```

---

## 🔀 조건문

```matlab
% MATLAB
if x > 10
    disp('크다')
elseif x > 5
    disp('중간')
else
    disp('작다')
end
```

```python
# Python
if x > 10:
    print('크다')
elif x > 5:      # MATLAB의 elseif
    print('중간')
else:
    print('작다')
```

---

## 🎭 논리 연산

### 스칼라 논리 연산

| MATLAB | Python |
|--------|--------|
| `&&` | `and` |
| `||` | `or` |
| `~` | `not` |

```matlab
% MATLAB
if x > 5 && x < 10
    disp('OK')
end
```

```python
# Python
if x > 5 and x < 10:
    print('OK')
```

### 배열 논리 연산

| MATLAB | Python |
|--------|--------|
| `&` | `&` |
| `|` | `|` |
| `~` | `~` |

```matlab
% MATLAB
mask = (arr > 2) & (arr < 5);
result = arr(mask);
```

```python
# Python
mask = (arr > 2) & (arr < 5)
result = arr[mask]
```

---

## 🔧 함수 정의

### 단일 출력

```matlab
% MATLAB
function result = add_numbers(a, b)
    result = a + b;
end
```

```python
# Python
def add_numbers(a, b):
    result = a + b
    return result
```

### 다중 출력

```matlab
% MATLAB
function [sum_val, prod_val] = calc(a, b)
    sum_val = a + b;
    prod_val = a * b;
end

[s, p] = calc(3, 4);
```

```python
# Python
def calc(a, b):
    sum_val = a + b
    prod_val = a * b
    return sum_val, prod_val  # 튜플 반환

s, p = calc(3, 4)
```

---

## 📊 플로팅

### 기본 플롯

```matlab
% MATLAB
x = linspace(0, 2*pi, 100);
y = sin(x);
figure;
plot(x, y);
xlabel('x');
ylabel('sin(x)');
title('Sine Wave');
grid on;
```

```python
# Python
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.figure()
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Wave')
plt.grid(True)
plt.show()
```

### 다중 플롯

```matlab
% MATLAB
figure;
subplot(2, 1, 1);
plot(x, sin(x));
title('Sin');

subplot(2, 1, 2);
plot(x, cos(x));
title('Cos');
```

```python
# Python
fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(x, np.sin(x))
ax1.set_title('Sin')

ax2.plot(x, np.cos(x))
ax2.set_title('Cos')

plt.tight_layout()
plt.show()
```

### 플롯 스타일

| MATLAB | Python |
|--------|--------|
| `plot(x, y, 'r-')` | `plt.plot(x, y, 'r-')` |
| `plot(x, y, 'bo')` | `plt.plot(x, y, 'bo')` |
| `plot(x, y, 'LineWidth', 2)` | `plt.plot(x, y, linewidth=2)` |
| `hold on` | 불필요 (기본 동작) |
| `legend('A', 'B')` | `plt.legend(['A', 'B'])` |

---

## 💾 파일 입출력

### 텍스트 파일

```matlab
% MATLAB - 저장
data = [1, 2, 3; 4, 5, 6];
save('data.txt', 'data', '-ascii');

% MATLAB - 불러오기
data = load('data.txt');
```

```python
# Python - 저장
data = np.array([[1, 2, 3], [4, 5, 6]])
np.savetxt('data.txt', data)

# Python - 불러오기
data = np.loadtxt('data.txt')
```

### MAT 파일 (MATLAB 파일)

```python
# Python에서 MATLAB 파일 다루기
from scipy.io import savemat, loadmat

# 저장
data_dict = {'matrix': np.array([[1, 2], [3, 4]]),
             'vector': np.array([1, 2, 3])}
savemat('data.mat', data_dict)

# 불러오기
data = loadmat('data.mat')
matrix = data['matrix']
```

### CSV 파일

```matlab
% MATLAB
csvwrite('data.csv', data);
data = csvread('data.csv');
```

```python
# Python
np.savetxt('data.csv', data, delimiter=',')
data = np.loadtxt('data.csv', delimiter=',')

# 또는 Pandas 사용 (더 강력)
import pandas as pd
df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)
df = pd.read_csv('data.csv')
```

---

## 🔨 행렬 조작

| 작업 | MATLAB | Python |
|------|--------|--------|
| 전치 | `A'` | `A.T` |
| Reshape | `reshape(A, m, n)` | `A.reshape(m, n)` |
| 벡터화 | `A(:)` | `A.flatten()` 또는 `A.ravel()` |
| 세로 결합 | `[A; B]` | `np.vstack([A, B])` |
| 가로 결합 | `[A, B]` | `np.hstack([A, B])` |
| 크기 | `size(A)` | `A.shape` |
| 원소 개수 | `numel(A)` | `A.size` |
| 길이 | `length(v)` | `len(v)` |

---

## 🧮 선형 대수

| 작업 | MATLAB | Python |
|------|--------|--------|
| 선형 방정식 | `x = A \ b` | `x = np.linalg.solve(A, b)` |
| 역행렬 | `inv(A)` | `np.linalg.inv(A)` |
| 행렬식 | `det(A)` | `np.linalg.det(A)` |
| 고유값/벡터 | `[V, D] = eig(A)` | `vals, vecs = np.linalg.eig(A)` |
| SVD | `[U, S, V] = svd(A)` | `U, S, V = np.linalg.svd(A)` |
| Rank | `rank(A)` | `np.linalg.matrix_rank(A)` |
| Norm | `norm(A)` | `np.linalg.norm(A)` |

---

## 📦 데이터 구조

### 셀 배열 → 리스트

```matlab
% MATLAB
data = {1, 'hello', [1,2,3]};
data{1}  % 1
data{2}  % 'hello'
```

```python
# Python
data = [1, 'hello', [1, 2, 3]]
data[0]  # 1
data[1]  # 'hello'
```

### 구조체 → 딕셔너리

```matlab
% MATLAB
person.name = 'John';
person.age = 30;
person.scores = [85, 90, 92];
```

```python
# Python
person = {
    'name': 'John',
    'age': 30,
    'scores': [85, 90, 92]
}
```

---

## ⚠️ 주요 함정 (Gotchas)

### 1. 인덱스는 0부터!
```python
# MATLAB: arr(1) = 첫 번째
# Python: arr[0] = 첫 번째
```

### 2. 슬라이싱 끝 값 제외
```python
# MATLAB: arr(2:5)  -> 2, 3, 4, 5
# Python: arr[1:5]  -> 1, 2, 3, 4 (5 제외!)
```

### 3. range()는 끝 값 제외
```python
# MATLAB: for i = 1:5  -> 1, 2, 3, 4, 5
# Python: for i in range(1, 6): -> 1, 2, 3, 4, 5
```

### 4. 행렬 곱셈 vs 원소별 곱셈
```python
# MATLAB: A * B (행렬), A .* B (원소별)
# Python: A @ B (행렬), A * B (원소별)
```

### 5. NumPy 배열은 복사가 아닌 참조
```python
# 주의!
a = np.array([1, 2, 3])
b = a        # 참조 (같은 메모리)
b[0] = 999
print(a)     # [999, 2, 3] - a도 변경됨!

# 복사하려면
b = a.copy()  # 독립적인 복사본
```

---

## 🚀 실전 팁

### 1. 대화형 개발
```bash
# IPython 사용 (MATLAB Command Window와 유사)
pip install ipython
ipython
```

### 2. Jupyter Notebook (MATLAB Live Script와 유사)
```bash
pip install jupyter
jupyter notebook
```

### 3. 디버깅
```python
# MATLAB의 keyboard와 유사
import pdb; pdb.set_trace()  # 중단점

# 또는 더 간단히 (Python 3.7+)
breakpoint()
```

### 4. 도움말
```python
# MATLAB: help function_name
# Python:
help(np.array)
np.array?  # IPython에서
```

### 5. 변수 확인
```python
# MATLAB: whos
# Python (IPython):
%whos

# 일반 Python:
locals()  # 로컬 변수
globals()  # 전역 변수
```

---

## 📚 추가 학습 자료

### 필수 패키지
- **NumPy**: 배열/행렬 연산
- **Matplotlib**: 플로팅
- **SciPy**: 과학 계산
- **Pandas**: 데이터 분석

### 유용한 링크
- [NumPy for MATLAB users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html)
- [SciPy Lecture Notes](https://scipy-lectures.org/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)

---

## 🎯 빠른 시작 템플릿

```python
# Python 과학 계산 표준 시작 코드
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal, optimize, integrate
import pandas as pd

# 설정
np.set_printoptions(precision=4, suppress=True)
plt.style.use('seaborn-v0_8-darkgrid')

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 플롯
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('My Plot')
plt.grid(True)
plt.show()
```

---

**이 가이드를 즐겨찾기해두고 필요할 때 참조하세요!**
