function temperature = calc_temp_from_ph(pressure, enthalpy)
    % calc_temp_from_ph - Calculate temperature from pressure and enthalpy
    %
    % Inputs:
    %   pressure  - Total pressure [MPa]
    %   enthalpy  - Specific enthalpy [kJ/kg]
    %
    % Output:
    %   temperature - Temperature [°C]
    %
    % Example:
    %   T = calc_temp_from_ph(10.0, 3000.5);  % P=10 MPa, h=3000.5 kJ/kg

    % Convert MPa to bar (XSteam uses bar)
    pressure_bar = pressure * 10;

    % Calculate temperature using XSteam
    % XSteam('T_ph', P, h) returns temperature in °C
    try
        temperature = XSteam('T_ph', pressure_bar, enthalpy);
    catch
        error('XSteam library not found. Please install XSteam for steam properties calculation.');
    end

    % Check if result is valid
    if isnan(temperature) || isinf(temperature)
        warning('Invalid result. Check if pressure and enthalpy values are within valid range.');
    end
end
