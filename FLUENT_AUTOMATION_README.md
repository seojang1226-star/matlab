# ANSYS Fluent 자동화 예제

Fluent를 단독으로 실행하고 격자를 불러와 경계 조건을 설정하는 세 가지 방법을 제공합니다.

## 📁 파일 목록

1. **fluent_example_pyfluent.py** - PyFluent API 사용 (권장)
2. **fluent_example_tui.py** - TUI 명령어 사용
3. **fluent_example.jou** - Journal 파일 (Fluent 네이티브)

---

## 🚀 방법 1: PyFluent (권장)

### 특징
- 최신 Python API
- 객체 지향적 접근
- 타입 체킹 및 자동완성 지원
- 가장 직관적이고 읽기 쉬운 코드

### 설치
```bash
pip install ansys-fluent-core
```

### 실행
```bash
python fluent_example_pyfluent.py
```

### 주요 코드 예시
```python
import ansys.fluent.core as pyfluent

# Fluent 실행
solver = pyfluent.launch_fluent(
    precision="double",
    processor_count=4,
    dimension=3,
    show_gui=False
)

# 격자 불러오기
solver.file.read(file_type="case", file_name="mesh.msh")

# 경계 조건 설정
solver.setup.boundary_conditions.velocity_inlet["inlet"] = {
    "momentum": {"velocity": {"value": 10}}
}

# 계산 실행
solver.solution.run_calculation.iterate(iter_count=100)
```

---

## ⚙️ 방법 2: TUI (Text User Interface)

### 특징
- Fluent의 전통적인 명령어 인터페이스
- 더 세밀한 제어 가능
- Journal 파일과 호환
- 복잡한 설정에 유용

### 실행
```bash
python fluent_example_tui.py
```

### 주요 코드 예시
```python
import ansys.fluent.core as pyfluent

solver = pyfluent.launch_fluent(...)
tui = solver.tui

# TUI 명령어 사용
tui.file.read_case("mesh.msh")
tui.define.models.viscous.ke_standard("yes")
tui.define.boundary_conditions.velocity_inlet(
    "inlet", "yes", "no", 10, ...
)
tui.solve.iterate(100)
```

---

## 📝 방법 3: Journal 파일 (.jou)

### 특징
- Fluent 네이티브 스크립트 형식
- GUI 없이 완전 자동화
- 배치 작업에 최적
- 재현성이 뛰어남

### 실행 방법

#### GUI에서 실행
1. Fluent 실행
2. File → Read → Journal...
3. `fluent_example.jou` 선택

#### 명령줄에서 실행 (배치 모드)
```bash
# 3D, double precision, 4 코어
fluent 3ddp -t4 -i fluent_example.jou

# 백그라운드에서 실행
fluent 3ddp -t4 -i fluent_example.jou > output.log 2>&1 &
```

### Journal 파일 예시
```scheme
; 격자 읽기
/file/read-case mesh.msh

; 솔버 설정
/define/models/solver/pressure-based yes
/define/models/steady yes

; 난류 모델
/define/models/viscous/ke-standard yes

; 경계 조건
/define/boundary-conditions/velocity-inlet inlet yes no 10 no 300 no no yes 5 10

; 계산 실행
/solve/initialize/hyb-initialization
/solve/iterate 100

; 저장
/file/write-case-data results.cas.h5
/exit yes
```

---

## 📊 경계 조건 타입

### 입구 조건
- **velocity-inlet**: 속도 지정
- **pressure-inlet**: 압력 지정
- **mass-flow-inlet**: 질량 유량 지정

### 출구 조건
- **pressure-outlet**: 압력 출구 (가장 일반적)
- **outflow**: 유출 경계
- **pressure-far-field**: 원방 경계 (외부 유동)

### 벽면 조건
- **wall**: 고체 벽면 (no-slip 또는 slip)
- **symmetry**: 대칭면
- **axis**: 축대칭 축

### 기타
- **periodic**: 주기 경계
- **interface**: 유체-유체 경계면

---

## 🔧 주요 설정 항목

### 1. 격자 파일 경로
세 파일 모두에서 다음 부분을 수정하세요:
```python
mesh_file = "/path/to/your/mesh_file.msh"
```

### 2. 경계 이름
격자 파일의 실제 경계 이름으로 변경:
```python
inlet_name = "inlet"      # 실제 입구 이름
outlet_name = "outlet"    # 실제 출구 이름
wall_name = "wall"        # 실제 벽면 이름
```

### 3. 물리 모델
- 솔버: `pressure-based` 또는 `density-based`
- 시간: `steady` 또는 `transient`
- 난류: `k-epsilon`, `k-omega`, `SST`, `Spalart-Allmaras` 등

### 4. 경계 조건 값
```python
velocity = 10          # m/s
pressure = 0           # Pa (gauge)
temperature = 300      # K
turbulent_intensity = 5  # %
```

---

## 🎯 사용 시나리오별 추천

### 단순 자동화 + 재현성
→ **Journal 파일 (.jou)** 사용

### Python 기반 파라미터 스터디
→ **PyFluent** 사용

### 복잡한 설정 + 세밀한 제어
→ **TUI 방식** 사용

### 대규모 배치 작업
→ **Journal 파일** + Shell 스크립트 조합

---

## 💡 유용한 팁

### 1. 경계 이름 확인하기
```python
# PyFluent
boundary_names = solver.setup.boundary_conditions.get_boundary_zones()
print(boundary_names)

# TUI
tui.mesh.check()
```

### 2. 병렬 계산
```python
# 4개 코어 사용
solver = pyfluent.launch_fluent(processor_count=4)
```

```bash
# Journal 파일 실행 시
fluent 3ddp -t4 -i example.jou
```

### 3. GUI 사용
개발/디버깅 시 GUI를 켜면 실시간으로 확인 가능:
```python
solver = pyfluent.launch_fluent(show_gui=True)
```

### 4. 결과 모니터링
```python
# 잔차 플롯 저장
solver.solution.monitor.residual.plot = True
```

---

## 🔍 트러블슈팅

### Fluent를 찾을 수 없는 경우
환경 변수 설정:
```bash
export AWP_ROOT242=/path/to/ansys_inc/v242
export FLUENT_PATH=$AWP_ROOT242/fluent
```

### 라이센스 오류
```bash
# 라이센스 서버 확인
echo $ANSYSLMD_LICENSE_FILE

# 라이센스 서버 설정
export ANSYSLMD_LICENSE_FILE=port@server
```

### 경계 조건 설정 실패
1. 격자 파일에서 경계 이름 확인
2. 경계 타입이 올바른지 확인
3. TUI 명령어 순서 확인

---

## 📚 참고 자료

- [PyFluent 공식 문서](https://fluent.docs.pyansys.com/)
- [Fluent TUI 가이드](https://ansyshelp.ansys.com/)
- [Fluent Theory Guide](https://ansyshelp.ansys.com/Views/Secured/corp/v242/en/flu_th/flu_th.html)

---

## 📞 추가 도움말

더 자세한 정보가 필요하면 다음 명령어로 도움말 확인:

```python
# PyFluent
help(solver.setup.boundary_conditions)

# TUI에서
# Fluent 콘솔에서 '?' 입력
```
