preamble

n = 945743994;
v = cumprod((perms(factor(n)))');
div1 = [1, (unique(v))'];
div2 = divisors(n);
all(div1 == div2)
