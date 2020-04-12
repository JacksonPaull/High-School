%Problem 1
C = [1 5; -5 3];
D = [4 3 -2; 1 0 5; 2 -1 6];

%Problem 2
% a)
5*eye(2)
disp('This generates a 2x2 identity matrix with 1s replaces with 5s')

% b)
eye(2)+ones(2)
disp('This creates a 2x2 matrix where items on the diagonal are 2, and everything else is 1')

% c)
ones(size(C))
disp('This creates a matrix the same size as C filled completely with 1s')

% d)
C+ones(size(C))
disp('This returns the matrix C with 1 added to every item')

% e)
diag(D)
disp('This returns a column matrix of everything in the diagonal of D')

% f)
diag(diag(D))
disp('This creates a matrix of m = Dm, with diagonals equal to those of D and everything else equal to 0')

% g)
diag([5 -7 1])
disp('This creates a 3x3 matrix where the items on the diagonal are 5, -7, and 1 respectively')

% h)
triu(D)
disp('This returns the upper triangular part of matrix D')

%Problem 3
% a)
diag(6*(eye(8)))

% b)
diag(3*eye(10))'

% c)
7*eye(5)

% d)
ones(3) + 2*(eye(3))

% e)
7*eye(3)-2*ones(3)

% f)
a = rand(4,3)*20

% g)
disp(a)

%Problem 4
n = 3;
a = (n-2)*eye(n)+ones(n);
disp(a)

n = 5;
a = (n-2)*eye(n)+ones(n);
disp(a)

n = 8;
a = (n-2)*eye(n)+ones(n);
disp(a)


