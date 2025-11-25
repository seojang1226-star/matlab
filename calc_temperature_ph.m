function T = calc_temperature_ph(p, h)
    % calc_temperature_ph - Calculate temperature from pressure and enthalpy
    % Based on IAPWS-IF97 standard (extracted from XSteam logic)
    %
    % Inputs:
    %   p - Pressure [MPa]
    %   h - Specific enthalpy [kJ/kg]
    %
    % Output:
    %   T - Temperature [°C]
    %
    % Example:
    %   T = calc_temperature_ph(10.0, 3000.5);

    % Constants
    R = 0.461526;  % kJ/(kg·K) - Specific gas constant for water

    % Convert pressure to absolute bar for internal calculations
    p_bar = p * 10;  % MPa to bar

    % Region boundaries
    p_critical = 22.064;  % MPa
    T_critical = 373.946;  % °C
    h_critical = 2087.5463;  % kJ/kg at critical point

    % Determine region based on pressure and enthalpy
    if p <= 0 || h <= 0
        error('Pressure and enthalpy must be positive');
    end

    % Get saturation properties at given pressure
    if p < p_critical
        T_sat = calc_Tsat_p(p);
        h_liquid = calc_hL_p(p);
        h_vapor = calc_hV_p(p);

        % Check if in two-phase region (Region 4)
        if h >= h_liquid && h <= h_vapor
            T = T_sat;
            return;
        elseif h < h_liquid
            % Compressed liquid (Region 1)
            T = calc_T_ph_region1(p, h);
            return;
        else
            % Superheated vapor (Region 2)
            T = calc_T_ph_region2(p, h);
            return;
        end
    else
        % High pressure (Region 3 or above critical)
        T = calc_T_ph_region2(p, h);
        return;
    end
end

%% Region 1: Compressed Liquid
function T = calc_T_ph_region1(p, h)
    % Iterative solution using Newton-Raphson
    T_guess = 300;  % Initial guess in K

    for iter = 1:20
        h_calc = calc_h_pT_region1(p, T_guess - 273.15);
        if abs(h_calc - h) < 0.001
            break;
        end

        % Derivative approximation
        dT = 0.1;
        h_calc_plus = calc_h_pT_region1(p, T_guess - 273.15 + dT);
        dh_dT = (h_calc_plus - h_calc) / dT;

        T_guess = T_guess - (h_calc - h) / dh_dT;
    end

    T = T_guess - 273.15;  % Convert to °C
end

%% Region 2: Superheated Vapor
function T = calc_T_ph_region2(p, h)
    % IAPWS-IF97 Region 2 backward equation T(p,h)
    % Coefficients for subregion 2a, 2b, 2c

    p_star = 1;     % MPa
    h_star = 2000;  % kJ/kg

    pi = p / p_star;
    eta = h / h_star;

    % Determine subregion
    h_boundary = calc_h2bc_p(p);

    if h <= h_boundary
        % Subregion 2a
        T = calc_T_ph_region2a(pi, eta);
    else
        % Subregion 2b or 2c
        if p <= 4
            T = calc_T_ph_region2b(pi, eta);
        else
            T = calc_T_ph_region2c(pi, eta);
        end
    end
end

%% Region 2a: T(p,h) backward equation
function T = calc_T_ph_region2a(pi, eta)
    % Coefficients (IAPWS-IF97 Table 24)
    I = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7];
    J = [0, 1, 2, 3, 7, 20, 0, 1, 2, 3, 7, 9, 11, 18, 44, 0, 2, 7, 36, 38, 40, 42, 44, 24, 44, 12, 32, 44, 32, 36, 42, 34, 44, 28];
    n = [1089.8952318288, 849.51654495535, -107.81748091826, 33.153654801263, -7.4232016790248, ...
         11.765048724356, 1.844574935579, -4.1792700549624, 6.2478196935812, -17.344563108114, ...
         -200.58176862096, 271.96065473796, -455.11318285818, 3091.9688604755, 252266.40357872, ...
         -6.1707422868339e-03, -0.31078046629583, 11.670873077107, 128127984.04046, -985549096.23276, ...
         2822454697.3002, -3594897141.0703, 1722734991.3197, -13551.334240775, 12848734.66465, ...
         1.3865724283226, 235988.32556514, -13105236.545054, 7399.9835474766, -551966.9703006, ...
         3715408.5996233, 19127.72923966, -415351.64835634, -62.459855192507];

    theta = 0;
    for k = 1:length(I)
        theta = theta + n(k) * pi^I(k) * (eta - 2.1)^J(k);
    end

    T = theta;  % Already in °C
end

%% Region 2b: T(p,h) backward equation
function T = calc_T_ph_region2b(pi, eta)
    % Simplified calculation for region 2b
    I = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 7, 7, 9, 9];
    J = [0, 1, 2, 12, 18, 24, 28, 40, 0, 2, 6, 12, 18, 24, 28, 40, 2, 8, 18, 40, 1, 2, 12, 24, 2, 12, 18, 24, 28, 40, 18, 24, 40, 28, 2, 28, 1, 40];
    n = [1489.5041079516, 743.07798314034, -97.708318797837, 2.4742464705674, -0.63281320016026, ...
         1.1385952129658, -0.47811863648625, 8.5208123431544e-03, 0.93747147377932, 3.3593118604916, ...
         3.3809355601454, 0.16844539671904, 0.73875745236695, -0.47128737436186, 0.15020273139707, ...
         -0.002176411421975, -0.021810755324761, -0.10829784403677, -0.046333324635812, 7.1280351959551e-05, ...
         1.1032831789999e-04, 1.8955248387902e-04, 3.0891541160537e-03, 1.3555504554949e-03, 2.8640237477456e-07, ...
         -1.0779857357512e-05, -7.6462712454814e-05, 1.4052392818316e-05, -3.1083814331434e-05, -1.0302738212103e-06, ...
         2.8217281635040e-07, 1.2704902271945e-06, 7.3803353468292e-08, -1.1030139238909e-08, -8.1456365207833e-14, ...
         -2.5180545682962e-11, -1.7565233969407e-18, 8.6934156344163e-15];

    theta = 0;
    for k = 1:length(I)
        theta = theta + n(k) * (pi - 2)^I(k) * (eta - 2.6)^J(k);
    end

    T = theta;
end

%% Region 2c: T(p,h) backward equation
function T = calc_T_ph_region2c(pi, eta)
    % Simplified for region 2c
    T = calc_T_ph_region2b(pi, eta);  % Approximation
end

%% Saturation temperature from pressure
function T_sat = calc_Tsat_p(p)
    % IAPWS-IF97 Saturation temperature equation
    p_star = 1;  % MPa
    n = [0, 0.11670521452767e4, -0.72421316703206e6, -0.17073846940092e2, ...
         0.12020824702470e5, -0.32325550322333e7, 0.14915108613530e2, ...
         -0.48232657361591e4, 0.40511340542057e6, -0.23855557567849, 0.65017534844798e3];

    beta = (p / p_star)^0.25;

    E = beta^2 + n(3) * beta + n(6);
    F = n(1) * beta^2 + n(4) * beta + n(7);
    G = n(2) * beta^2 + n(5) * beta + n(8);
    D = 2 * G / (-F - sqrt(F^2 - 4 * E * G));

    T_sat = (n(10) + D - sqrt((n(10) + D)^2 - 4 * (n(9) + n(10) * D))) / 2 - 273.15;
end

%% Saturated liquid enthalpy
function hL = calc_hL_p(p)
    T_sat = calc_Tsat_p(p);
    hL = calc_h_pT_region1(p, T_sat);
end

%% Saturated vapor enthalpy
function hV = calc_hV_p(p)
    T_sat = calc_Tsat_p(p);
    T_sat_K = T_sat + 273.15;

    % Region 2 enthalpy calculation (simplified)
    p_star = 1;
    T_star = 540;

    pi = p / p_star;
    tau = T_star / T_sat_K;

    % Ideal gas part
    J0 = [0, 1, -5, -4, -3, -2, -1, 2, 3];
    n0 = [-9.6927686500217, 10.086655968018, -0.005608791128302, 0.071452738081455, ...
          -0.40710498223928, 1.4240819171444, -4.383951131945, -0.28408632460772, 0.021268463753307];

    gamma0_tau = 0;
    for k = 1:length(J0)
        gamma0_tau = gamma0_tau + n0(k) * J0(k) * tau^(J0(k)-1);
    end

    % Residual part (simplified)
    gamma_r_tau = 0;  % Simplified

    hV = 2000 + (gamma0_tau + gamma_r_tau) * 0.461526 * T_sat_K;
end

%% Region 1 enthalpy
function h = calc_h_pT_region1(p, T)
    % Simplified Region 1 enthalpy (liquid)
    T_K = T + 273.15;
    p_star = 16.53;
    T_star = 1386;

    pi = p / p_star;
    tau = T_star / T_K;

    % Simplified coefficients
    h = 4.2 * T + 0.001 * p * 1000;  % Approximation for liquid
end

%% Boundary between region 2b and 2c
function h = calc_h2bc_p(p)
    % Boundary enthalpy
    p_star = 1;
    h_star = 2000;

    pi = p / p_star;

    eta = 0.90584278514723 - 0.67955786399241 * pi + 0.12809002730136 * pi^2;
    h = eta * h_star;
end
