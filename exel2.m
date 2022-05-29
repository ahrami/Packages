T = readtable("fileExcel.xlsx");
a = 0;
b = 0;
thing = ["Руководитель"; "Исполнитель"];
for c = 1:size(T,1)
    if(strcmp(char(table2array(T(c,2))),thing(1)))
        a = a + 1;
        A(a,:) = T(c,:);
    else
        b = b + 1;
        B(b,:) = T(c,:);
    end
end
for c = 1:size(A,1)
    At = [table2array(A(c,1))];
end
for c = 1:size(B,1)
    Bt = [table2array(B(c,1))];
end
C = [string(At); string(Bt)];
TT = table(thing, C);
TT.Properties.VariableNames{'thing'} = 'Роли';
TT.Properties.VariableNames{'C'} = 'Люди';
disp(TT);
writetable(TT,"out.xlsx");
clear;