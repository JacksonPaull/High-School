%Problem 1
A = [4 -2 -5; 1 1 -1; 0 0 -1];

eq = poly(A);
val = roots(poly(eq));
eq = poly2sym(eq);

disp("The characterisitc polynomial of A is:")
disp(eq)
disp("An eigen value of A is: " + val)

%Problem 2
B = [-6 8 1; -4 6 1; 0 0 1];

eq = poly(B);
val = roots(poly(eq));
eq = poly2sym(eq);

disp("The characterisitc polynomial of B is:")
disp(eq)
disp("An eigen value of B is: " + val)

%Problem 3
C = [-1/2 1 -1/2; -1/2 1 -1/2; 0 0 1];

eq = poly(C);
val = roots(poly(eq));
eq = poly2sym(eq);

disp("The characterisitc polynomial of C is:")
disp(eq)
disp("An eigen value of C is: " + val)

%Problem 4
D = [1 2 0 0; 2 1 0 0; 0 0 1 1; 0 0 1 1];

eq = poly(D);
val = roots(poly(eq));
eq = poly2sym(eq);

disp("The characterisitc polynomial of D is:")
disp(eq)
disp("An eigen value of D is: " + val)

%Problem 5
A = triu(fix(10*rand(3)));
disp("The Eigenvalues of any uppper triangular matrix should be its diagonal")
[v,d] = eig(A);

disp("Here is A followed by its eigen values")
disp(A)
disp(d)

%Problem 6
A = tril(fix(10*rand(3)));
disp("The Eigenvalues of any lower triangular matrix should be its diagonal")
[v,d] = eig(A);

disp("Here is A followed by its eigen values")
disp(A)
disp(d)

%Problem 7
disp("Therefore the eigenvalues of diagonal matricies are the values on its diagonal")






