% test_temperature_ph.m - Test temperature calculation from pressure and enthalpy
% This script tests the standalone temperature calculation function

clear;
clc;

fprintf('=== Temperature Calculation from Pressure and Enthalpy ===\n');
fprintf('Based on IAPWS-IF97 Standard\n\n');

% Test Case 1: Superheated steam (typical HP turbine inlet)
fprintf('Test 1: HP Turbine Inlet Condition\n');
p1 = 10.0;      % MPa
h1 = 3000.0;    % kJ/kg
T1 = calc_temperature_ph(p1, h1);
fprintf('  Pressure:    %8.2f MPa\n', p1);
fprintf('  Enthalpy:    %8.2f kJ/kg\n', h1);
fprintf('  Temperature: %8.2f °C\n\n', T1);

% Test Case 2: Medium pressure steam
fprintf('Test 2: IP Turbine Condition\n');
p2 = 5.0;       % MPa
h2 = 2900.0;    % kJ/kg
T2 = calc_temperature_ph(p2, h2);
fprintf('  Pressure:    %8.2f MPa\n', p2);
fprintf('  Enthalpy:    %8.2f kJ/kg\n', h2);
fprintf('  Temperature: %8.2f °C\n\n', T2);

% Test Case 3: Low pressure steam
fprintf('Test 3: LP Turbine Condition\n');
p3 = 1.0;       % MPa
h3 = 2800.0;    % kJ/kg
T3 = calc_temperature_ph(p3, h3);
fprintf('  Pressure:    %8.2f MPa\n', p3);
fprintf('  Enthalpy:    %8.2f kJ/kg\n', h3);
fprintf('  Temperature: %8.2f °C\n\n', T3);

% Test Case 4: Extraction point
fprintf('Test 4: Extraction Point\n');
p4 = 3.5;       % MPa
h4 = 2950.0;    % kJ/kg
T4 = calc_temperature_ph(p4, h4);
fprintf('  Pressure:    %8.2f MPa\n', p4);
fprintf('  Enthalpy:    %8.2f kJ/kg\n', h4);
fprintf('  Temperature: %8.2f °C\n\n', T4);

% Test Case 5: Multiple calculations
fprintf('Test 5: Multiple Turbine Stages\n');
fprintf('  Stage  P[MPa]  h[kJ/kg]   T[°C]\n');
fprintf('  -------------------------------------\n');

P_stages = [12.0, 10.0, 7.5, 5.0, 3.0, 1.5, 0.5];
h_stages = [3100, 3000, 2950, 2900, 2850, 2800, 2700];

for i = 1:length(P_stages)
    T = calc_temperature_ph(P_stages(i), h_stages(i));
    fprintf('  %5d  %6.2f  %8.2f  %7.2f\n', i, P_stages(i), h_stages(i), T);
end

fprintf('\n=== Calculation Complete ===\n');
