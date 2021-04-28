preamble
syms a b c d

sab = (a+b+d)/2;
Aab = sqrt(sab*(sab-a)*(sab-b)*(sab-d));

sac = (a+c+d)/2;
Aac = sqrt(sac*(sac-a)*(sac-c)*(sac-d));

sbc = (c+b+d)/2;
Abc = sqrt(sbc*(sbc-c)*(sbc-b)*(sbc-d));

A = d^2*sqrt(3)/4;

sol = solve( Aab + Aac + Abc == A, d )

sol = double(subs(sol, [a b c], [3 4 5]));

sol0 = sol(sol>5 & imag(sol)==0)

sol0sym = sym(sol0)