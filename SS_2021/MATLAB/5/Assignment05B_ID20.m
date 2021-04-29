preamble
syms a b c d

sab = (a+b+d)/2;
Aab = sqrt(sab*(sab-a)*(sab-b)*(sab-d));

sac = (a+c+d)/2;
Aac = sqrt(sac*(sac-a)*(sac-c)*(sac-d));

sbc = (c+b+d)/2;
Abc = sqrt(sbc*(sbc-c)*(sbc-b)*(sbc-d));

A = d^2*sqrt(3)/4;

symsols = solve( Aab + Aac + Abc == A, d );

sides = [3 4 5];

numsols = double(subs(symsols, [a b c], sides));

ind = find(numsols>max(sides) & imag(numsols)==0);
numsolb = numsols(ind);
numsolA = numsolb^2*sqrt(3)/4

symsolb = symsols(ind);
symsolA = simplify(symsolb^2*sqrt(3)/4)