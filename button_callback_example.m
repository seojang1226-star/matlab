% MATLAB 버튼 콜백 변수 초기화 예제
% 버튼을 여러 번 클릭해도 안전하게 실행되도록 변수를 초기화하는 방법

function button_callback_example()
    % GUI Figure 생성
    fig = figure('Name', '버튼 콜백 변수 초기화 예제', ...
                 'Position', [100, 100, 400, 300], ...
                 'NumberTitle', 'off');

    % 결과를 표시할 텍스트 영역
    resultText = uicontrol('Style', 'text', ...
                          'Position', [50, 150, 300, 100], ...
                          'String', '버튼을 클릭하세요', ...
                          'FontSize', 12, ...
                          'HorizontalAlignment', 'left');

    % 실행 버튼
    runBtn = uicontrol('Style', 'pushbutton', ...
                      'String', '데이터 처리 실행', ...
                      'Position', [100, 80, 200, 40], ...
                      'FontSize', 11, ...
                      'Callback', @processData);

    % 초기화 없는 버튼 (문제가 있는 예시)
    badBtn = uicontrol('Style', 'pushbutton', ...
                      'String', '초기화 없이 실행 (오류 발생)', ...
                      'Position', [100, 30, 200, 40], ...
                      'FontSize', 9, ...
                      'BackgroundColor', [1, 0.8, 0.8], ...
                      'Callback', @processDataWithoutInit);

    % ======== 올바른 콜백 함수: 변수 초기화 포함 ========
    function processData(~, ~)
        try
            % ★★★ 중요: 콜백 시작 부분에서 모든 변수 초기화 ★★★
            % 이전 실행의 변수가 남아있지 않도록 완전히 초기화
            data = [];           % 배열 초기화
            results = [];        % 결과 배열 초기화
            count = 0;           % 카운터 초기화
            status = '';         % 문자열 초기화
            isProcessed = false; % 플래그 초기화

            % 실제 데이터 처리 작업
            data = rand(1, 10);  % 랜덤 데이터 생성

            % 데이터 처리
            results = data * 2 + 5;
            count = length(results);

            % 통계 계산
            meanVal = mean(results);
            maxVal = max(results);
            minVal = min(results);

            status = sprintf('처리 완료!\n데이터 개수: %d\n평균: %.2f\n최대: %.2f\n최소: %.2f', ...
                           count, meanVal, maxVal, minVal);
            isProcessed = true;

            % 결과 표시
            resultText.String = status;
            resultText.ForegroundColor = [0, 0.6, 0];

            fprintf('✓ 성공: 변수가 올바르게 초기화되어 실행됨\n');

        catch ME
            % 오류 처리
            errorMsg = sprintf('오류 발생:\n%s', ME.message);
            resultText.String = errorMsg;
            resultText.ForegroundColor = [1, 0, 0];
            fprintf('✗ 오류: %s\n', ME.message);
        end
    end

    % ======== 잘못된 콜백 함수: 변수 초기화 없음 (비교용) ========
    function processDataWithoutInit(~, ~)
        try
            % ★★★ 문제: 변수 초기화 없이 바로 사용 ★★★
            % 이전 실행의 변수가 남아있을 수 있음

            % 변수가 이미 존재하면 크기가 다를 수 있어 오류 발생 가능
            data = [data, rand(1, 5)];  % 기존 data에 추가 시도

            % 예상치 못한 동작 발생 가능
            results = data * 2 + 5;

            status = sprintf('처리 완료 (초기화 없음)\n데이터 크기: %d', length(results));
            resultText.String = status;
            resultText.ForegroundColor = [1, 0.5, 0];

            fprintf('⚠ 경고: 변수 초기화 없이 실행됨 - 예상치 못한 동작 가능\n');

        catch ME
            errorMsg = sprintf('오류 발생 (예상됨):\n%s\n\n변수 초기화가 필요합니다!', ME.message);
            resultText.String = errorMsg;
            resultText.ForegroundColor = [1, 0, 0];
            fprintf('✗ 오류 발생 (초기화 부족): %s\n', ME.message);
        end
    end
end
