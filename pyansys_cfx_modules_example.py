"""
PyAnsys를 사용한 CFX 모듈 실행 예제

이 스크립트는 다음 ANSYS CFX 모듈들을 실행하는 방법을 보여줍니다:
1. TurboGrid - 터보 기계용 격자 생성
2. CFX-Pre - CFX 전처리 (경계 조건 설정)
3. CFD Solver Manager - CFX 솔버 실행
4. CFD-Post - 후처리 및 결과 시각화

사전 요구사항:
    - ANSYS CFX 설치 필요
    - 환경 변수 AWP_ROOT 또는 ANSYS_ROOT 설정

설치:
    pip install ansys-tools-path
    pip install ansys-platform-instancemanagement
"""

import os
import subprocess
import sys
from pathlib import Path

# ============================================
# 0. ANSYS 설치 경로 찾기
# ============================================
def find_ansys_installation():
    """ANSYS 설치 경로를 찾습니다."""
    print("=== ANSYS 설치 경로 검색 ===")

    # 환경 변수에서 찾기
    awp_root = os.getenv('AWP_ROOT')
    ansys_root = os.getenv('ANSYS_ROOT')

    if awp_root:
        print(f"AWP_ROOT 발견: {awp_root}")
        return awp_root
    elif ansys_root:
        print(f"ANSYS_ROOT 발견: {ansys_root}")
        return ansys_root

    # 일반적인 설치 경로에서 찾기
    common_paths = [
        "/usr/ansys_inc",
        "/opt/ansys_inc",
        "C:\\Program Files\\ANSYS Inc",
        "C:\\Program Files (x86)\\ANSYS Inc"
    ]

    for path in common_paths:
        if os.path.exists(path):
            # 최신 버전 찾기
            versions = sorted([d for d in os.listdir(path) if d.startswith('v')], reverse=True)
            if versions:
                ansys_path = os.path.join(path, versions[0])
                print(f"ANSYS 설치 발견: {ansys_path}")
                return ansys_path

    print("경고: ANSYS 설치를 찾을 수 없습니다.")
    print("AWP_ROOT 또는 ANSYS_ROOT 환경 변수를 설정하세요.")
    return None


def get_cfx_bin_path(ansys_root):
    """CFX 실행 파일 경로를 반환합니다."""
    if not ansys_root:
        return None

    # Linux/Unix
    cfx_bin = os.path.join(ansys_root, "CFX", "bin")
    if os.path.exists(cfx_bin):
        return cfx_bin

    # Windows
    cfx_bin = os.path.join(ansys_root, "CFX", "bin")
    if os.path.exists(cfx_bin):
        return cfx_bin

    return None


# ============================================
# 1. TurboGrid 실행
# ============================================
def launch_turbogrid(ansys_root, script_file=None, batch_mode=False):
    """
    TurboGrid를 실행합니다.

    Parameters:
    -----------
    ansys_root : str
        ANSYS 설치 루트 경로
    script_file : str, optional
        실행할 TurboGrid 스크립트 파일 (.tse)
    batch_mode : bool
        배치 모드로 실행 (GUI 없이)
    """
    print("\n=== TurboGrid 실행 ===")

    cfx_bin = get_cfx_bin_path(ansys_root)
    if not cfx_bin:
        print("오류: CFX 실행 파일을 찾을 수 없습니다.")
        return False

    # TurboGrid 실행 파일
    turbogrid_exe = os.path.join(cfx_bin, "cfxtg")

    if not os.path.exists(turbogrid_exe):
        print(f"오류: TurboGrid 실행 파일을 찾을 수 없습니다: {turbogrid_exe}")
        return False

    # 실행 명령 구성
    cmd = [turbogrid_exe]

    if batch_mode:
        cmd.append("-batch")

    if script_file:
        cmd.extend(["-script", script_file])

    print(f"실행 명령: {' '.join(cmd)}")

    try:
        if batch_mode and script_file:
            # 배치 모드로 실행 (스크립트 완료까지 대기)
            result = subprocess.run(cmd, capture_output=True, text=True)
            print("TurboGrid 실행 완료")
            print(f"반환 코드: {result.returncode}")
            if result.stdout:
                print(f"출력:\n{result.stdout}")
            return result.returncode == 0
        else:
            # GUI 모드로 실행 (백그라운드)
            process = subprocess.Popen(cmd)
            print(f"TurboGrid가 시작되었습니다 (PID: {process.pid})")
            print("GUI 모드로 실행 중...")
            return True
    except Exception as e:
        print(f"오류 발생: {e}")
        return False


# ============================================
# 2. CFX-Pre 실행
# ============================================
def launch_cfx_pre(ansys_root, def_file=None, script_file=None, batch_mode=False):
    """
    CFX-Pre를 실행합니다.

    Parameters:
    -----------
    ansys_root : str
        ANSYS 설치 루트 경로
    def_file : str, optional
        불러올 정의 파일 (.def)
    script_file : str, optional
        실행할 CCL 스크립트 파일
    batch_mode : bool
        배치 모드로 실행
    """
    print("\n=== CFX-Pre 실행 ===")

    cfx_bin = get_cfx_bin_path(ansys_root)
    if not cfx_bin:
        print("오류: CFX 실행 파일을 찾을 수 없습니다.")
        return False

    # CFX-Pre 실행 파일
    cfxpre_exe = os.path.join(cfx_bin, "cfx5pre")

    if not os.path.exists(cfxpre_exe):
        print(f"오류: CFX-Pre 실행 파일을 찾을 수 없습니다: {cfxpre_exe}")
        return False

    # 실행 명령 구성
    cmd = [cfxpre_exe]

    if batch_mode:
        cmd.append("-batch")

    if def_file:
        cmd.extend(["-def", def_file])

    if script_file:
        cmd.extend(["-ccl", script_file])

    print(f"실행 명령: {' '.join(cmd)}")

    try:
        if batch_mode:
            # 배치 모드로 실행
            result = subprocess.run(cmd, capture_output=True, text=True)
            print("CFX-Pre 실행 완료")
            print(f"반환 코드: {result.returncode}")
            if result.stdout:
                print(f"출력:\n{result.stdout}")
            return result.returncode == 0
        else:
            # GUI 모드로 실행
            process = subprocess.Popen(cmd)
            print(f"CFX-Pre가 시작되었습니다 (PID: {process.pid})")
            print("GUI 모드로 실행 중...")
            return True
    except Exception as e:
        print(f"오류 발생: {e}")
        return False


# ============================================
# 3. CFD Solver Manager 실행
# ============================================
def launch_solver_manager(ansys_root, def_file=None, par_local=None):
    """
    CFD Solver Manager를 통해 CFX 솔버를 실행합니다.

    Parameters:
    -----------
    ansys_root : str
        ANSYS 설치 루트 경로
    def_file : str, optional
        실행할 정의 파일 (.def)
    par_local : int, optional
        병렬 계산 코어 수
    """
    print("\n=== CFD Solver Manager 실행 ===")

    cfx_bin = get_cfx_bin_path(ansys_root)
    if not cfx_bin:
        print("오류: CFX 실행 파일을 찾을 수 없습니다.")
        return False

    # CFX Solver Manager 실행 파일
    solver_exe = os.path.join(cfx_bin, "cfx5solve")

    if not os.path.exists(solver_exe):
        print(f"오류: CFX Solver를 찾을 수 없습니다: {solver_exe}")
        return False

    if not def_file:
        print("주의: 정의 파일이 지정되지 않았습니다.")
        print("Solver Manager GUI를 실행합니다...")

        # Solver Manager GUI 실행
        solver_manager_exe = os.path.join(cfx_bin, "cfx5")
        if os.path.exists(solver_manager_exe):
            cmd = [solver_manager_exe]
            process = subprocess.Popen(cmd)
            print(f"Solver Manager가 시작되었습니다 (PID: {process.pid})")
            return True
        else:
            print("오류: Solver Manager를 찾을 수 없습니다.")
            return False

    # 솔버 실행 명령 구성
    cmd = [solver_exe, "-def", def_file]

    if par_local:
        cmd.extend(["-par-local", str(par_local)])

    # 출력 파일 지정
    output_dir = os.path.dirname(def_file) if def_file else "."
    cmd.extend(["-out", os.path.join(output_dir, "solver_output.out")])

    print(f"실행 명령: {' '.join(cmd)}")

    try:
        # 솔버 실행 (백그라운드)
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"CFX Solver가 시작되었습니다 (PID: {process.pid})")
        print(f"정의 파일: {def_file}")
        if par_local:
            print(f"병렬 계산 코어: {par_local}")
        print("솔버가 실행 중입니다...")

        # 실시간 출력 (선택사항)
        # for line in process.stdout:
        #     print(line, end='')

        return True
    except Exception as e:
        print(f"오류 발생: {e}")
        return False


# ============================================
# 4. CFD-Post 실행
# ============================================
def launch_cfd_post(ansys_root, res_file=None, script_file=None, batch_mode=False):
    """
    CFD-Post를 실행합니다.

    Parameters:
    -----------
    ansys_root : str
        ANSYS 설치 루트 경로
    res_file : str, optional
        불러올 결과 파일 (.res)
    script_file : str, optional
        실행할 세션 스크립트 파일 (.cse)
    batch_mode : bool
        배치 모드로 실행
    """
    print("\n=== CFD-Post 실행 ===")

    cfx_bin = get_cfx_bin_path(ansys_root)
    if not cfx_bin:
        print("오류: CFX 실행 파일을 찾을 수 없습니다.")
        return False

    # CFD-Post 실행 파일
    cfdpost_exe = os.path.join(cfx_bin, "cfdpost")

    if not os.path.exists(cfdpost_exe):
        print(f"오류: CFD-Post 실행 파일을 찾을 수 없습니다: {cfdpost_exe}")
        return False

    # 실행 명령 구성
    cmd = [cfdpost_exe]

    if batch_mode:
        cmd.append("-batch")

    if res_file:
        cmd.extend(["-res", res_file])

    if script_file:
        cmd.extend(["-script", script_file])

    print(f"실행 명령: {' '.join(cmd)}")

    try:
        if batch_mode and script_file:
            # 배치 모드로 실행
            result = subprocess.run(cmd, capture_output=True, text=True)
            print("CFD-Post 실행 완료")
            print(f"반환 코드: {result.returncode}")
            if result.stdout:
                print(f"출력:\n{result.stdout}")
            return result.returncode == 0
        else:
            # GUI 모드로 실행
            process = subprocess.Popen(cmd)
            print(f"CFD-Post가 시작되었습니다 (PID: {process.pid})")
            print("GUI 모드로 실행 중...")
            return True
    except Exception as e:
        print(f"오류 발생: {e}")
        return False


# ============================================
# 5. 종합 워크플로우 예제
# ============================================
def run_complete_workflow(ansys_root):
    """
    완전한 CFX 워크플로우를 실행하는 예제입니다.
    (실제 파일 경로는 사용자 환경에 맞게 수정 필요)
    """
    print("\n" + "="*60)
    print("완전한 CFX 워크플로우 예제")
    print("="*60)

    # 작업 디렉토리
    work_dir = "/home/user/matlab/cfx_workflow"
    os.makedirs(work_dir, exist_ok=True)

    print(f"\n작업 디렉토리: {work_dir}")

    # 1. TurboGrid로 격자 생성 (예제)
    print("\n[1/4] TurboGrid로 격자 생성")
    turbogrid_script = os.path.join(work_dir, "turbogrid_script.tse")
    # launch_turbogrid(ansys_root, script_file=turbogrid_script, batch_mode=True)
    print("    -> 스킵 (예제 스크립트 파일 없음)")

    # 2. CFX-Pre로 전처리 (예제)
    print("\n[2/4] CFX-Pre로 케이스 설정")
    def_file = os.path.join(work_dir, "case_setup.def")
    # launch_cfx_pre(ansys_root, def_file=def_file, batch_mode=False)
    print("    -> 스킵 (예제 정의 파일 없음)")

    # 3. CFX Solver로 계산 실행 (예제)
    print("\n[3/4] CFX Solver로 계산 실행")
    # launch_solver_manager(ansys_root, def_file=def_file, par_local=4)
    print("    -> 스킵 (예제 정의 파일 없음)")

    # 4. CFD-Post로 후처리 (예제)
    print("\n[4/4] CFD-Post로 결과 확인")
    res_file = os.path.join(work_dir, "results.res")
    # launch_cfd_post(ansys_root, res_file=res_file)
    print("    -> 스킵 (예제 결과 파일 없음)")

    print("\n워크플로우 완료!")


# ============================================
# 메인 실행
# ============================================
if __name__ == "__main__":
    print("="*60)
    print("PyAnsys CFX 모듈 실행 예제")
    print("="*60)

    # ANSYS 설치 경로 찾기
    ansys_root = find_ansys_installation()

    if not ansys_root:
        print("\n오류: ANSYS 설치를 찾을 수 없습니다.")
        print("\n다음 방법 중 하나를 시도하세요:")
        print("1. 환경 변수 설정:")
        print("   export AWP_ROOT=/path/to/ansys/v242")
        print("   또는")
        print("   export ANSYS_ROOT=/path/to/ansys/v242")
        print("\n2. 스크립트를 수정하여 ANSYS 경로를 직접 지정:")
        print("   ansys_root = '/usr/ansys_inc/v242'")
        sys.exit(1)

    print(f"\n사용할 ANSYS 경로: {ansys_root}")

    # 사용 예제 메뉴
    print("\n" + "="*60)
    print("실행할 모듈을 선택하세요:")
    print("="*60)
    print("1. TurboGrid 실행 (GUI)")
    print("2. CFX-Pre 실행 (GUI)")
    print("3. CFX Solver Manager 실행 (GUI)")
    print("4. CFD-Post 실행 (GUI)")
    print("5. 전체 워크플로우 예제 보기")
    print("0. 종료")

    try:
        choice = input("\n선택 (0-5): ").strip()

        if choice == "1":
            launch_turbogrid(ansys_root, batch_mode=False)

        elif choice == "2":
            launch_cfx_pre(ansys_root, batch_mode=False)

        elif choice == "3":
            launch_solver_manager(ansys_root)

        elif choice == "4":
            launch_cfd_post(ansys_root, batch_mode=False)

        elif choice == "5":
            run_complete_workflow(ansys_root)

        elif choice == "0":
            print("종료합니다.")

        else:
            print("잘못된 선택입니다.")

    except KeyboardInterrupt:
        print("\n\n프로그램이 중단되었습니다.")
    except Exception as e:
        print(f"\n오류 발생: {e}")


# ============================================
# 추가 사용 예제
# ============================================
"""
# 예제 1: TurboGrid 배치 모드 실행
ansys_root = "/usr/ansys_inc/v242"
turbogrid_script = "/path/to/blade_geometry.tse"
launch_turbogrid(ansys_root, script_file=turbogrid_script, batch_mode=True)

# 예제 2: CFX-Pre로 케이스 설정 자동화
def_file = "/path/to/case.def"
ccl_script = "/path/to/setup_boundary_conditions.ccl"
launch_cfx_pre(ansys_root, def_file=def_file, script_file=ccl_script, batch_mode=True)

# 예제 3: CFX Solver 병렬 실행 (4 코어)
def_file = "/path/to/case_setup.def"
launch_solver_manager(ansys_root, def_file=def_file, par_local=4)

# 예제 4: CFD-Post 스크립트 자동 실행
res_file = "/path/to/results.res"
cse_script = "/path/to/create_plots.cse"
launch_cfd_post(ansys_root, res_file=res_file, script_file=cse_script, batch_mode=True)

# 예제 5: Python으로 CFX 워크플로우 자동화
def automate_cfx_analysis(geometry_file, output_dir):
    # 1. TurboGrid로 격자 생성
    turbogrid_script = create_turbogrid_script(geometry_file)
    launch_turbogrid(ansys_root, script_file=turbogrid_script, batch_mode=True)

    # 2. CFX-Pre로 케이스 설정
    ccl_script = create_setup_script(output_dir)
    def_file = os.path.join(output_dir, "case.def")
    launch_cfx_pre(ansys_root, script_file=ccl_script, batch_mode=True)

    # 3. 솔버 실행
    launch_solver_manager(ansys_root, def_file=def_file, par_local=8)

    # 4. 후처리
    res_file = os.path.join(output_dir, "results.res")
    post_script = create_post_script(res_file)
    launch_cfd_post(ansys_root, res_file=res_file, script_file=post_script, batch_mode=True)
"""


# ============================================
# 유용한 팁
# ============================================
"""
CFX 모듈별 주요 파일 형식:
- TurboGrid: .tse (스크립트), .gtm (격자 템플릿), .inf (격자 정보)
- CFX-Pre: .def (정의 파일), .ccl (CCL 스크립트), .gtm (격자)
- CFX Solver: .def (입력), .res (결과), .out (출력 로그)
- CFD-Post: .res (결과), .cse (세션 스크립트), .csv (데이터 내보내기)

환경 변수 설정 (Linux/Mac):
export AWP_ROOT=/usr/ansys_inc/v242
export PATH=$AWP_ROOT/CFX/bin:$PATH

환경 변수 설정 (Windows):
set AWP_ROOT=C:\Program Files\ANSYS Inc\v242
set PATH=%AWP_ROOT%\CFX\bin;%PATH%

PyAnsys 관련 패키지:
- ansys-tools-path: ANSYS 설치 경로 자동 탐지
- ansys-platform-instancemanagement: 원격 실행 관리

더 많은 정보:
- CFX 문서: https://ansyshelp.ansys.com/
- PyAnsys 문서: https://docs.pyansys.com/
"""
