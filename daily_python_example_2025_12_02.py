#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Daily Python Example - 2025-12-02
데일리 데이터 분석 및 처리 예제

이 예제는 다음 기능을 포함합니다:
1. 파일 읽기/쓰기
2. 데이터 필터링 및 통계 계산
3. 클래스와 함수 활용
4. 실용적인 로깅 기능
"""

from datetime import datetime
from typing import List, Dict
import json


class DataAnalyzer:
    """간단한 데이터 분석 클래스"""

    def __init__(self, name: str):
        self.name = name
        self.data: List[float] = []
        self.created_at = datetime.now()

    def add_data(self, values: List[float]) -> None:
        """데이터 추가"""
        self.data.extend(values)
        print(f"✓ {len(values)}개 데이터 추가됨 (총 {len(self.data)}개)")

    def calculate_statistics(self) -> Dict[str, float]:
        """기본 통계량 계산"""
        if not self.data:
            return {"error": "데이터가 없습니다"}

        sorted_data = sorted(self.data)
        n = len(sorted_data)

        stats = {
            "평균": sum(self.data) / n,
            "최솟값": min(self.data),
            "최댓값": max(self.data),
            "중앙값": sorted_data[n // 2] if n % 2 != 0
                     else (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2,
            "데이터 개수": n
        }

        # 표준편차 계산
        mean = stats["평균"]
        variance = sum((x - mean) ** 2 for x in self.data) / n
        stats["표준편차"] = variance ** 0.5

        return stats

    def filter_data(self, min_val: float = None, max_val: float = None) -> List[float]:
        """데이터 필터링"""
        filtered = self.data.copy()

        if min_val is not None:
            filtered = [x for x in filtered if x >= min_val]

        if max_val is not None:
            filtered = [x for x in filtered if x <= max_val]

        return filtered

    def save_report(self, filename: str) -> None:
        """분석 결과를 JSON 파일로 저장"""
        stats = self.calculate_statistics()

        report = {
            "분석자": self.name,
            "생성 시간": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "통계": stats,
            "원본 데이터": self.data[:10]  # 처음 10개만 저장
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)

        print(f"✓ 보고서가 '{filename}'에 저장되었습니다")


def demonstrate_file_operations():
    """파일 입출력 예제"""
    print("\n=== 파일 입출력 예제 ===")

    # 텍스트 파일 쓰기
    with open('sample_data.txt', 'w', encoding='utf-8') as f:
        f.write("10.5\n20.3\n15.7\n30.2\n25.8\n")

    print("✓ 샘플 데이터 파일 생성")

    # 텍스트 파일 읽기
    numbers = []
    with open('sample_data.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(float(line.strip()))

    print(f"✓ 파일에서 {len(numbers)}개 숫자 읽음: {numbers}")

    return numbers


def demonstrate_list_comprehension():
    """리스트 컴프리헨션 예제"""
    print("\n=== 리스트 컴프리헨션 예제 ===")

    # 1부터 20까지의 짝수
    even_numbers = [x for x in range(1, 21) if x % 2 == 0]
    print(f"짝수: {even_numbers}")

    # 제곱수
    squares = [x**2 for x in range(1, 11)]
    print(f"제곱수: {squares}")

    # 딕셔너리 컴프리헨션
    square_dict = {x: x**2 for x in range(1, 6)}
    print(f"제곱 딕셔너리: {square_dict}")

    return even_numbers, squares


def demonstrate_string_formatting():
    """문자열 포매팅 예제"""
    print("\n=== 문자열 포매팅 예제 ===")

    name = "Python"
    version = 3.12
    today = datetime.now()

    # f-string (권장)
    print(f"언어: {name}, 버전: {version:.1f}")

    # 날짜 포매팅
    print(f"오늘 날짜: {today:%Y년 %m월 %d일}")

    # 숫자 포매팅
    pi = 3.14159265359
    print(f"원주율: {pi:.2f} (소수점 2자리)")
    print(f"원주율: {pi:.4f} (소수점 4자리)")


def main():
    """메인 실행 함수"""
    print("=" * 50)
    print("Daily Python Example - 2025-12-02")
    print("=" * 50)

    # 1. 파일 입출력 데모
    file_data = demonstrate_file_operations()

    # 2. 데이터 분석 클래스 사용
    print("\n=== 데이터 분석 예제 ===")
    analyzer = DataAnalyzer("Daily Analyzer")

    # 샘플 데이터 추가
    sample_data = [15.2, 23.5, 18.7, 30.1, 12.8, 25.4, 19.9, 28.3]
    analyzer.add_data(sample_data)
    analyzer.add_data(file_data)

    # 통계 계산
    stats = analyzer.calculate_statistics()
    print("\n📊 통계 결과:")
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.2f}")
        else:
            print(f"  {key}: {value}")

    # 데이터 필터링
    filtered = analyzer.filter_data(min_val=20.0)
    print(f"\n✓ 20 이상 값들: {filtered}")

    # 보고서 저장
    analyzer.save_report('daily_analysis_report.json')

    # 3. 리스트 컴프리헨션
    demonstrate_list_comprehension()

    # 4. 문자열 포매팅
    demonstrate_string_formatting()

    print("\n" + "=" * 50)
    print("예제 실행 완료! ✓")
    print("=" * 50)


if __name__ == "__main__":
    main()
