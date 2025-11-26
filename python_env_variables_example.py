"""
Python에서 시스템 환경변수 접근 예제
ANSYS 설치 경로를 찾는 방법
"""

import os
import sys
from pathlib import Path

# ============================================
# 1. 기본 환경변수 접근
# ============================================
print("=== 1. 환경변수 기본 접근 ===")

# 환경변수 가져오기 - os.environ
# 형식: os.environ['변수명'] 또는 os.environ.get('변수명')

# 방법 1: 직접 접근 (변수가 없으면 KeyError 발생)
try:
    home_dir = os.environ['HOME']
    print(f"HOME: {home_dir}")
except KeyError:
    print("HOME 환경변수가 없습니다.")

# 방법 2: get() 사용 (권장 - 변수가 없으면 None 반환)
user = os.environ.get('USER')
print(f"USER: {user}")

# 방법 3: get()에 기본값 지정
lang = os.environ.get('LANG', 'en_US.UTF-8')  # 없으면 기본값 반환
print(f"LANG: {lang}")


# ============================================
# 2. ANSYS 경로 찾기
# ============================================
print("\n=== 2. ANSYS 설치 경로 찾기 ===")

# ANSYS 관련 주요 환경변수들
ansys_env_vars = [
    'AWP_ROOT242',      # ANSYS 2024 R2
    'AWP_ROOT241',      # ANSYS 2024 R1
    'AWP_ROOT232',      # ANSYS 2023 R2
    'AWP_ROOT231',      # ANSYS 2023 R1
    'ANSYS_ROOT',       # 일반적인 ANSYS 루트
    'FLUENT_ROOT',      # Fluent 전용
    'ANSYSLMD_LICENSE_FILE',  # 라이센스 서버
]

print("설치된 ANSYS 버전:")
for var in ansys_env_vars:
    value = os.environ.get(var)
    if value:
        print(f"  {var}: {value}")
    else:
        print(f"  {var}: (설정 안됨)")


# ============================================
# 3. ANSYS 경로 찾기 함수
# ============================================
print("\n=== 3. ANSYS 경로 자동 탐색 ===")

def find_ansys_installation():
    """
    ANSYS 설치 경로를 찾는 함수

    반환값:
        dict: {'version': 버전, 'path': 경로}
    """

    # 1. 환경변수에서 찾기
    for var in os.environ:
        if var.startswith('AWP_ROOT'):
            version = var.replace('AWP_ROOT', '20')  # AWP_ROOT242 -> 20242
            version = f"{version[:4]} R{version[4]}"  # 2024 R2
            return {
                'version': version,
                'path': os.environ[var],
                'source': 'environment variable'
            }

    # 2. 일반적인 설치 경로에서 찾기 (Linux)
    common_paths_linux = [
        '/usr/ansys_inc',
        '/opt/ansys_inc',
        '/ansys_inc',
    ]

    # 3. 일반적인 설치 경로에서 찾기 (Windows)
    common_paths_windows = [
        'C:/Program Files/ANSYS Inc',
        'C:/ANSYS Inc',
    ]

    paths = common_paths_linux if sys.platform.startswith('linux') else common_paths_windows

    for base_path in paths:
        if os.path.exists(base_path):
            # 버전 폴더 찾기 (v232, v241 등)
            try:
                versions = [d for d in os.listdir(base_path) if d.startswith('v')]
                if versions:
                    latest = sorted(versions)[-1]  # 최신 버전
                    full_path = os.path.join(base_path, latest)
                    return {
                        'version': latest,
                        'path': full_path,
                        'source': 'common installation path'
                    }
            except PermissionError:
                continue

    return None

# ANSYS 경로 찾기 실행
ansys_info = find_ansys_installation()

if ansys_info:
    print(f"ANSYS 발견!")
    print(f"  버전: {ansys_info['version']}")
    print(f"  경로: {ansys_info['path']}")
    print(f"  출처: {ansys_info['source']}")
else:
    print("ANSYS 설치를 찾을 수 없습니다.")


# ============================================
# 4. Fluent 실행 파일 경로 찾기
# ============================================
print("\n=== 4. Fluent 실행 파일 경로 ===")

def find_fluent_executable(ansys_root):
    """
    Fluent 실행 파일 찾기

    매개변수:
        ansys_root: ANSYS 설치 루트 경로

    반환값:
        str: Fluent 실행 파일 전체 경로
    """
    if not ansys_root or not os.path.exists(ansys_root):
        return None

    # Linux
    fluent_path_linux = os.path.join(ansys_root, 'fluent', 'bin', 'fluent')
    # Windows
    fluent_path_windows = os.path.join(ansys_root, 'fluent', 'ntbin', 'win64', 'fluent.exe')

    fluent_path = fluent_path_linux if sys.platform.startswith('linux') else fluent_path_windows

    if os.path.exists(fluent_path):
        return fluent_path
    else:
        return None

if ansys_info:
    fluent_exe = find_fluent_executable(ansys_info['path'])
    if fluent_exe:
        print(f"Fluent 실행 파일: {fluent_exe}")
    else:
        print("Fluent 실행 파일을 찾을 수 없습니다.")


# ============================================
# 5. 환경변수 설정하기
# ============================================
print("\n=== 5. 환경변수 설정 (현재 세션만) ===")

# Python 스크립트 내에서 환경변수 설정
# 주의: 현재 Python 프로세스와 하위 프로세스에만 적용됨

# 설정
os.environ['MY_ANSYS_PATH'] = '/path/to/ansys'
os.environ['FLUENT_CORES'] = '4'

# 확인
print(f"MY_ANSYS_PATH: {os.environ.get('MY_ANSYS_PATH')}")
print(f"FLUENT_CORES: {os.environ.get('FLUENT_CORES')}")


# ============================================
# 6. 모든 환경변수 출력
# ============================================
print("\n=== 6. 모든 환경변수 보기 (ANSYS 관련만) ===")

print("ANSYS/FLUENT 관련 환경변수:")
for key, value in sorted(os.environ.items()):
    if any(keyword in key.upper() for keyword in ['ANSYS', 'FLUENT', 'AWP']):
        print(f"  {key} = {value}")


# ============================================
# 7. 실전 예제: PyFluent에서 사용
# ============================================
print("\n=== 7. PyFluent와 연동 ===")

def setup_fluent_environment():
    """
    PyFluent 실행을 위한 환경 설정
    """
    # ANSYS 경로 찾기
    ansys_info = find_ansys_installation()

    if not ansys_info:
        print("오류: ANSYS 설치를 찾을 수 없습니다.")
        print("\n수동 설정 방법:")
        print("  export AWP_ROOT242=/path/to/ansys_inc/v242")
        return False

    # 필요한 환경변수 설정
    ansys_root = ansys_info['path']
    os.environ['AWP_ROOT'] = ansys_root

    # Fluent 경로 설정
    fluent_root = os.path.join(ansys_root, 'fluent')
    if os.path.exists(fluent_root):
        os.environ['FLUENT_ROOT'] = fluent_root
        print(f"Fluent 환경 설정 완료: {fluent_root}")
        return True
    else:
        print(f"오류: Fluent를 찾을 수 없습니다: {fluent_root}")
        return False

# 환경 설정 실행
if setup_fluent_environment():
    print("\nPyFluent 실행 준비 완료!")
    print("\n다음 코드로 Fluent를 실행할 수 있습니다:")
    print("  import ansys.fluent.core as pyfluent")
    print("  solver = pyfluent.launch_fluent(...)")


# ============================================
# 8. 환경변수 파일 읽기 (.env 파일)
# ============================================
print("\n=== 8. .env 파일에서 환경변수 읽기 ===")

def load_env_file(env_file='.env'):
    """
    .env 파일에서 환경변수 읽어오기

    .env 파일 형식:
        AWP_ROOT242=/usr/ansys_inc/v242
        FLUENT_CORES=4
    """
    if not os.path.exists(env_file):
        print(f".env 파일을 찾을 수 없습니다: {env_file}")
        return

    with open(env_file, 'r') as f:
        for line in f:
            line = line.strip()
            # 주석이나 빈 줄 무시
            if not line or line.startswith('#'):
                continue

            # KEY=VALUE 파싱
            if '=' in line:
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()
                print(f"  {key.strip()} = {value.strip()}")

print(".env 파일 형식 예시:")
print("  AWP_ROOT242=/usr/ansys_inc/v242")
print("  ANSYSLMD_LICENSE_FILE=1055@license-server")
print("  FLUENT_CORES=4")

# 실제 .env 파일이 있으면 읽기
if os.path.exists('.env'):
    print("\n.env 파일 읽기:")
    load_env_file('.env')
else:
    print("\n.env 파일이 없습니다.")


# ============================================
# 참고 사항
# ============================================
print("\n=== 참고 사항 ===")
print("""
주요 환경변수:

ANSYS 관련:
  AWP_ROOT242       : ANSYS 2024 R2 설치 경로
  AWP_ROOT241       : ANSYS 2024 R1 설치 경로
  ANSYSLMD_LICENSE_FILE : 라이센스 서버 (예: 1055@server)

Fluent 관련:
  FLUENT_ROOT       : Fluent 설치 경로
  FLUENT_ARCH       : 아키텍처 (lnamd64, ntx86 등)

시스템 정보:
  HOME              : 사용자 홈 디렉토리
  USER              : 사용자 이름
  PATH              : 실행 파일 검색 경로

환경변수 설정 방법:

Linux/Mac:
  export AWP_ROOT242=/usr/ansys_inc/v242

  영구 설정 (~/.bashrc 또는 ~/.zshrc에 추가):
  echo 'export AWP_ROOT242=/usr/ansys_inc/v242' >> ~/.bashrc
  source ~/.bashrc

Windows (PowerShell):
  $env:AWP_ROOT242 = "C:\\Program Files\\ANSYS Inc\\v242"

  영구 설정:
  [Environment]::SetEnvironmentVariable("AWP_ROOT242", "C:\\Program Files\\ANSYS Inc\\v242", "User")

Windows (CMD):
  set AWP_ROOT242=C:\\Program Files\\ANSYS Inc\\v242

  영구 설정:
  setx AWP_ROOT242 "C:\\Program Files\\ANSYS Inc\\v242"
""")