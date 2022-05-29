fig = uifigure;
ax1 = uiaxes(fig,'Position',[10 220 200 200]);

x = 0:0.0001:2;
y = humps(x);
y2040 = (y >= 20 & y <= 40);
x2 = x(y2040);
y2 = y(y2040);
minimum = y == min(y);
maximum = y == max(y);
plot(ax1, x, y, x2, y2, "*", x(minimum), y(minimum), "*", x(maximum), y(maximum), "*");

global nv mv av phi;
nv = 1;
mv = 1;
av = 1;

global ax2;
ax2 = uiaxes(fig,'Position',[10 10 200 200]);
global n m a;
n = uislider(fig,'Value',1, 'Position',[220 40 200 200], 'ValueChangingFcn',@(n, event) sliderMoving(event));
n.Limits = [-100 100];
m = uislider(fig,'Value',1, 'Position',[220 80 200 200], 'ValueChangingFcn',@(m, event) sliderMoving(event));
m.Limits = [-10 10];
a = uislider(fig,'Value',1, 'Position',[220 120 200 200], 'ValueChangingFcn',@(a, event) sliderMoving(event));
a.Limits = [-10 10];

phi = 0:0.0001:2*pi*m.Value;

function sliderMoving(event)
global nv mv av phi ax2;
global n m a;
nv = n.Value;
mv = m.Value;
av = a.Value;
phi = 0:0.0001:2*pi*mv;
nm = nv/mv;
x = (1+nm)*cos(nm*phi)-av*nm*cos((1+nm) * phi);
y = (1+nm)*sin(nm*phi)-av*nm*sin((1+nm) * phi);
plot(ax2, x, y)
end