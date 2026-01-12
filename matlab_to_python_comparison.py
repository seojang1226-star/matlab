"""
MATLAB to Python 전환 가이드
MATLAB 실무 사용자를 위한 Python 문법 비교

이 파일은 MATLAB 사용자가 Python으로 전환할 때 필요한
주요 문법과 개념을 비교합니다.
"""

# ============================================
# 1. 기본 문법 비교
# ============================================
print("=== 1. 기본 문법 비교 ===\n")

# MATLAB: 세미콜론(;)으로 출력 억제
# a = 5;        % 출력 안됨
# b = 10        % 출력됨

# Python: 기본적으로 출력 안됨
a = 5          # 출력 안됨
b = 10         # 출력 안됨
print(b)       # 명시적으로 출력해야 함

# 주석
# MATLAB: % 이것은 주석입니다
# Python: # 이것은 주석입니다

"""
MATLAB:
%{
여러 줄
주석
%}

Python:
여러 줄 주석은
큰따옴표 3개로
"""


# ============================================
# 2. 변수와 데이터 타입
# ============================================
print("=== 2. 변수와 데이터 타입 ===\n")

# MATLAB: 모든 것이 행렬 (double 기본)
# x = 5;                % 1x1 행렬
# y = 'hello';          % 문자 배열
# z = [1, 2, 3];        % 1x3 행렬

# Python: 다양한 타입
x = 5                  # 정수 (int)
y = "hello"            # 문자열 (str)
z = [1, 2, 3]          # 리스트 (list)

print(f"x = {x}, type: {type(x)}")
print(f"y = {y}, type: {type(y)}")
print(f"z = {z}, type: {type(z)}")


# ============================================
# 3. 배열/행렬 생성 (NumPy 사용)
# ============================================
print("\n=== 3. 배열/행렬 생성 ===\n")

import numpy as np

# --- 벡터 생성 ---
# MATLAB: a = [1, 2, 3, 4, 5];
a_matlab = np.array([1, 2, 3, 4, 5])
print(f"벡터: {a_matlab}")

# MATLAB: b = 1:5;
b_matlab = np.arange(1, 6)  # 주의: 끝 값 6은 포함 안됨!
print(f"1:5 = {b_matlab}")

# MATLAB: c = 0:0.1:1;
c_matlab = np.arange(0, 1.1, 0.1)  # 또는 np.linspace(0, 1, 11)
print(f"0:0.1:1 = {c_matlab}")

# MATLAB: d = linspace(0, 10, 5);
d_matlab = np.linspace(0, 10, 5)
print(f"linspace(0, 10, 5) = {d_matlab}")

# --- 행렬 생성 ---
# MATLAB: A = [1, 2, 3; 4, 5, 6; 7, 8, 9];
A_matlab = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
print(f"\n행렬 A:\n{A_matlab}")

# MATLAB: B = zeros(3, 4);
B_matlab = np.zeros((3, 4))
print(f"\nzeros(3, 4):\n{B_matlab}")

# MATLAB: C = ones(2, 3);
C_matlab = np.ones((2, 3))
print(f"\nones(2, 3):\n{C_matlab}")

# MATLAB: D = eye(3);
D_matlab = np.eye(3)
print(f"\neye(3):\n{D_matlab}")

# MATLAB: E = rand(2, 3);
E_matlab = np.random.rand(2, 3)
print(f"\nrand(2, 3):\n{E_matlab}")


# ============================================
# 4. 인덱싱 (가장 중요한 차이!)
# ============================================
print("\n=== 4. 인덱싱 (매우 중요!) ===\n")

arr = np.array([10, 20, 30, 40, 50])

# MATLAB: 인덱스가 1부터 시작
# arr(1)    -> 10
# arr(5)    -> 50
# arr(end)  -> 50

# Python: 인덱스가 0부터 시작
print(f"arr[0] = {arr[0]}     (MATLAB의 arr(1))")
print(f"arr[4] = {arr[4]}     (MATLAB의 arr(5))")
print(f"arr[-1] = {arr[-1]}   (MATLAB의 arr(end))")

# 슬라이싱 차이
# MATLAB: arr(2:4)     -> [20, 30, 40] (2, 3, 4번째 원소)
# Python: arr[1:4]     -> [20, 30, 40] (끝 인덱스 포함 안됨!)
print(f"\narr[1:4] = {arr[1:4]}   (MATLAB의 arr(2:4))")

# 2D 배열 인덱싱
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# MATLAB: matrix(2, 3)  -> 6
# Python: matrix[1, 2]  -> 6 (0부터 시작!)
print(f"\nmatrix[1, 2] = {matrix[1, 2]}   (MATLAB의 matrix(2,3))")

# MATLAB: matrix(2, :)  -> [4, 5, 6]
# Python: matrix[1, :]  -> [4, 5, 6]
print(f"matrix[1, :] = {matrix[1, :]}   (MATLAB의 matrix(2,:))")

# MATLAB: matrix(:, 2)  -> [2; 5; 8]
# Python: matrix[:, 1]  -> [2 5 8]
print(f"matrix[:, 1] = {matrix[:, 1]}   (MATLAB의 matrix(:,2))")


# ============================================
# 5. 배열 연산
# ============================================
print("\n=== 5. 배열 연산 ===\n")

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# MATLAB: c = a + b;    (원소별 덧셈)
c = a + b
print(f"a + b = {c}")

# MATLAB: d = a .* b;   (원소별 곱셈, 점 필요!)
# Python: d = a * b     (NumPy는 기본이 원소별)
d = a * b
print(f"a * b = {d}")

# MATLAB: e = a.^2;     (원소별 제곱)
# Python: e = a**2
e = a**2
print(f"a**2 = {e}")

# 행렬 곱셈
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# MATLAB: C = A * B;    (행렬 곱셈)
# Python: C = A @ B 또는 np.dot(A, B)
C = A @ B
print(f"\nA @ B (행렬 곱):\n{C}")

# MATLAB: D = A .* B;   (원소별 곱셈)
# Python: D = A * B
D = A * B
print(f"\nA * B (원소별 곱):\n{D}")


# ============================================
# 6. 수학 함수
# ============================================
print("\n=== 6. 수학 함수 ===\n")

x = np.array([0, np.pi/4, np.pi/2, np.pi])

# MATLAB          Python (NumPy)
# sin(x)          np.sin(x)
# cos(x)          np.cos(x)
# exp(x)          np.exp(x)
# log(x)          np.log(x)      (자연로그)
# log10(x)        np.log10(x)
# sqrt(x)         np.sqrt(x)
# abs(x)          np.abs(x)

print(f"sin(x) = {np.sin(x)}")
print(f"cos(x) = {np.cos(x)}")
print(f"exp([1,2,3]) = {np.exp([1,2,3])}")

# 통계 함수
data = np.array([1, 2, 3, 4, 5])

# MATLAB          Python (NumPy)
# mean(data)      np.mean(data)
# std(data)       np.std(data)
# max(data)       np.max(data)
# min(data)       np.min(data)
# sum(data)       np.sum(data)

print(f"\nmean = {np.mean(data)}")
print(f"std = {np.std(data)}")
print(f"max = {np.max(data)}")
print(f"sum = {np.sum(data)}")


# ============================================
# 7. 반복문
# ============================================
print("\n=== 7. 반복문 ===\n")

# --- for 반복문 ---
print("for 반복문:")

# MATLAB:
# for i = 1:5
#     disp(i)
# end

# Python:
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(f"  i = {i}")

# 배열 순회
print("\n배열 순회:")
arr = np.array([10, 20, 30, 40])

# MATLAB:
# for val = arr
#     disp(val)
# end

# Python:
for val in arr:
    print(f"  val = {val}")

# --- while 반복문 ---
print("\nwhile 반복문:")

# MATLAB:
# i = 1;
# while i <= 3
#     disp(i)
#     i = i + 1;
# end

# Python:
i = 1
while i <= 3:
    print(f"  i = {i}")
    i += 1  # i = i + 1과 동일


# ============================================
# 8. 조건문
# ============================================
print("\n=== 8. 조건문 ===\n")

score = 85

# MATLAB:
# if score >= 90
#     grade = 'A';
# elseif score >= 80
#     grade = 'B';
# else
#     grade = 'C';
# end

# Python:
if score >= 90:
    grade = 'A'
elif score >= 80:  # MATLAB의 elseif
    grade = 'B'
else:
    grade = 'C'

print(f"점수 {score} -> 등급 {grade}")


# ============================================
# 9. 함수 정의
# ============================================
print("\n=== 9. 함수 정의 ===\n")

# MATLAB:
# function result = add_numbers(a, b)
#     result = a + b;
# end

# Python:
def add_numbers(a, b):
    result = a + b
    return result

print(f"add_numbers(10, 20) = {add_numbers(10, 20)}")

# 여러 값 반환
# MATLAB:
# function [sum_val, prod_val] = calc(a, b)
#     sum_val = a + b;
#     prod_val = a * b;
# end
# [s, p] = calc(3, 4);

# Python: 튜플로 반환
def calc(a, b):
    sum_val = a + b
    prod_val = a * b
    return sum_val, prod_val  # 튜플 반환

s, p = calc(3, 4)
print(f"\ncalc(3, 4): sum={s}, product={p}")


# ============================================
# 10. 플로팅 (Matplotlib)
# ============================================
print("\n=== 10. 플로팅 ===\n")

import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# MATLAB:
# figure;
# plot(x, y);
# xlabel('x');
# ylabel('sin(x)');
# title('Sine Wave');
# grid on;

# Python:
plt.figure(figsize=(8, 4))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Wave')
plt.grid(True)
plt.savefig('/home/user/matlab/sine_wave.png')
plt.close()

print("플롯 저장: sine_wave.png")

# 여러 그래프
# MATLAB:
# figure;
# subplot(2, 1, 1);
# plot(x, sin(x));
# subplot(2, 1, 2);
# plot(x, cos(x));

# Python:
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
ax1.plot(x, np.sin(x))
ax1.set_ylabel('sin(x)')
ax1.grid(True)

ax2.plot(x, np.cos(x))
ax2.set_xlabel('x')
ax2.set_ylabel('cos(x)')
ax2.grid(True)

plt.tight_layout()
plt.savefig('/home/user/matlab/multi_plot.png')
plt.close()

print("다중 플롯 저장: multi_plot.png")


# ============================================
# 11. 파일 입출력
# ============================================
print("\n=== 11. 파일 입출력 ===\n")

# --- 텍스트 파일 ---
# MATLAB:
# data = [1, 2, 3; 4, 5, 6];
# save('data.txt', 'data', '-ascii');

# Python:
data = np.array([[1, 2, 3], [4, 5, 6]])
np.savetxt('/home/user/matlab/data.txt', data)
print("텍스트 파일 저장: data.txt")

# MATLAB: data = load('data.txt');
# Python:
loaded_data = np.loadtxt('/home/user/matlab/data.txt')
print(f"불러온 데이터:\n{loaded_data}")

# --- MAT 파일 (MATLAB 파일) ---
# Python에서 MATLAB 파일 읽기/쓰기
from scipy.io import savemat, loadmat

# 저장
matlab_data = {
    'matrix': np.array([[1, 2], [3, 4]]),
    'vector': np.array([1, 2, 3, 4, 5]),
    'scalar': 42
}
savemat('/home/user/matlab/python_data.mat', matlab_data)
print("\nMAT 파일 저장: python_data.mat")

# 불러오기
loaded_mat = loadmat('/home/user/matlab/python_data.mat')
print(f"MAT 파일에서 불러온 matrix:\n{loaded_mat['matrix']}")

# --- CSV 파일 ---
# MATLAB: csvwrite('data.csv', data);
# Python: np.savetxt('data.csv', data, delimiter=',')

# MATLAB: data = csvread('data.csv');
# Python: data = np.loadtxt('data.csv', delimiter=',')


# ============================================
# 12. 논리 연산
# ============================================
print("\n=== 12. 논리 연산 ===\n")

a = np.array([1, 2, 3, 4, 5])

# MATLAB: b = a > 2;
# Python: b = a > 2
b = a > 2
print(f"a > 2 = {b}")

# MATLAB: c = a(a > 2);  (논리 인덱싱)
# Python: c = a[a > 2]
c = a[a > 2]
print(f"a[a > 2] = {c}")

# 논리 연산자
# MATLAB          Python
# &&              and
# ||              or
# ~               not
# &               &  (배열)
# |               |  (배열)

x = 5
# MATLAB: if x > 3 && x < 10
# Python: if x > 3 and x < 10
if x > 3 and x < 10:
    print(f"{x}는 3과 10 사이입니다")

# 배열 논리 연산
arr = np.array([1, 2, 3, 4, 5])
# MATLAB: mask = (arr > 2) & (arr < 5);
# Python: mask = (arr > 2) & (arr < 5)
mask = (arr > 2) & (arr < 5)
print(f"\n(arr > 2) & (arr < 5) = {mask}")
print(f"arr[mask] = {arr[mask]}")


# ============================================
# 13. 셀 배열 vs 리스트
# ============================================
print("\n=== 13. 셀 배열 vs 리스트 ===\n")

# MATLAB: 셀 배열
# data = {1, 'hello', [1,2,3]};
# data{1}    -> 1
# data{2}    -> 'hello'

# Python: 리스트
data = [1, 'hello', [1, 2, 3]]
print(f"data[0] = {data[0]}")
print(f"data[1] = {data[1]}")
print(f"data[2] = {data[2]}")


# ============================================
# 14. 구조체 vs 딕셔너리
# ============================================
print("\n=== 14. 구조체 vs 딕셔너리 ===\n")

# MATLAB: 구조체
# person.name = 'John';
# person.age = 30;
# person.scores = [85, 90, 92];

# Python: 딕셔너리
person = {
    'name': 'John',
    'age': 30,
    'scores': [85, 90, 92]
}

print(f"이름: {person['name']}")
print(f"나이: {person['age']}")
print(f"점수: {person['scores']}")


# ============================================
# 15. 크기 관련 함수
# ============================================
print("\n=== 15. 크기 관련 함수 ===\n")

matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

# MATLAB          Python
# size(matrix)    matrix.shape
# length(vec)     len(vec)
# numel(matrix)   matrix.size

print(f"shape (MATLAB의 size): {matrix.shape}")
print(f"size (MATLAB의 numel): {matrix.size}")

vec = np.array([1, 2, 3, 4, 5])
print(f"length: {len(vec)}")


# ============================================
# 16. 행렬 조작
# ============================================
print("\n=== 16. 행렬 조작 ===\n")

A = np.array([[1, 2, 3],
              [4, 5, 6]])

# MATLAB: B = A';  (전치)
# Python: B = A.T
B = A.T
print(f"전치 (A.T):\n{B}")

# MATLAB: C = reshape(A, 3, 2);
# Python: C = A.reshape(3, 2)
C = A.reshape(3, 2)
print(f"\nreshape(3, 2):\n{C}")

# MATLAB: D = A(:);  (벡터로 펼치기)
# Python: D = A.flatten()
D = A.flatten()
print(f"\nflatten: {D}")

# 행렬 결합
# MATLAB: E = [A; A];  (세로로 결합)
# Python: E = np.vstack([A, A])
E = np.vstack([A, A])
print(f"\nvstack (세로 결합):\n{E}")

# MATLAB: F = [A, A];  (가로로 결합)
# Python: F = np.hstack([A, A])
F = np.hstack([A, A])
print(f"\nhstack (가로 결합):\n{F}")


# ============================================
# 17. 선형 대수
# ============================================
print("\n=== 17. 선형 대수 ===\n")

A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])

# MATLAB: x = A \ b;  (선형 방정식 풀이)
# Python: x = np.linalg.solve(A, b)
x = np.linalg.solve(A, b)
print(f"연립방정식 해: {x}")

# MATLAB: inv_A = inv(A);  (역행렬)
# Python: inv_A = np.linalg.inv(A)
inv_A = np.linalg.inv(A)
print(f"\n역행렬:\n{inv_A}")

# MATLAB: d = det(A);  (행렬식)
# Python: d = np.linalg.det(A)
d = np.linalg.det(A)
print(f"\n행렬식: {d}")

# MATLAB: [V, D] = eig(A);  (고유값, 고유벡터)
# Python: eigenvalues, eigenvectors = np.linalg.eig(A)
eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"\n고유값: {eigenvalues}")
print(f"고유벡터:\n{eigenvectors}")


# ============================================
# 18. 실무 예제: 데이터 분석
# ============================================
print("\n=== 18. 실무 예제: 데이터 분석 ===\n")

# 시뮬레이션 데이터 생성
time = np.linspace(0, 10, 100)
signal = np.sin(2*np.pi*0.5*time) + 0.2*np.random.randn(100)

# 통계 분석
print(f"평균: {np.mean(signal):.4f}")
print(f"표준편차: {np.std(signal):.4f}")
print(f"최대값: {np.max(signal):.4f}")
print(f"최소값: {np.min(signal):.4f}")

# 특정 조건 데이터 추출
# MATLAB: positive = signal(signal > 0);
positive = signal[signal > 0]
print(f"\n양수 데이터 개수: {len(positive)}")

# 이동 평균 (Moving average)
window_size = 5
# MATLAB: smoothed = movmean(signal, window_size);
# Python: NumPy로 구현
smoothed = np.convolve(signal, np.ones(window_size)/window_size, mode='same')

# 플롯
plt.figure(figsize=(10, 4))
plt.plot(time, signal, 'b-', alpha=0.5, label='Original')
plt.plot(time, smoothed, 'r-', linewidth=2, label='Smoothed')
plt.xlabel('Time')
plt.ylabel('Signal')
plt.title('Signal Smoothing')
plt.legend()
plt.grid(True)
plt.savefig('/home/user/matlab/signal_analysis.png')
plt.close()

print("신호 분석 플롯 저장: signal_analysis.png")


# ============================================
# 요약 및 주요 차이점
# ============================================
print("\n" + "="*60)
print("주요 차이점 요약")
print("="*60)

summary = """
1. 인덱싱:
   MATLAB: 1부터 시작, arr(1), arr(end)
   Python: 0부터 시작, arr[0], arr[-1]

2. 슬라이싱:
   MATLAB: arr(2:5)  -> 2,3,4,5 포함
   Python: arr[1:5]  -> 1,2,3,4 (5 제외!)

3. 배열 연산:
   MATLAB: .* ./ .^  (점 연산자 필요)
   Python: * / **    (NumPy는 기본이 원소별)

4. 행렬 곱셈:
   MATLAB: A * B     (행렬 곱)
   Python: A @ B     (행렬 곱), A * B (원소별)

5. 반복문:
   MATLAB: for i = 1:10 ... end
   Python: for i in range(1, 11): ...

6. 조건문:
   MATLAB: elseif
   Python: elif

7. 함수:
   MATLAB: function 키워드 필요
   Python: def 키워드 사용

8. 논리 연산:
   MATLAB: && || ~
   Python: and or not (스칼라), & | ~ (배열)

9. 출력:
   MATLAB: disp(), fprintf()
   Python: print()

10. 패키지:
    MATLAB: 기본 제공
    Python: import numpy, matplotlib 필요
"""

print(summary)

print("\n필수 Python 패키지:")
print("  - NumPy: 배열/행렬 연산 (MATLAB 핵심 기능)")
print("  - Matplotlib: 플로팅 (MATLAB의 plot)")
print("  - SciPy: 과학 계산 (MATLAB 툴박스와 유사)")
print("  - Pandas: 데이터 분석 (테이블 데이터)")

print("\n설치 명령어:")
print("  pip install numpy matplotlib scipy pandas")
