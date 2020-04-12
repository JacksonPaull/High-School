clc

%Problem 1
[X,Y,Z] = meshgrid(0:.5:3);
u = sin(Y);
v = X .* cos(Y);
w = X./X;
quiver3(X,Y,Z,u,w,v)

%Problem 2
[X,Y,Z] = meshgrid(-3:.5:3);
u = exp(Z).*Y;
v = exp(Z) .* X;
w = exp(Z) .* X .* Y;
quiver3(X,Y,Z,u,w,v)

%Problem 3
[X,Y,Z] = meshgrid(-3:.5:3);
u = X.^2 + Y.^2;
v = X./X;
quiver(X,Y,u,v)

%Problem 4
[X,Y] = meshgrid(-5:0.5:5);
z = 5*X.^2 + 3*X.*Y + 10*Y.^2;
[dx,dy] = gradient(z);
hold on
contour(X,Y,z)
quiver(X,Y,dx,dy)
hold off

%Problem 5
[X,Y] = meshgrid(-2:.1:2);
z = sin(3*X).*cos(4*Y);
[dx,dy] = gradient(z);
hold on
contour(X,Y,z)
quiver(X,Y,dx,dy)
hold off

%Problem 6
syms x y z t
F(x,y) = [x*y,y];
ux(t) = 4*cos(t);
uy(t) = 4*sin(t);
area = int(  F(ux,uy)*diff([ux;uy],t)  ,t,0,pi/2);
vpa(area)

%Problem 7
syms x y z t
F(x,y,z) = [x^2 * z,6 * y,y*z^2];
ux(t) = t;
uy(t) = t^2;
uz(t) = log(t);
vpa(int(F(ux,uy,uz)*diff([ux;uy;uz],t),t,1,3))


