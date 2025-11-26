"""
ANSYS Fluent 자동화 예제 - PyFluent 사용

이 스크립트는 Fluent를 단독으로 실행하고, 격자를 불러오며,
경계 조건을 설정하는 예제입니다.

사전 요구사항:
    pip install ansys-fluent-core

환경 변수 설정이 필요할 수 있습니다:
    export FLUENT_PATH=/path/to/fluent
"""

import ansys.fluent.core as pyfluent
from ansys.fluent.core import examples

# ============================================
# 1. Fluent 세션 시작
# ============================================
print("=== Fluent 세션 시작 ===")

# Fluent를 3D, double precision 모드로 실행
# dimension: 2 (2D) 또는 3 (3D)
# precision: "single" 또는 "double"
# processor_count: 사용할 코어 수 (병렬 계산)
solver = pyfluent.launch_fluent(
    precision="double",
    processor_count=4,  # 4개 코어 사용
    mode="solver",  # "solver" 또는 "meshing"
    dimension=3,  # 3D 문제
    show_gui=False  # GUI 없이 실행 (True로 하면 GUI 표시)
)

print("Fluent 세션이 시작되었습니다.")


# ============================================
# 2. 격자 파일 불러오기
# ============================================
print("\n=== 격자 파일 불러오기 ===")

# 격자 파일 경로 지정 (.msh 또는 .cas 파일)
mesh_file = "/path/to/your/mesh_file.msh"

# 예제: 실제 파일 경로로 변경하세요
# mesh_file = "/home/user/fluent_cases/pipe_flow.msh"

try:
    # 격자 파일 읽기
    solver.file.read(file_type="case", file_name=mesh_file)
    print(f"격자 파일 '{mesh_file}' 로드 완료")
except Exception as e:
    print(f"격자 파일 로드 실패: {e}")
    print("예제를 위해 내장 샘플 케이스를 사용합니다.")

    # 예제 케이스 다운로드 및 사용
    import_file = examples.download_file(
        "mixing_elbow.msh.h5",
        "pyfluent/mixing_elbow"
    )
    solver.file.read(file_type="case", file_name=import_file)
    print("예제 케이스 로드 완료")


# ============================================
# 3. 솔버 설정
# ============================================
print("\n=== 솔버 설정 ===")

# 솔버 타입 설정 (pressure-based 또는 density-based)
solver.setup.general.solver.type = "pressure-based"

# 시간 설정 (steady 또는 transient)
solver.setup.general.solver.time = "steady"

print("솔버 타입: Pressure-based, Steady")


# ============================================
# 4. 물성치 설정
# ============================================
print("\n=== 물성치 설정 ===")

# 유체 물성 (공기)
solver.setup.materials.fluid["air"] = {
    "density": {"option": "constant", "value": 1.225},  # kg/m^3
    "viscosity": {"option": "constant", "value": 1.7894e-5}  # kg/(m·s)
}

print("유체 물성 설정 완료: 공기 (밀도: 1.225 kg/m³, 점성: 1.7894e-5 kg/m·s)")


# ============================================
# 5. 경계 조건 설정
# ============================================
print("\n=== 경계 조건 설정 ===")

# 사용 가능한 경계 조건 영역 확인
print("사용 가능한 경계:")
boundary_names = solver.setup.boundary_conditions.get_boundary_zones()
for boundary in boundary_names:
    print(f"  - {boundary}")

# 예제: 입구 경계 조건 (velocity-inlet)
# 실제 경계 이름은 격자 파일에 따라 다릅니다
try:
    # 입구: 속도 입구 조건
    inlet_name = "inlet"  # 격자 파일의 실제 입구 이름으로 변경
    solver.setup.boundary_conditions.velocity_inlet[inlet_name] = {
        "momentum": {
            "velocity": {
                "value": 10  # m/s
            }
        },
        "turbulence": {
            "turbulent_intensity": 0.05,  # 5%
            "turbulent_viscosity_ratio": 10
        }
    }
    print(f"입구 '{inlet_name}' 설정: 속도 10 m/s")

    # 출구: 압력 출구 조건
    outlet_name = "outlet"  # 격자 파일의 실제 출구 이름으로 변경
    solver.setup.boundary_conditions.pressure_outlet[outlet_name] = {
        "momentum": {
            "gauge_pressure": {
                "value": 0  # Pa (게이지 압력)
            }
        }
    }
    print(f"출구 '{outlet_name}' 설정: 게이지 압력 0 Pa")

    # 벽면: 벽면 조건 (no-slip)
    wall_name = "wall"  # 격자 파일의 실제 벽면 이름으로 변경
    solver.setup.boundary_conditions.wall[wall_name] = {
        "momentum": {
            "shear_condition": "no-slip"
        }
    }
    print(f"벽면 '{wall_name}' 설정: No-slip 조건")

except Exception as e:
    print(f"경계 조건 설정 중 오류: {e}")
    print("경계 이름을 격자 파일에 맞게 수정하세요.")


# ============================================
# 6. 난류 모델 설정
# ============================================
print("\n=== 난류 모델 설정 ===")

# k-epsilon 난류 모델 사용
solver.setup.models.viscous.model = "k-epsilon"
solver.setup.models.viscous.k_epsilon_model = "standard"

print("난류 모델: k-epsilon (standard)")


# ============================================
# 7. 솔루션 초기화
# ============================================
print("\n=== 솔루션 초기화 ===")

# Hybrid 초기화 (권장)
solver.solution.initialization.hybrid_initialize()

print("솔루션 초기화 완료 (Hybrid Initialization)")


# ============================================
# 8. 반복 계산 설정 및 실행
# ============================================
print("\n=== 계산 실행 ===")

# 수렴 조건 설정
solver.solution.monitor.residual.options.criterion_type = "absolute"
solver.solution.monitor.residual.equations["continuity"] = {"absolute_criteria": 1e-4}

# 반복 계산 실행
number_of_iterations = 100
solver.solution.run_calculation.iterate(iter_count=number_of_iterations)

print(f"{number_of_iterations}회 반복 계산 완료")


# ============================================
# 9. 결과 저장
# ============================================
print("\n=== 결과 저장 ===")

# 케이스 및 데이터 파일 저장
output_case_file = "/home/user/matlab/fluent_results.cas.h5"
output_data_file = "/home/user/matlab/fluent_results.dat.h5"

solver.file.write(
    file_type="case-data",
    file_name=output_case_file
)

print(f"결과 저장 완료: {output_case_file}")


# ============================================
# 10. Fluent 세션 종료
# ============================================
print("\n=== Fluent 세션 종료 ===")

solver.exit()

print("Fluent 세션이 종료되었습니다.")


# ============================================
# 참고 사항
# ============================================
print("\n=== 참고 사항 ===")
print("""
이 스크립트 사용 방법:
1. ANSYS Fluent가 설치되어 있어야 합니다.
2. PyFluent 설치: pip install ansys-fluent-core
3. mesh_file 변수를 실제 격자 파일 경로로 변경
4. 경계 조건 이름(inlet, outlet, wall)을 격자에 맞게 수정
5. 스크립트 실행: python fluent_example_pyfluent.py

주요 경계 조건 타입:
- velocity_inlet: 속도 입구
- pressure_inlet: 압력 입구
- pressure_outlet: 압력 출구
- mass_flow_inlet: 질량 유량 입구
- wall: 벽면
- symmetry: 대칭면
- periodic: 주기 경계

더 많은 정보:
https://fluent.docs.pyansys.com/
""")