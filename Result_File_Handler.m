% Button pushed function: Result_File_Button
function Result_File_ButtonPushed(app, event)
    app.folderPath = uigetdir('','Directory Folder Select');
    app.directory_folder = app.folderPath;
    app.Dyn_Data_Table = {};
    app.Deviation_Data_Table={};
    Text_Value = app.CR_Textarea.Value;

    if Text_Value == "0"
        app.RPM_Textarea.Value = {'0'};
        app.CR_Textarea.Value = {'0'};
        app.Ecc_Textarea.Value = {'0'};
    end

    if app.folderPath == 0
        uialert(app.UIFigure, '폴더 선택이 취소되었습니다.', 'Folder Selection Cancelled');
        return;
    end

    app.Result_File_Path_Textarea.Value = app.folderPath;
    folderList = dir(app.folderPath);
    app.CaseNames = {'Case Folder List'};

    for i = 1:length(folderList)
        if folderList(i).isdir && ~strcmp(folderList(i).name, '.') && ~strcmp(folderList(i).name, '..')
            app.CaseNames{end+1} = folderList(i).name;
        end
    end

    % Refactored: Update all 14 CFD_Case_List_DropDown components using a loop
    dropdownNames = {'CFD_Case_List_DropDown', 'CFD_Case_List_DropDown_2', ...
                     'CFD_Case_List_DropDown_3', 'CFD_Case_List_DropDown_4', ...
                     'CFD_Case_List_DropDown_5', 'CFD_Case_List_DropDown_6', ...
                     'CFD_Case_List_DropDown_7', 'CFD_Case_List_DropDown_8', ...
                     'CFD_Case_List_DropDown_9', 'CFD_Case_List_DropDown_10', ...
                     'CFD_Case_List_DropDown_11', 'CFD_Case_List_DropDown_12', ...
                     'CFD_Case_List_DropDown_13', 'CFD_Case_List_DropDown_14'};

    for i = 1:length(dropdownNames)
        app.(dropdownNames{i}).Items = app.CaseNames;
    end

    % Build Case_List for ListBoxes
    Case_List = {};
    for i = 1:length(folderList)
        if folderList(i).isdir && ~strcmp(folderList(i).name, '.') && ~strcmp(folderList(i).name, '..')
            Case_List{end+1} = folderList(i).name;
        end
    end

    app.ListBox_Seal_Type_1.Items = Case_List;
    app.ListBox_Seal_Type_2.Items = Case_List;
    app.ListBox_Seal_Type_1.Value = app.ListBox_Seal_Type_1.Items;
    app.ListBox_Seal_Type_2.Value = app.ListBox_Seal_Type_2.Items;
    app.ListBox_Result_Data_1.Value = app.ListBox_Result_Data_1.Items;
    app.ListBox_Result_Data_2.Value = app.ListBox_Result_Data_2.Items;

    app.CFD_Case_List_DropDown.Enable = 'on';

end
