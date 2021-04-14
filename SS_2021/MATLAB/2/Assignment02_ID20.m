preamble
%% problem 1
p_g = [2;3];
a_g = [2;-1];
p_h = [4;-1];
a_h = [3;2];

A = [-a_g a_h];
b = [p_g - p_h];
lambdamu = A\b;
x1 = p_g + lambdamu(1)*a_g
phi1 = acos(dot(a_g,a_h)/(norm(a_g)*norm(a_h)))

%% problem 2
n_g = [2 -3];
n_h = [3 5];
c_g = 4;
c_h = 2;

B = [n_g; n_h];
c = [c_g; c_h];

x2 = B\c

s_g = -n_g(1)/n_g(2); % Steigung von g (positiv)
s_h = -n_h(1)/n_h(2); % Steigung von h (negativ)

phi2 = atan(s_g)+atan(-s_h)

e = c_h/(dot(n_h,n_h));
d = e*norm(n_h)

%% problem 3
p_g = [1; 3; -2];
p_h = [4; 1; 2];
a_g = [2; -1; 4];
a_h = [-2; 3; 5];

A = [-a_g a_h];
b = [p_g - p_h];
lambdamu = pinv(A)*b;

C = p_g + lambdamu(1)*a_g
D = p_h + lambdamu(2)*a_h

shortest = norm(C-D)

%% problem 4
A = [-3; 2; -4];
B = [-2; 5; -1];
C = [1; 4; 6];

a = B - C;
b = C - A;
c = A - B;

lengths = [norm(a) norm(b) norm(c)]
s = sum(lengths)/2; % semiperimeter
angles = [acos(-dot(b,c)/(norm(b)*norm(c))) acos(-dot(a,c)/(norm(a)*norm(c))) acos(-dot(a,b)/(norm(a)*norm(b)))]
area1 = 1/2 * lengths(1)*lengths(2)* sin(angles(1)+angles(2))
area2 = sqrt(s*(s-lengths(1))*(s-lengths(2))*(s-lengths(3)))