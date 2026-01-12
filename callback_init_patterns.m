% 콜백 변수 초기화 패턴 모음
% 실무에서 자주 사용되는 변수 초기화 방법들

function callback_init_patterns()
    fprintf('=== MATLAB 콜백 변수 초기화 패턴 ===\n\n');

    % 패턴 1: 기본 변수 초기화
    pattern1_basic_init();

    % 패턴 2: 구조체 초기화
    pattern2_struct_init();

    % 패턴 3: 전역 변수/핸들 데이터 초기화
    pattern3_handle_data_init();
end

%% 패턴 1: 기본 변수 타입별 초기화
function pattern1_basic_init()
    fprintf('--- 패턴 1: 기본 변수 초기화 ---\n');

    % 콜백 함수 예시
    function buttonCallback(~, ~)
        % ========== 변수 초기화 섹션 ==========
        % 숫자형
        counter = 0;
        sumValue = 0;
        avgValue = 0;

        % 배열/행렬
        dataArray = [];
        resultMatrix = zeros(10, 10);  % 크기가 정해진 경우

        % 셀 배열
        cellData = {};

        % 문자열
        message = '';
        status = 'idle';

        % 논리형
        isComplete = false;
        hasError = false;

        % 테이블 (R2013b 이상)
        if exist('table', 'builtin')
            dataTable = table();
        end

        % ========== 실제 처리 로직 ==========
        counter = 1;
        dataArray = 1:10;
        resultMatrix = rand(10, 10);
        message = '처리 완료';
        isComplete = true;

        fprintf('  기본 초기화 완료: counter=%d, array size=%d\n', ...
                counter, length(dataArray));
    end

    buttonCallback([], []);
end

%% 패턴 2: 구조체를 이용한 체계적 초기화
function pattern2_struct_init()
    fprintf('\n--- 패턴 2: 구조체 초기화 ---\n');

    function advancedCallback(~, ~)
        % ========== 구조체로 변수 그룹화 및 초기화 ==========
        % 방법 1: 모든 필드를 한번에 초기화
        params = struct(...
            'inputData', [], ...
            'outputData', [], ...
            'settings', struct('tolerance', 1e-6, 'maxIter', 100), ...
            'status', struct('isRunning', false, 'progress', 0, 'error', ''));

        % 방법 2: 빈 구조체로 시작 (모든 이전 데이터 제거)
        results = struct();

        % ========== 실제 처리 ==========
        params.inputData = rand(100, 1);
        params.status.isRunning = true;
        params.status.progress = 0;

        % 처리 시뮬레이션
        for i = 1:10
            params.status.progress = i * 10;
            % 계산 수행...
        end

        results.mean = mean(params.inputData);
        results.std = std(params.inputData);
        results.count = length(params.inputData);

        params.status.isRunning = false;
        params.status.progress = 100;

        fprintf('  구조체 초기화 완료: progress=%d%%, mean=%.4f\n', ...
                params.status.progress, results.mean);
    end

    advancedCallback([], []);
end

%% 패턴 3: GUI 핸들 데이터 초기화
function pattern3_handle_data_init()
    fprintf('\n--- 패턴 3: 핸들 데이터 초기화 ---\n');

    % GUI 생성
    fig = figure('Name', '핸들 데이터 예제', ...
                 'NumberTitle', 'off', ...
                 'Position', [100, 100, 300, 200], ...
                 'Visible', 'off');  % 예제 실행시 화면에 표시 안함

    btn = uicontrol('Parent', fig, ...
                    'Style', 'pushbutton', ...
                    'String', '데이터 처리', ...
                    'Position', [100, 80, 100, 40], ...
                    'Callback', @handleDataCallback);

    function handleDataCallback(src, ~)
        % ========== 핸들 데이터 완전 초기화 ==========
        % 방법 1: 구조체로 한번에 초기화
        appData = struct();
        appData.session = struct(...
            'startTime', datetime('now'), ...
            'clickCount', 0, ...
            'lastResult', []);
        appData.cache = struct(...
            'data', [], ...
            'isValid', false);

        % 핸들에 저장
        setappdata(src, 'appData', appData);

        % ========== 또는 개별 초기화 ==========
        % 이전 앱 데이터가 있으면 모두 제거
        if isappdata(src, 'oldData')
            rmappdata(src, 'oldData');
        end

        % ========== 실제 처리 ==========
        appData.session.clickCount = appData.session.clickCount + 1;
        appData.cache.data = rand(50, 1);
        appData.cache.isValid = true;
        appData.session.lastResult = mean(appData.cache.data);

        % 업데이트된 데이터 저장
        setappdata(src, 'appData', appData);

        fprintf('  핸들 데이터 초기화 완료: clickCount=%d, mean=%.4f\n', ...
                appData.session.clickCount, appData.session.lastResult);
    end

    % 예제 실행
    handleDataCallback(btn, []);

    % Figure 닫기
    close(fig);
end
