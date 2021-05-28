preamble

syms y(t)
Dy=diff(y,t,1);
syms k M
syms C1

eqstr = "y' - k*y*(1-y/M)";

eqs=strrep(eqstr,"y'","Dy");
eq=eval(eqs)==0;

answers=dsolve(eq);
ysol (t) = answers(diff(answers, t, 1)~=0)

k0 = 0.025;
M0 = 12000;
const = [k0 M0];
inicond = [y(0)==600];
rg = [0 300];

eqsubs=subs(eq,[k M],const);
ysolpar(t)=simplify(dsolve(eqsubs,inicond));
disp(['Particular solution: y(t)=',char(ysolpar(t))]);

lastwarn('')
figure(1)
clf
fplot(ysolpar,rg)
titstr="y'-0.025y(1-y/12000)=0,\ y(0)=600";
mystr="$"+titstr+"$";
title(mystr,'fontsize',18)
box on
xlabel('$t$')
ylabel('$y(t)$')

t1 = double(solve(ysolpar(t) == 0.9*M0))

xline(t1, '-',{'t_1'})

t2 = double(solve(diff(ysolpar,t,2)==0))

xline(t2, '-',{'t_2'})

