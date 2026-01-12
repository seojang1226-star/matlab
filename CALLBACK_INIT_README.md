# MATLAB 버튼 콜백 변수 초기화 가이드

## 문제 상황
버튼을 여러 번 클릭할 때, 이전 실행의 변수가 남아있어 다음과 같은 문제가 발생할 수 있습니다:
- 배열 크기 불일치 오류
- 예상치 못한 변수 값
- 메모리 누수
- 논리 오류

## 해결 방법
콜백 함수의 **맨 앞부분**에 모든 변수를 명시적으로 초기화합니다.

## 📁 예제 파일

### 1. `button_callback_example.m`
기본 GUI 예제 - 직접 실행하여 차이를 확인할 수 있습니다.

```matlab
% MATLAB에서 실행
button_callback_example()
```

**특징:**
- ✅ 올바른 초기화 방법 (녹색 버튼)
- ❌ 초기화 없는 방법 (빨간 버튼) - 비교용

### 2. `callback_init_patterns.m`
실무에서 사용하는 다양한 초기화 패턴

```matlab
% 모든 패턴 실행
callback_init_patterns()
```

**포함된 패턴:**
- 기본 변수 타입별 초기화
- 구조체를 이용한 체계적 초기화
- GUI 핸들 데이터 초기화

## 🎯 빠른 시작 템플릿

### 기본 템플릿
```matlab
function myButtonCallback(src, event)
    % ========== 변수 초기화 (필수!) ==========
    data = [];
    result = [];
    counter = 0;
    status = '';
    isComplete = false;

    % ========== 실제 처리 로직 ==========
    % 여기에 실제 코드 작성
    data = rand(100, 1);
    result = mean(data);
    counter = length(data);
    status = '완료';
    isComplete = true;

    fprintf('처리 완료: %s\n', status);
end
```

### 구조체 사용 템플릿 (권장)
```matlab
function myAdvancedCallback(src, event)
    % ========== 구조체로 체계적 초기화 ==========
    params = struct();
    params.input = [];
    params.output = [];
    params.config = struct('mode', 'auto', 'verbose', true);
    params.status = struct('running', false, 'progress', 0);

    results = struct();

    % ========== 실제 처리 로직 ==========
    params.input = rand(100, 1);
    params.status.running = true;

    % 처리...
    results.mean = mean(params.input);
    results.std = std(params.input);

    params.status.running = false;
    params.status.progress = 100;
end
```

## 📌 변수 타입별 초기화 방법

| 타입 | 초기화 방법 | 예시 |
|------|------------|------|
| 숫자 | `0` 또는 원하는 값 | `count = 0;` |
| 배열 | `[]` 또는 `zeros()` | `data = [];` 또는 `data = zeros(10,1);` |
| 행렬 | `[]` 또는 `zeros(m,n)` | `matrix = zeros(5, 5);` |
| 문자열 | `''` | `message = '';` |
| 셀 배열 | `{}` | `cellData = {};` |
| 구조체 | `struct()` | `params = struct();` |
| 테이블 | `table()` | `dataTable = table();` |
| 논리형 | `false` 또는 `true` | `isReady = false;` |

## ⚠️ 주의사항

### DO ✅
```matlab
function goodCallback(~, ~)
    % 맨 앞에서 초기화
    data = [];
    result = [];

    % 처리
    data = processData();
    result = analyze(data);
end
```

### DON'T ❌
```matlab
function badCallback(~, ~)
    % 초기화 없이 바로 사용
    data = [data, newData];  % data가 이전 값일 수 있음!
    result = result + 1;      % result가 정의되지 않을 수 있음!
end
```

## 🔍 핸들 데이터 사용 시

GUI 핸들에 데이터를 저장하는 경우:

```matlab
function handleCallback(src, ~)
    % 이전 데이터 완전 제거
    if isappdata(src, 'myData')
        rmappdata(src, 'myData');
    end

    % 새로운 데이터 구조 생성
    appData = struct();
    appData.values = [];
    appData.timestamp = datetime('now');

    % 처리 및 저장
    appData.values = rand(100, 1);
    setappdata(src, 'myData', appData);
end
```

## 💡 베스트 프랙티스

1. **항상 초기화**: 모든 변수를 콜백 시작 부분에서 초기화
2. **구조체 사용**: 관련 변수들을 구조체로 그룹화
3. **명확한 구분**: 주석으로 초기화 섹션과 로직 섹션 구분
4. **일관성 유지**: 프로젝트 전체에서 동일한 패턴 사용
5. **테스트**: 버튼을 여러 번 클릭하여 동작 확인

## 실행 방법

```matlab
% 1. GUI 예제 실행
button_callback_example()

% 2. 패턴 예제 실행 (콘솔 출력)
callback_init_patterns()
```

## 추가 자료

- MATLAB 공식 문서: [Callbacks](https://www.mathworks.com/help/matlab/creating_plots/callback-definition.html)
- App Designer의 경우 properties 섹션에서 변수 관리 가능
