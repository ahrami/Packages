function [A] = fun(n, m)
a = zeros(n,m);
b = ones(n,m);
A = [[b,a];[a,b]];
end

