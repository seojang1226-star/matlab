% test_calc_temp.m - Test script for temperature calculation
% This script demonstrates how to calculate temperature from pressure and enthalpy

clear;
clc;

fprintf('=== Temperature Calculation from Pressure and Enthalpy ===\n\n');

% Example 1: High pressure steam
P1 = 10.0;      % MPa
h1 = 3000.5;    % kJ/kg
T1 = calc_temp_from_ph(P1, h1);
fprintf('Example 1:\n');
fprintf('  Pressure:  %.2f MPa\n', P1);
fprintf('  Enthalpy:  %.2f kJ/kg\n', h1);
fprintf('  Temperature: %.2f °C\n\n', T1);

% Example 2: Medium pressure steam
P2 = 5.0;       % MPa
h2 = 2800.0;    % kJ/kg
T2 = calc_temp_from_ph(P2, h2);
fprintf('Example 2:\n');
fprintf('  Pressure:  %.2f MPa\n', P2);
fprintf('  Enthalpy:  %.2f kJ/kg\n', h2);
fprintf('  Temperature: %.2f °C\n\n', T2);

% Example 3: Array calculation
fprintf('Example 3: Multiple calculations\n');
P_array = [1.0, 5.0, 10.0, 15.0];    % MPa
h_array = [2700, 2800, 3000, 3200];  % kJ/kg

fprintf('  P[MPa]  h[kJ/kg]  T[°C]\n');
fprintf('  ------------------------\n');
for i = 1:length(P_array)
    T = calc_temp_from_ph(P_array(i), h_array(i));
    fprintf('  %6.2f  %8.2f  %6.2f\n', P_array(i), h_array(i), T);
end
