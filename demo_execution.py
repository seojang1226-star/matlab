"""
Claude Code 실행 및 시각화 데모
"""

# ============================================
# 1. 기본 Python 코드 실행
# ============================================
print("=== Claude Code에서 코드 실행 ===\n")

# 간단한 계산
a = 10
b = 20
result = a + b
print(f"{a} + {b} = {result}")

# 반복문
print("\n구구단 3단:")
for i in range(1, 10):
    print(f"3 × {i} = {3 * i}")

# 함수 정의 및 실행
def fibonacci(n):
    """피보나치 수열 생성"""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

fib_sequence = fibonacci(10)
print(f"\n피보나치 수열 (10개): {fib_sequence}")


# ============================================
# 2. 데이터 처리 및 분석
# ============================================
print("\n=== 데이터 분석 예제 ===\n")

# 수동으로 데이터 생성 (NumPy 없이)
temperatures = [22.5, 23.1, 21.8, 24.2, 25.0, 23.8, 22.9, 23.5]
print(f"온도 데이터: {temperatures}")

# 평균 계산
avg_temp = sum(temperatures) / len(temperatures)
print(f"평균 온도: {avg_temp:.2f}°C")

# 최대/최소
max_temp = max(temperatures)
min_temp = min(temperatures)
print(f"최고 온도: {max_temp}°C")
print(f"최저 온도: {min_temp}°C")

# 필터링 (23도 이상)
high_temps = [t for t in temperatures if t >= 23.0]
print(f"23도 이상인 온도: {high_temps}")


# ============================================
# 3. ASCII 그래프 생성 (간단한 시각화)
# ============================================
print("\n=== ASCII 그래프 ===\n")

data = [5, 12, 8, 15, 20, 18, 10, 7]
max_val = max(data)

print("온도 변화 (막대 그래프):")
for i, val in enumerate(data):
    bar = '█' * int((val / max_val) * 30)
    print(f"Day {i+1}: {bar} {val}°C")


# ============================================
# 4. 파일 생성 및 읽기
# ============================================
print("\n=== 파일 입출력 ===\n")

# CSV 파일 생성
csv_content = """Time,Temperature,Humidity
08:00,22.5,65
09:00,23.1,63
10:00,24.2,60
11:00,25.0,58
12:00,25.5,57
"""

with open('/home/user/matlab/demo_data.csv', 'w') as f:
    f.write(csv_content)
print("CSV 파일 생성: demo_data.csv")

# CSV 파일 읽기
print("\n파일 내용:")
with open('/home/user/matlab/demo_data.csv', 'r') as f:
    content = f.read()
    print(content)


# ============================================
# 5. 간단한 HTML 리포트 생성
# ============================================
print("\n=== HTML 리포트 생성 ===\n")

html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>데이터 분석 결과</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        h1 {{ color: #333; }}
        .result {{ background: #f0f0f0; padding: 15px; border-radius: 5px; }}
        table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #4CAF50; color: white; }}
    </style>
</head>
<body>
    <h1>온도 데이터 분석 결과</h1>

    <div class="result">
        <h2>통계 요약</h2>
        <ul>
            <li>평균 온도: {avg_temp:.2f}°C</li>
            <li>최고 온도: {max_temp}°C</li>
            <li>최저 온도: {min_temp}°C</li>
            <li>데이터 개수: {len(temperatures)}개</li>
        </ul>
    </div>

    <h2>온도 데이터</h2>
    <table>
        <tr>
            <th>시간</th>
            <th>온도 (°C)</th>
            <th>상태</th>
        </tr>
"""

for i, temp in enumerate(temperatures):
    status = "높음" if temp >= 24 else "보통" if temp >= 22 else "낮음"
    html_content += f"""        <tr>
            <td>{i+1}시간</td>
            <td>{temp}</td>
            <td>{status}</td>
        </tr>
"""

html_content += """    </table>
</body>
</html>
"""

with open('/home/user/matlab/report.html', 'w') as f:
    f.write(html_content)

print("HTML 리포트 생성: report.html")
print("브라우저로 열어서 확인할 수 있습니다!")


# ============================================
# 완료
# ============================================
print("\n" + "="*50)
print("모든 작업 완료!")
print("="*50)
print("\n생성된 파일:")
print("  - demo_data.csv")
print("  - report.html")
