clc

%Problem 1
A = [5 -2 1; 1 0 4; -3 7 2];
B = [2 2 3; -1 4 1; 5 -3 0];
C = [1 -1 2; 0 1 4; -5 3 6];
D = [-1 2 3; 0 4 5];
x = [-2; 3; 1];

%Problem 2
a = A + B;
disp("b can't be computed as B and D do not have the same dimensions")%b = B - D;
c = A*B;
d = B*A;
e = D*C;
f = C';
g = C*x;
disp("H cannot be computed as x does not have the same number of rows and columns") %h = x*x;
i = x' * x;
j = ((A-B)*x)';
k = A^2;
l = A*A;
m = 6*D;
n = 5*A - 3*B;

%Problem 3
A = [1 3; 2 4; 3 1];
B = [-1 2; 4 -2; 7 -1];

%Problem 4
a = A.*B; disp("A.*B preforms piecewise multiplication of A and B which means each cell in A is multiplied by the corresponding cell in B")
b = A./B; disp("A./B preforms piecewise division of A by B, which means each cell in A is divided by the corresponding cell in B")
c = A.^3; disp("A.^3 cubes each individual cell in A")

%Problem 5
A = [-7.5 8.0 16.0; -2.0 2.5 4.0; -2.0 2.0 4.5];
X = [4; 1; 1];

%Problem 6
r = ((A*X)./X); % returns matrix where every cell is r
r = r(1,1);
disp(r)

%Problem 7
answer = A*X - r*X;

%Problem 8
if A'*X == r*X  
    disp("true")
else
    %This one triggers
    disp("false; A'X != r*X")
end

%Problem 9
syms x
A = [1 0 0 0; 2 3 0 0; 4 5 6 0; 7 8 9 0];
p = 2*x^2 - x + 1;

disp(subs(p,-2))
disp(subs(p,2))
disp(subs(p,A))

A = [1 2; 3 4];
p = x^3 -2*x^2 + 2;

disp(subs(p,-1))
disp(subs(p,3))
disp(subs(p,A))

%Problem 10
A = [5 -8 -1; 4 -7 -4; 0 0 4];
pol = poly(A);
disp(subs(pol,A))

A = [7 -4 0; 8 -5 0; -4 4 3];
pol = poly(A);
disp(subs(pol,A))

%Problem 11
disp("Evaluating the characteristic polynomial of A with A will yield a matrix with the same number of rows but many more columns, however this matrix will be full of repitition as the same operation is preformed with the sme matrix repeatedly")