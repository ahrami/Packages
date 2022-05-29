%%roots polynomial
%%solve; symbolic (syms x y z); can even do systems; vpasolve if cannot
%%find normally
%%fzero(@f, x0)
%%ginput look up
%%syms x y;
f = @(x)sin(x).*sin(x)+(0.5-1/x).*cos(x)-0.5;
answ = fzero(f, [pi/2, 3*pi]);
disp(answ);

syms x;
f = sin(x).*sin(x)+(0.5-1/x).*cos(x)-0.5;
answ = solve(f);
disp(answ);

n = 6;
x = -10*pi:0.01:10*pi;
f = @(x)sin(x).*(x+1);
y = f(x);
plot(x, y, x, 0*x); grid on
hold on
xlabel('x'); ylabel('y');
inputPoint = ginput(1);
plot(inputPoint(1), inputPoint(2), '*')
count = 0;
x0 = zeros(n,1);
y0 = zeros(n,1);
a = 0;
while count < n
    [x0tmp, y0tmp] = fzero(f, inputPoint(1)+a);
    zero = 0;
    for b = 0:count
        if b == count
            x0(count + 1) = x0tmp;
            y0(count + 1) = y0tmp;
            count = count + 1;
            plot(x0(count), y0(count), '*');
            disp([x0(count) y0(count)]);
        end
        if abs(x0tmp) > 1e-6 && abs(x0tmp - x0(b+1)) < 1e-6
            break;
        end
        if abs(x0(b+1)) <= 1e-6
            zero = zero + 1;
        end
        if zero > 0 && abs(x0tmp) <= 1e-6
            break
        end
    end
    if a > 0
        a = -a - 0.1;
    else
        a = -a + 0.1;
    end
end
hold off

x = -2*pi:0.01:2*pi;
f = @(x)1+(1+sin(x)-cos(x)).^2-(sin(2*x)-cos(2*x)-0.2).^2;
y = f(x);
figure
plot(x, y, x, 0*x); grid on
xlabel('x'); ylabel('y');
z = ginput(1);
x0 = z(1);
h = 0.00001;
hold on
plot(z(1), z(2), '*')
i = 0;
while(abs(f(x0)) > 1e-5)
    i = i + 1;
    x0 = x0 - h*f(x0)/(f(x0+h)-f(x0));
end
plot(x0, f(x0), '*')
disp('newton');
disp(i);
disp('difference')
disp(x0 - fzero(f,z(1)))
hold off

figure
plot(x, y, x, 0*x); grid on
xlabel('x'); ylabel('y');
hold on
x1 = ginput(1);
plot(x1(1), x1(2), '*');
x1 = x1(1);
x2 = ginput(1);
plot(x2(1), x2(2), '*');
x2 = x2(1);
c = (x1 + x2) / 2;
if f(x1)*f(x2) <= 0
    i = 0;
    while abs(x1 - x2) > 1e-8
        i = i + 1;
        c = (x1 + x2) / 2;
        if f(x1)*f(c) < 0
            x2 = c;
        else
            x1 = c;
        end
    end
    disp('divide');
    disp(i);
    plot(c, f(c), '*')
else
    disp('no');
end
hold off







