%Problem 1
syms x y
int(int(exp(x^2-y^2),y,1-x,1-x^2),x,0,1)

%Problem 2
double(int(int(exp(x^2-y^2),y,1-x,1-x^2),x,0,1))

%Problem 3
syms x y
y1 = 3*x^2;
y2 = 2*x+3;
ezplot(y1,[-3,3]); hold on
ezplot(y2,[-3,3]); hold off
    %Vertically simple
lims = solve(y2-y1);
double(int(int(x*exp(-y^2),y,y1,y2),x,lims(1),lims(2)))

%Problem 4

syms r th
eq = x^2+(y-2)^2-4;
eq = simplify(subs(eq,[x,y],[r*cos(th),r*sin(th)]));
%lims = solve(eq,r);

double(  int(  int(r*exp(-r^2),r,0,4*sin(th))  ,th,0,pi)  )