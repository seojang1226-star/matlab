"""
Python 기초 학습 예제
이 파일은 Python을 처음 시작하는 분들을 위한 기본 개념과 예제를 포함합니다.
"""

# ============================================
# 1. 기본 출력과 주석
# ============================================
print("=== 1. 기본 출력 ===")
print("Hello, Python!")  # 한 줄 주석은 # 으로 시작합니다
print("여러 개의 값:", 1, 2, 3)


# ============================================
# 2. 변수와 데이터 타입
# ============================================
print("\n=== 2. 변수와 데이터 타입 ===")

# 정수 (Integer)
age = 25
print(f"나이: {age}, 타입: {type(age)}")

# 실수 (Float)
height = 175.5
print(f"키: {height}cm, 타입: {type(height)}")

# 문자열 (String)
name = "홍길동"
print(f"이름: {name}, 타입: {type(name)}")

# 불리언 (Boolean)
is_student = True
print(f"학생 여부: {is_student}, 타입: {type(is_student)}")


# ============================================
# 3. 리스트 (List) - 순서가 있는 데이터 모음
# ============================================
print("\n=== 3. 리스트 ===")

fruits = ["사과", "바나나", "오렌지", "포도"]
print(f"과일 리스트: {fruits}")
print(f"첫 번째 과일: {fruits[0]}")
print(f"마지막 과일: {fruits[-1]}")

# 리스트에 항목 추가
fruits.append("딸기")
print(f"추가 후: {fruits}")

# 리스트 길이
print(f"과일 개수: {len(fruits)}")


# ============================================
# 4. 딕셔너리 (Dictionary) - 키-값 쌍으로 데이터 저장
# ============================================
print("\n=== 4. 딕셔너리 ===")

person = {
    "이름": "김철수",
    "나이": 30,
    "직업": "개발자",
    "취미": ["독서", "운동", "코딩"]
}

print(f"사람 정보: {person}")
print(f"이름: {person['이름']}")
print(f"나이: {person['나이']}")
print(f"취미: {person['취미']}")


# ============================================
# 5. 조건문 (if, elif, else)
# ============================================
print("\n=== 5. 조건문 ===")

score = 85

if score >= 90:
    grade = "A"
    print(f"점수 {score}점 - 등급: {grade}")
elif score >= 80:
    grade = "B"
    print(f"점수 {score}점 - 등급: {grade}")
elif score >= 70:
    grade = "C"
    print(f"점수 {score}점 - 등급: {grade}")
else:
    grade = "D"
    print(f"점수 {score}점 - 등급: {grade}")


# ============================================
# 6. 반복문 (for, while)
# ============================================
print("\n=== 6. 반복문 ===")

# for 반복문 - 리스트 순회
print("for 반복문:")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"  숫자: {num}, 제곱: {num ** 2}")

# for 반복문 - range 사용
print("\nrange를 사용한 반복:")
for i in range(3):
    print(f"  반복 {i + 1}회")

# while 반복문
print("\nwhile 반복문:")
count = 0
while count < 3:
    print(f"  카운트: {count}")
    count += 1


# ============================================
# 7. 함수 정의와 사용
# ============================================
print("\n=== 7. 함수 ===")

# 기본 함수
def greet(name):
    """이름을 받아서 인사하는 함수"""
    return f"안녕하세요, {name}님!"

message = greet("파이썬")
print(message)


# 여러 매개변수를 받는 함수
def add_numbers(a, b):
    """두 숫자를 더하는 함수"""
    result = a + b
    return result

sum_result = add_numbers(10, 20)
print(f"10 + 20 = {sum_result}")


# 기본값이 있는 함수
def introduce(name, age=25):
    """이름과 나이를 소개하는 함수 (나이는 기본값 25)"""
    return f"제 이름은 {name}이고, 나이는 {age}살입니다."

print(introduce("김영희"))
print(introduce("박민수", 30))


# ============================================
# 8. 실전 예제: 간단한 계산기 함수
# ============================================
print("\n=== 8. 실전 예제: 계산기 ===")

def calculator(num1, num2, operation):
    """
    간단한 계산기 함수

    매개변수:
        num1: 첫 번째 숫자
        num2: 두 번째 숫자
        operation: 연산자 ('+', '-', '*', '/')

    반환값:
        계산 결과
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "0으로 나눌 수 없습니다!"
    else:
        return "잘못된 연산자입니다!"

print(f"15 + 5 = {calculator(15, 5, '+')}")
print(f"15 - 5 = {calculator(15, 5, '-')}")
print(f"15 * 5 = {calculator(15, 5, '*')}")
print(f"15 / 5 = {calculator(15, 5, '/')}")


# ============================================
# 9. 리스트 컴프리헨션 (고급)
# ============================================
print("\n=== 9. 리스트 컴프리헨션 ===")

# 1부터 10까지의 제곱수 리스트
squares = [x ** 2 for x in range(1, 11)]
print(f"1~10의 제곱수: {squares}")

# 짝수만 필터링
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(f"1~20의 짝수: {even_numbers}")


# ============================================
# 10. 문자열 다루기
# ============================================
print("\n=== 10. 문자열 다루기 ===")

text = "Python Programming"

print(f"원본: {text}")
print(f"소문자: {text.lower()}")
print(f"대문자: {text.upper()}")
print(f"단어 분리: {text.split()}")
print(f"길이: {len(text)}")
print(f"'Python' 포함 여부: {'Python' in text}")


# ============================================
# 실습 문제
# ============================================
print("\n=== 실습 문제 ===")
print("""
이제 직접 해보세요!

1. 자신의 이름, 나이, 취미를 변수로 만들어보세요.
2. 1부터 100까지의 숫자 중 3의 배수만 출력하는 코드를 작성해보세요.
3. 섭씨 온도를 화씨로 변환하는 함수를 만들어보세요.
   공식: 화씨 = (섭씨 × 9/5) + 32
4. 리스트 [10, 20, 30, 40, 50]의 평균을 구하는 코드를 작성해보세요.
""")