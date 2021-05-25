preamble

dydt=@(t,y,a,q) [y(2);-(a-2*q*cos(2*t))*y(1)];

opt=odeset('maxstep',0.01);
solver=@ode23;
tspan=[0 100];
a=1.25;
q = 0.25;

y0=[0;2];

sol=solver(@(t,y) dydt(t,y,a,q),tspan,y0,opt);
t=sol.x;
y=sol.y;

figure(1)
clf
plot(t,y(1,:))
hold on
plot(t,y(2,:))
legend("$y(t)$","$y'(t)$",'interpreter','latex','fontsize',14)
xlabel('$t$')
ylabel('$y(t)$')
xlim(tspan)
titstr=['$y'''' + [a-2q\cos(2t)]y = 0 $'];
title(titstr,'fontsize',18)