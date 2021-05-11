preamble 

%% problem 1
syms x y t
a = 5; 
b = 3; 

f(x,y) = cos(x*y);
x = a*cos(t);
y = b*sin(t);
g(t) = f(x,y);

n(t) = norm([diff(x, t) diff(y,t)]);
h = matlabFunction(n*g);
I0=integral(h,0,2*pi)

%% problem 2
syms x y 

g(x,y) = x^2 + y^2;

boundsy = solve(x^2/a^2 + y^2/b^2 == 1, y);

I1 = int(int(g, y, boundsy(1), boundsy(2)), x, -a, a)

gh=matlabFunction(g);
ymin=matlabFunction(boundsy(1));
ymax=matlabFunction(boundsy(2));
I2=integral2(gh,-a,a,ymin,ymax)

relerr1=double((I2-I1)/I1)

%% problem 3
syms r positive 
syms phi;

x = a*r*cos(phi);
y = b*r*sin(phi);
gr(r, phi) = g(x,y);

J=jacobian([x y],[r phi]);
detJ=abs(det(J));

I3=int(int(detJ*gr,r,0,1), phi, 0, 2*pi)

integrandh = matlabFunction(gr*detJ);
I4 = integral2(integrandh, 0, 1, 0, 2*pi)

relerr2=double((I4-I3)/I3)