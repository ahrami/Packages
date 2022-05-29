%%
A = rand(20);
L = eig(A);
b = sort(L);
%%
A = rand(4);
L = eig(A);
[a, b] = eig(A);
(A*a - a*b) < 1.0e-10
%%
n = 20
A = -2 * diag(ones(n, 1)) + diag(ones(n-1, 1), 1) + diag(ones(n-1, 1), -1) + diag(ones(1, 1), n-1) + diag(ones(1, 1), -n+1)
%%
n = 4
A = magic(n)
a = max(A)
b = max(A')
c = max(max(A))
%%
fun(5,10)