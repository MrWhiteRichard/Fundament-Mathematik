preamble

dydt=@(t,y,mu) [y(2);mu*(1-y(1)^2)*y(2) - y(1)];

opt=odeset('maxstep',0.01);
solver=@ode23;
tspan1=[0 20];
mu1=1;
tspan2=[0 100];
mu2=10;

y0=[2;0];

sol1=solver(@(t,y) dydt(t,y,mu1),tspan1,y0,opt);
t=sol1.x;
y=sol1.y;

figure(1)
clf
subplot(2,1,1)
plot(t,y(1,:))
xlabel('$t$')
ylabel('$y(t)$')
xlim(tspan1)
titstr=['$y'''' = (1-y^2)y'' - y$'];
title(titstr,'fontsize',18)

sol2=solver(@(t,y) dydt(t,y,mu2),tspan2,y0,opt);
t=sol2.x;
y=sol2.y;
subplot(2,1,2)
plot(t,y(1,:))
xlabel('$t$')
ylabel('$y(t)$')
xlim(tspan2)
titstr=['$y'''' = 10(1-y^2)y'' - y$'];
title(titstr,'fontsize',18)

