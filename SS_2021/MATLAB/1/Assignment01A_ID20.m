preamble
n = 108927;
assert(n>0)
vek = [1:n/2];
div1 = [vek(mod(n,vek) == 0), n]
div2 = divisors(n);
all(div1 == div2)