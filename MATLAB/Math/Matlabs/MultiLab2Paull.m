clc
tiledlayout(3,2)

%Problem One
nexttile
t = linspace(0,6*pi);
x = (t-sin(t));
y = (t-cos(t));
comet(x,y)
title('Problem One')
xlabel('t-sin(t)')
ylabel('t-cos(t)')


%Problem 2
nexttile
t = linspace(0,2*pi);
x = ((cos(t)).^3);
y = ((sin(t)).^3);
comet(x,y)
title('Problem 2')
xlabel('cos(t)^3')
ylabel('sin(t)^3')


%Problem 3
nexttile
t = linspace(0,2*pi);
x = (2*cos(t)+cos(2*t));
y = (2*sin(t)-sin(2*t));
comet(x,y)
title('Problem 3')
xlabel('2cos(t)+cos(2t)')
ylabel('2sin(t)-sin(2t)')


%Problem 4
nexttile
t = linspace(-2*pi,2*pi);
x =(t+2*sin(2*t));
y = (t+2*cos(5*t));
comet(x,y)
title('Problem 4')
xlabel('t+2sin(2t)')
ylabel('t+2cos(5t)')


%Problem 5
nexttile
t = linspace(0,2*pi); 
x = (9*cos(t)-cos(9*t));
y = (9*sin(t)-sin(9*t));
comet(x,y)
title('Problem 5')
xlabel('9cos(t)-cos(9t)')
ylabel('9sin(t)-sin(9t)')


%Problem 6
nexttile
t = linspace(0,2*pi);
x = (sin(3*t));
y = (cos(4*t));
comet(x,y)
title('Problem 6')
xlabel('sin(3t)')
ylabel('cos(4t)')
