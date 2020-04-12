format rat

%Problem 1
a = [1; -1; 1];
b = [1;0;1];
c = [1;1;2];
%Step 1, choose one vector and make it unit
v1 = a/norm(a);

%Step 2, project a vector onto v1, then take e and make it unit
A = [v1];
e = b-A*inv(A'*A)*A'*b;
v2 = e/norm(e);

%Step 3, repeat step 2 with the last matrix onto the plane created by the
%first 2
A = [v1 v2];
e = c-A*inv(A'*A)*A'*c;
v3 = e/norm(e);

%Step 4 checking
dot(v1,v2) %Just about 0
dot(v1,v3) %Just about 0
dot(v2,v3) %Just about 0

norm(v1)
norm(v2)
norm(v3)

%Problem 2
a = [1;1;1;1;1];
b = [1;2;3;4;5];
c = [1;0;1;0;1];
d = [1;2;1;0;1];
B = [a b c d];

v1 = a/norm(a);

A = [v1];
e = b-A*inv(A'*A)*A'*b;
v2 = e/norm(e);

A = [v1 v2];
e = c-A*inv(A'*A)*A'*c;
v3 = e/norm(e);

A = [v1 v2 v3];
e = d-A*inv(A'*A)*A'*d;
v4 = e/norm(e);

%Checking
dot(v1,v2)
dot(v1,v3)
dot(v1,v4)
dot(v2,v3)
dot(v2,v4)
dot(v3,v4)

norm(v1)
norm(v2)
norm(v3)
norm(v4)







