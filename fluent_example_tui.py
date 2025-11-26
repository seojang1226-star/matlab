"""
ANSYS Fluent 자동화 예제 - TUI (Text User Interface) 명령어 사용

이 스크립트는 Fluent TUI 명령어를 사용하여
격자를 불러오고 경계 조건을 설정하는 예제입니다.

TUI 방식은 PyFluent보다 더 세밀한 제어가 가능하며,
Fluent Journal 파일(.jou)과 호환됩니다.
"""

import ansys.fluent.core as pyfluent

# ============================================
# 1. Fluent 세션 시작
# ============================================
print("=== Fluent 세션 시작 (TUI 모드) ===")

solver = pyfluent.launch_fluent(
    precision="double",
    processor_count=4,
    mode="solver",
    dimension=3,
    show_gui=False
)

# TUI 객체 가져오기
tui = solver.tui

print("Fluent TUI 세션이 시작되었습니다.")


# ============================================
# 2. 격자 파일 불러오기 (TUI)
# ============================================
print("\n=== 격자 파일 불러오기 (TUI) ===")

mesh_file = "/path/to/your/mesh_file.msh"

# TUI 명령어로 파일 읽기
# file/read-case filename
try:
    tui.file.read_case(mesh_file)
    print(f"격자 파일 '{mesh_file}' 로드 완료")
except:
    print("격자 파일 로드 실패. 예제 케이스를 사용합니다.")
    from ansys.fluent.core import examples
    import_file = examples.download_file("mixing_elbow.msh.h5", "pyfluent/mixing_elbow")
    tui.file.read_case(import_file)
    print("예제 케이스 로드 완료")


# ============================================
# 3. 솔버 설정 (TUI)
# ============================================
print("\n=== 솔버 설정 (TUI) ===")

# Pressure-based solver 설정
tui.define.models.solver.pressure_based("yes")

# Steady state 설정
tui.define.models.steady("yes")

print("솔버 설정: Pressure-based, Steady")


# ============================================
# 4. 난류 모델 설정 (TUI)
# ============================================
print("\n=== 난류 모델 설정 (TUI) ===")

# k-epsilon 모델 활성화
# define/models/viscous/ke-standard yes
tui.define.models.viscous.ke_standard("yes")

print("난류 모델: k-epsilon (standard)")


# ============================================
# 5. 물성치 설정 (TUI)
# ============================================
print("\n=== 물성치 설정 (TUI) ===")

# 공기 물성 설정
# define/materials/change-create air air yes constant 1.225 no no yes constant 1.7894e-05 no no no no no
tui.define.materials.change_create(
    "air",  # 재료 이름
    "air",  # 재료 타입
    "yes",  # 밀도 변경
    "constant",  # 밀도 옵션
    1.225,  # 밀도 값 [kg/m³]
    "no",  # 엔탈피
    "no",  # 더 이상 엔탈피 관련 옵션 없음
    "yes",  # 점성 변경
    "constant",  # 점성 옵션
    1.7894e-05,  # 점성 값 [kg/m·s]
    "no",  # 열전도도
    "no",  # 더 이상 옵션 없음
    "no",
    "no",
    "no"
)

print("유체 물성 설정 완료")


# ============================================
# 6. 경계 조건 설정 (TUI)
# ============================================
print("\n=== 경계 조건 설정 (TUI) ===")

# 사용 가능한 경계 조건 확인
# 실제 경계 이름은 사용자의 격자 파일에 따라 다릅니다

# 예제 1: 속도 입구 조건 설정
# define/boundary-conditions/velocity-inlet inlet yes no 10 no 0 no 0 no no yes 5 10
inlet_bc = "inlet"  # 실제 입구 이름으로 변경
print(f"입구 경계 조건 설정: {inlet_bc}")

tui.define.boundary_conditions.velocity_inlet(
    inlet_bc,  # 경계 이름
    "yes",  # 속도 설정
    "no",  # 방향 벡터 사용 안함
    10,  # 속도 크기 [m/s]
    "no",  # 온도 설정 안함
    0,  # 온도 (사용 안함)
    "no",  # 난류 강도 설정
    0,  # 난류 강도 (기본값 사용)
    "no",  # 난류 점성비 설정
    "no",  # 더 이상 옵션 없음
    "yes",  # 난류 명세 방법
    5,  # 난류 강도 [%]
    10  # 난류 점성비
)

# 예제 2: 압력 출구 조건 설정
# define/boundary-conditions/pressure-outlet outlet yes no 0 no 300 no yes no yes 5 10
outlet_bc = "outlet"  # 실제 출구 이름으로 변경
print(f"출구 경계 조건 설정: {outlet_bc}")

tui.define.boundary_conditions.pressure_outlet(
    outlet_bc,  # 경계 이름
    "yes",  # 압력 설정
    "no",  # 방사 옵션
    0,  # 게이지 압력 [Pa]
    "no",  # 온도 설정
    300,  # 온도 [K] (설정 안함)
    "no",  # 역류 조건
    "yes",  # 난류 명세 방법
    "no",
    "yes",
    5,  # 역류 난류 강도 [%]
    10  # 역류 난류 점성비
)

# 예제 3: 벽면 조건 설정
# define/boundary-conditions/wall wall yes no 0 no 0
wall_bc = "wall"  # 실제 벽면 이름으로 변경
print(f"벽면 경계 조건 설정: {wall_bc}")

tui.define.boundary_conditions.wall(
    wall_bc,  # 경계 이름
    "yes",  # 전단 조건 (no-slip)
    "no",  # 벽면 운동 없음
    0,  # 벽면 속도
    "no",  # 열 조건
    0  # 온도/열유속
)

print("경계 조건 설정 완료")


# ============================================
# 7. 솔루션 제어 설정 (TUI)
# ============================================
print("\n=== 솔루션 제어 설정 ===")

# Under-relaxation factors (안정성을 위해 조정 가능)
# solve/set/under-relaxation/pressure 0.3
tui.solve.set.under_relaxation.pressure(0.3)
tui.solve.set.under_relaxation.momentum(0.7)

print("Under-relaxation factors 설정 완료")


# ============================================
# 8. 수렴 조건 설정 (TUI)
# ============================================
print("\n=== 수렴 조건 설정 ===")

# 잔차 수렴 기준 설정
# solve/monitors/residual/convergence-criteria 1e-4 1e-4 1e-4 1e-4 1e-4 1e-4
tui.solve.monitors.residual.convergence_criteria(
    1e-4,  # continuity
    1e-4,  # x-velocity
    1e-4,  # y-velocity
    1e-4,  # z-velocity
    1e-4,  # k
    1e-4   # epsilon
)

print("잔차 수렴 기준: 1e-4")


# ============================================
# 9. 솔루션 초기화 (TUI)
# ============================================
print("\n=== 솔루션 초기화 ===")

# Hybrid 초기화
# solve/initialize/hyb-initialization
tui.solve.initialize.hyb_initialization()

print("Hybrid 초기화 완료")


# ============================================
# 10. 계산 실행 (TUI)
# ============================================
print("\n=== 계산 실행 ===")

# 자동 저장 설정 (50회 반복마다)
tui.file.auto_save.data_frequency(50)

# 계산 실행
iterations = 100
print(f"{iterations}회 반복 계산 시작...")

# solve/iterate number-of-iterations
tui.solve.iterate(iterations)

print("계산 완료")


# ============================================
# 11. 결과 저장 (TUI)
# ============================================
print("\n=== 결과 저장 ===")

output_file = "/home/user/matlab/fluent_tui_results.cas.h5"

# file/write-case-data filename
tui.file.write_case_data(output_file)

print(f"결과 저장 완료: {output_file}")


# ============================================
# 12. 리포트 생성 (TUI)
# ============================================
print("\n=== 리포트 생성 ===")

# 표면적분 리포트 (예: 항력 계산)
# report/surface-integrals/area inlet ()

# 유량 리포트
# report/surface-integrals/mass-flow inlet ()

# 예제: inlet의 면적 리포트
try:
    print("inlet 면적 계산:")
    tui.report.surface_integrals.area("inlet", "()")
except:
    print("리포트 생성 실패 (경계 이름 확인 필요)")


# ============================================
# 13. Fluent 세션 종료
# ============================================
print("\n=== Fluent 세션 종료 ===")

solver.exit()

print("Fluent 세션이 종료되었습니다.")


# ============================================
# TUI 명령어 참고
# ============================================
print("\n=== TUI 명령어 참고 ===")
print("""
주요 TUI 명령어:

파일 작업:
- file/read-case filename
- file/read-data filename
- file/write-case-data filename

경계 조건:
- define/boundary-conditions/velocity-inlet
- define/boundary-conditions/pressure-outlet
- define/boundary-conditions/wall
- define/boundary-conditions/mass-flow-inlet

모델 설정:
- define/models/viscous/ke-standard
- define/models/viscous/kw-sst
- define/models/solver/pressure-based

솔루션:
- solve/initialize/hyb-initialization
- solve/iterate number
- solve/set/under-relaxation

리포트:
- report/surface-integrals/area
- report/surface-integrals/mass-flow
- report/forces

디스플레이:
- display/contour
- display/vector
- display/pathlines

TUI 명령어 확인:
Fluent 콘솔에서 '?'를 입력하면 사용 가능한 명령어 목록을 볼 수 있습니다.
각 메뉴 레벨에서 '?'를 입력하여 하위 명령어를 확인할 수 있습니다.
""")