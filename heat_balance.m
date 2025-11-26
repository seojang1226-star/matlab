function Heat_Balance_FileButtonPushed(app, event)
            %{
            app.EXTRACTIONLabel.Enable = 'on';
            app.Pre_Setting_Extraction_Temp.Enable = 'on';
            app.Pre_Setting_Extraction_Temp_TextArea.Enable = 'on';
            app.Pre_Setting_Extraction_Mass.Enable = 'on';
            app.Pre_Setting_Extraction_Mass_TextArea.Enable = 'on';
            app.Pre_Setting_Inter01_Mass.Enable = 'on';
            app.Pre_Setting_Inter01_Mass_TextArea.Enable = 'on';
            %}
            [res_file, res_path] = uigetfile({'*.res;','Pre Setting File(*.res)';}, 'Select File','pwd');
            if isequal(res_file, 0)
                uialert(app.UIFigure, '파일 선택이 취소되었습니다.', 'File Selection Cancelled');
                return;
            end
            res_File_Path = fullfile(res_path,res_file);
            app.Res_File = res_File_Path;
            app.Res_Path = res_path;
            app.Pre_File_Path_TextArea.Value = res_File_Path;
            content = fileread(res_File_Path);
            sections = strsplit(content, '------------------------------------------------------');
            tables = {};
            tables_out = {};
            for i = 1:length(sections)
                lines = strsplit(sections{i}, '\n');
                lines = lines(~cellfun(@isempty, strtrim(lines)));
                header_idx = find(contains(lines, 'p[ata]   e[kcal/kg]     q[t/hod]'), 1);
                if ~isempty(header_idx)
                    data_start = header_idx + 1;
                    data_lines = {};
                    j = data_start;
                    while j <= length(lines) && ~isempty(regexp(strtrim(lines{j}), '^\s*\d+,\s*\d+', 'once'))
                        data_lines{end+1} = lines{j};
                        j = j + 1;
                    end
                    if ~isempty(data_lines)
                        numRows = length(data_lines);
                        data = zeros(numRows, 12);
                        for k = 1:numRows
                            line = data_lines{k};
                            line = strrep(line, ',', ' ');
                            line = strrep(line, '|', ' ');
                            line = strrep(line, ';', ' ');
                            nums = str2double(regexp(line, '-?\d*\.?\d+', 'match'));
                            data(k, 1:min(length(nums), 12)) = nums(1:min(length(nums), 12));
                        end
                        table = array2table(data);
                        tables_out{end+1} = table;
                    end
                end
            end
            Inlet_counter = 0;
            Outlet_counter = 0;
            tables_out = tables_out{1, 1};
            tables_out = table2array(tables_out);
            for i = 1:height(tables_out)
                if tables_out(i,2) == 1
                    Inlet_Post_Value = tables_out(i,:);
                    Inlet_counter = Inlet_counter + 1;
                    Inlet_Post_Table(Inlet_counter,:) = Inlet_Post_Value;
                end
                if tables_out(i,2) == 2
                    Outlet_Post_Value = tables_out(i,:);
                    Outlet_counter = Outlet_counter + 1;
                    Outlet_Post_Table(Outlet_counter,:) = Outlet_Post_Value;
                end
            end
            diff_Inlet_Post_Table = diff(Inlet_Post_Table(:,1));
            split_Inlet_Post_Table = find(diff_Inlet_Post_Table >= 2);
            Inlet_Post_Table_New = cell(length(split_Inlet_Post_Table) + 1, 1);
            start_idx = 1;
            for i = 1:length(split_Inlet_Post_Table)
                end_idx = split_Inlet_Post_Table(i);
                Inlet_Post_Table_New{i} = Inlet_Post_Table(start_idx:end_idx, :);
                start_idx = end_idx + 1;
            end
            Inlet_Post_Table_New{end} = Inlet_Post_Table(start_idx:end, :);
            diff_Outlet_Post_Table = diff(Outlet_Post_Table(:,1));
            split_Outlet_Post_Table = find(diff_Outlet_Post_Table >= 2);
            Outlet_Post_Table_New = cell(length(split_Outlet_Post_Table) + 1, 1);
            start_idx = 1;
            for i = 1:length(split_Outlet_Post_Table)
                end_idx = split_Outlet_Post_Table(i);
                Outlet_Post_Table_New{i} = Outlet_Post_Table(start_idx:end_idx, :);
                start_idx = end_idx + 1;
            end
            Outlet_Post_Table_New{end} = Outlet_Post_Table(start_idx:end, :);
            HP_Inlet_Table = Inlet_Post_Table_New{1, 1};
            IP_Inlet_Table = Inlet_Post_Table_New{2, 1};
            HP_Outlet_Table = Outlet_Post_Table_New{1, 1};
            IP_Outlet_Table = Outlet_Post_Table_New{2, 1};
            for i = 1:length(sections)
                lines = strsplit(sections{i}, '\n');
                lines = lines(~cellfun(@isempty, strtrim(lines)));
                data_lines = lines(cellfun(@(x) ~isempty(regexp(strtrim(x), '^\d', 'once')), lines));
                if ~isempty(data_lines)
                    data = cellfun(@(x) textscan(x, '%f'), data_lines, 'UniformOutput', false);
                    max_cols = max(cellfun(@(x) length(x{1}), data));
                    matrix = zeros(length(data), max_cols);
                    for j = 1:length(data)
                        row_data = data{j}{1};
                        matrix(j, 1:length(row_data)) = row_data;
                    end
                    matrix(matrix == 0) = NaN;
                    table = array2table(matrix);
                    tables{end+1} = table;
                end
            end
            Table_1 = tables{1, 2};
            Table_2 = tables{1, 3};
            Turbine_Parts = Table_1{:,1};
            Turbine_Mass_Flow = Table_1{:,6};
            Turbine_Inlet_Pressure = Table_2{:,4};
            Turbine_Inlet_Enthalpy = Table_2{:,5};
            Turbine_Outlet_Pressure = Table_2{:,6};
            Pre_Post_Table = [Turbine_Parts, Turbine_Mass_Flow, Turbine_Inlet_Pressure, Turbine_Inlet_Enthalpy, Turbine_Outlet_Pressure];
            HP_Post_Table = [];
            Pre_Post_Table_New = Pre_Post_Table;
            hp_counter = 0;
            ip_counter = 0;
            for i = 1:height(Pre_Post_Table)
                if Pre_Post_Table_New(i,1) == 1
                    HP_Post_Value = Pre_Post_Table_New(i,:);
                    hp_counter = hp_counter + 1;
                    HP_Post_Table(hp_counter,:) = HP_Post_Value;
                end
                if Pre_Post_Table_New(i,1) == 2
                    IP_Post_Value = Pre_Post_Table_New(i,:);
                    ip_counter = ip_counter + 1;
                    IP_Post_Table(ip_counter,:) = IP_Post_Value;
                end
            end
            HP_Post_Table = array2table(HP_Post_Table);
            IP_Post_Table = array2table(IP_Post_Table);
            HP_Mass_Flow = HP_Post_Table{:,2};
            HP_Inlet_Pressure = HP_Post_Table{:,3};
            HP_Inlet_Enthalpy = HP_Post_Table{:,4};
            HP_Outlet_Presure = HP_Post_Table{:,5};
            IP_Mass_Flow = IP_Post_Table{:,2};
            IP_Inlet_Pressure = IP_Post_Table{:,3};
            IP_Inlet_Enthalpy = IP_Post_Table{:,4};
            IP_Outlet_Presure = IP_Post_Table{:,5};
            HP_Post_Table = [HP_Mass_Flow, HP_Inlet_Enthalpy, HP_Inlet_Pressure, HP_Outlet_Presure];
            IP_Post_Table = [IP_Mass_Flow, IP_Inlet_Enthalpy, IP_Inlet_Pressure, IP_Outlet_Presure];
            if app.HP_CheckBox.Value
                app.Pre_Setting_Table.Data = HP_Post_Table;
                Post_Table = HP_Post_Table;
                Inlet_Table = HP_Inlet_Table;
                Outlet_Table = HP_Outlet_Table;
            else
                app.Pre_Setting_Table.Data = IP_Post_Table;
                Post_Table = IP_Post_Table;
                Inlet_Table = IP_Inlet_Table;
                Outlet_Table = IP_Outlet_Table;
            end
            Inlet_Enthalpy = (Post_Table(app.Start_Stage,2))*4.186820884;
            Inlet_Pressure = (Post_Table(app.Start_Stage,3))*0.0980664921139645;
            Outlet_Pressure = (Post_Table(app.End_Stage,4))*0.0980664921139645;
            Inlet_Temperature = Inlet_Table(app.Start_Stage,6);
            app.Pre_Setting_Inlet_Ent_TextArea.Value = num2str(Inlet_Enthalpy);
            app.Pre_Setting_Inlet_Press_TextArea.Value = num2str(Inlet_Pressure);
            app.Pre_Setting_Outlet_Press_TextArea.Value = num2str(Outlet_Pressure);
            app.Pre_Setting_Inlet_Temp_TextArea.Value = num2str(Inlet_Temperature);
            diff_Outlet_Table_Ext = diff(Outlet_Table(:,9));
            Table_Ext = array2table(diff_Outlet_Table_Ext);
            diff_Outlet_Table_Ext = [diff_Outlet_Table_Ext; 0];
            range_table_ext = diff_Outlet_Table_Ext(app.Start_Stage:app.End_Stage, :);
            app.ext_numb = find(any(range_table_ext ~= 0, 2));
            app.Outlet_Post_Table_Ext = find(diff_Outlet_Table_Ext > 0);
            app.Extraction_Mass = Table_Ext{app.Outlet_Post_Table_Ext, :};
            Ext_Mass_Table = nonzeros(diff_Outlet_Table_Ext(app.Start_Stage : app.End_Stage));
            Extraction_Temp = Outlet_Table(1,6);
            app.Extraction_Count = sum(range_table_ext ~= 0);

            try
                app.EXTRACTIONLabel.Enable = 'off';
                app.Pre_Setting_Extraction_Temp.Enable = 'off';
                app.Pre_Setting_Extraction_Temp_2.Enable = 'off';
                app.Pre_Setting_Extraction_Temp_TextArea.Enable = 'off';
                app.Pre_Setting_Extraction_Mass.Enable = 'off';
                app.Pre_Setting_Extraction_Mass_2.Enable = 'off';
                app.Pre_Setting_Extraction_Mass_TextArea.Enable = 'off';
            catch
            end


            if ~app.Blade_Only_CheckBox.Value
                if app.Extraction_Count ~= 0

                    %{
                    app.EXTRACTIONLabel.Enable = 'off';
                    app.Pre_Setting_Extraction_Temp.Enable = 'off';
                    app.Pre_Setting_Extraction_Temp_2.Enable = 'off';
                    app.Pre_Setting_Extraction_Temp_TextArea.Enable = 'off';
                    app.Pre_Setting_Extraction_Mass.Enable = 'off';
                    app.Pre_Setting_Extraction_Mass_2.Enable = 'off';
                    app.Pre_Setting_Extraction_Mass_TextArea.Enable = 'off';
                    app.EXTRACTIONLabel.Visible = 'off';
                    app.Pre_Setting_Extraction_Temp.Visible = 'off';
                    app.Pre_Setting_Extraction_Temp_2.Visible = 'off';
                    app.Pre_Setting_Extraction_Temp_TextArea.Visible = 'off';
                    app.Pre_Setting_Extraction_Mass.Visible = 'off';
                    app.Pre_Setting_Extraction_Mass_2.Visible = 'off';
                    app.Pre_Setting_Extraction_Mass_TextArea.Visible = 'off';
                    %}

                    delete(allchild(app.Extraction_Table_Panel));

                    for i = 1 : app.Extraction_Count
                        New_Ext_Label_y = 95 + (app.Extraction_Count - i) * 140 ;
                        New_Ext_Label = uilabel(app.Extraction_Table_Panel);
                        New_Ext_Label.FontSize = 26;
                        New_Ext_Label.FontWeight = 'bold';
                        New_Ext_Label.FontColor = [0.502 0.502 0.502];
                        New_Ext_Label.Position = [16 New_Ext_Label_y 174 34];
                        if app.Extraction_Count == 1
                            New_Ext_Label.Text = 'Extraction';
                        else
                            New_Ext_Label.Text = ['Extraction ', num2str(i)];
                        end
                        New_Ext_Temp_Label_2_y = 58 + (app.Extraction_Count - i) * 140 ;
                        New_Ext_Temp_Label_2 = uilabel(app.Extraction_Table_Panel);
                        New_Ext_Temp_Label_2.FontSize = 20;
                        New_Ext_Temp_Label_2.FontWeight = 'bold';
                        New_Ext_Temp_Label_2.Position = [14 New_Ext_Temp_Label_2_y 177 26];
                        New_Ext_Temp_Label_2.Text = 'Total Temperature';

                        New_Ext_Temp_Label_3_y = 58 + (app.Extraction_Count - i) * 140 ;
                        New_Ext_Temp_Label_3 = uilabel(app.Extraction_Table_Panel);
                        New_Ext_Temp_Label_3.FontSize = 20;
                        New_Ext_Temp_Label_3.FontWeight = 'bold';
                        New_Ext_Temp_Label_3.Position = [293 New_Ext_Temp_Label_3_y 33 26];
                        New_Ext_Temp_Label_3.Text = '[C]';

                        New_Ext_Temp_Text_y = 56 + (app.Extraction_Count - i) * 140 ;
                        New_Ext_Temp_Text = uitextarea(app.Extraction_Table_Panel);
                        New_Ext_Temp_Text.Tag = ['Ext_Temp_', num2str(i)];
                        New_Ext_Temp_Text.HorizontalAlignment = 'right';
                        New_Ext_Temp_Text.WordWrap = 'off';
                        New_Ext_Temp_Text.FontSize = 16;
                        New_Ext_Temp_Text.Position = [199 New_Ext_Temp_Text_y 85 27];
                        New_Ext_Temp_Text.Value = num2str(Extraction_Temp);

                        New_Ext_Mass_Label_y = 15 + (app.Extraction_Count - i) * 140 ;
                        New_Ext_Mass_Label = uilabel(app.Extraction_Table_Panel);
                        New_Ext_Mass_Label.HorizontalAlignment = 'right';
                        New_Ext_Mass_Label.FontSize = 20;
                        New_Ext_Mass_Label.FontWeight = 'bold';
                        New_Ext_Mass_Label.Position = [82 New_Ext_Mass_Label_y 107 26];
                        New_Ext_Mass_Label.Text = 'Mass Flow';

                        New_Ext_Mass_Label_2_y = 15 + (app.Extraction_Count - i) * 140 ;
                        New_Ext_Mass_Label_2 = uilabel(app.Extraction_Table_Panel);
                        New_Ext_Mass_Label_2.FontSize = 20;
                        New_Ext_Mass_Label_2.FontWeight = 'bold';
                        New_Ext_Mass_Label_2.Position = [293 New_Ext_Mass_Label_2_y 59 26];
                        New_Ext_Mass_Label_2.Text = '[kg/s]';

                        New_Ext_Mass_Text_y = 13 + (app.Extraction_Count - i) * 140 ;
                        New_Ext_Mass_Text = uitextarea(app.Extraction_Table_Panel);
                        New_Ext_Mass_Text.Tag = ['Ext_Mass_', num2str(i)];
                        New_Ext_Mass_Text.HorizontalAlignment = 'right';
                        New_Ext_Mass_Text.WordWrap = 'off';
                        New_Ext_Mass_Text.FontSize = 16;
                        New_Ext_Mass_Text.Position = [199 New_Ext_Mass_Text_y 85 27];
                        New_Ext_Mass_Text.Value = num2str(Ext_Mass_Table(i));
                    end
                else
                    %{
                    app.EXTRACTIONLabel.Enable = 'off';
                    app.Pre_Setting_Extraction_Temp.Enable = 'off';
                    app.Pre_Setting_Extraction_Temp_2.Enable = 'off';
                    app.Pre_Setting_Extraction_Temp_TextArea.Enable = 'off';
                    app.Pre_Setting_Extraction_Mass.Enable = 'off';
                    app.Pre_Setting_Extraction_Mass_2.Enable = 'off';
                    app.Pre_Setting_Extraction_Mass_TextArea.Enable = 'off';
                    %}
                end
            end

            app.Pre_Setting_Inter01_Mass.Enable = 'on';
            app.Pre_Setting_Inter01_Mass_2.Enable = 'on';
            app.Pre_Setting_Inter01_Mass_TextArea.Enable = 'on';
            lines = strsplit(content, '\n');
            rpm_line = '';
            for i = 1:length(lines)
                if contains(lines{i}, 'r.p.m.')
                    rpm_line = lines{i};
                    break;
                end
            end
            if ~isempty(rpm_line)
                pattern = '(\d+)\s*\.\s*r\.p\.m\.';
                [match, ~] = regexp(rpm_line, pattern, 'tokens', 'match');
                if ~isempty(match)
                    rpm_value = str2double(match{1}{1});
                end
            end

            if app.Blade_Only_CheckBox.Value
                app.INTERSTAGEINLETLabel.Enable = 'off';
                app.Pre_Setting_Inter01_Mass_2.Enable = 'off';
                app.Pre_Setting_Inter01_Mass_TextArea.Enable = 'off';
                app.Pre_Setting_Inter01_Mass.Enable = 'off';
                try
                    app.EXTRACTIONLabel.Enable = 'off';
                    app.Pre_Setting_Extraction_Temp.Enable = 'off';
                    app.Pre_Setting_Extraction_Temp_2.Enable = 'off';
                    app.Pre_Setting_Extraction_Temp_TextArea.Enable = 'off';
                    app.Pre_Setting_Extraction_Mass.Enable = 'off';
                    app.Pre_Setting_Extraction_Mass_2.Enable = 'off';
                    app.Pre_Setting_Extraction_Mass_TextArea.Enable = 'off';
                catch
                end

            end
            app.Pre_Setting_RPM_TextArea.Value = num2str(rpm_value);
            app.Pre_Project_Name_TextArea.Value = app.Project_Name_TextArea.Value;
            app.DataFileExportButton.Enable = 'On';
            figure(app.UIFigure);
        end
