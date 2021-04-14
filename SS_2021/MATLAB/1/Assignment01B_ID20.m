preamble
n = 6;
assert(n >= 3)
M = magic(n)
Meven = M;
Meven(mod(Meven,2) == 1) = 0
Modd = M;
Modd(mod(Modd,2) == 0) = 0
all(all((Modd + Meven) == M))
all(sort(nonzeros(Meven)) == [2:2:n^2]')
all(sort(nonzeros(Modd)) == [1:2:n^2]')
