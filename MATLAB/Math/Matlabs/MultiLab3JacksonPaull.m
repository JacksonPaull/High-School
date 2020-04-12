clc


%Problem 1
f1 = figure;
figure(f1);
syms x y z
g = (-4*x)/(x^2+y^2+1);
gx = diff(g,x);
gy = diff(g,y);
[xcr,ycr] = solve(gx,gy);
gxx = diff(gx,x);
gyy = diff(gy,y);
gxy = diff(gx,y);
d = gxx*gyy-(gxy)^2;

for k = 1:2
    extrema = [xcr(k),ycr(k),subs(d,[x,y],[xcr(k),ycr(k)]),subs(gxx,[x,y],[xcr(k),ycr(k)])];
end

disp('At the point (1,0) there is a max and at point (-1,0) there is a min')

[xx,yy] = meshgrid(-2:.1:2,-2:.1:2);
gfun = @(x,y)eval(vectorize(g));
gxfun = @(x,y)eval(vectorize(gradg(1)));
gyfun = @(x,y)eval(vectorize(gradg(2)));
contour(xx,yy,gfun(xx,yy),30)


%Problem 2
f2 = figure;
figure(f2);
syms x y z
h = 3*x^2*y+y^3-3*x^2-3*y^2+2;
hx = diff(h,x);
hy = diff(h,y);
[xcr,ycr] = solve(hx,hy);
hxx = diff(hx,x);
hyy = diff(hy,y);
hxy = diff(hx,y);
d = hxx*hyy-(hxy)^2;

for k = 1:4
    extrema = [xcr(k),ycr(k),subs(d,[x,y],[xcr(k),ycr(k)]),subs(hxx,[x,y],[xcr(k),ycr(k)])]
end

disp('At the points (+/-1,1) there are saddle points. At (0,0) there is a max. At (0,2) there is a min.')
[xx,yy] = meshgrid(-2:.1:2,-3:.1:3);
hfun = @(x,y)eval(vectorize(h));
hxfun = @(x,y)eval(vectorize(gradh(1)));
hyfun = @(x,y)eval(vectorize(gradh(2)));
contour(xx,yy,hfun(xx,yy),50)