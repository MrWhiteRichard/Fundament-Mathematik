preamble

f=@(x,y) Function04(x,y);
x=linspace(-8,8,61); 
y=linspace(-8,8,61);
[xx,yy]=meshgrid(x,y);
figure(2)
clf
subplot(2,1,1)
zz=f(xx,yy);
surf(xx,yy,zz)
xlabel('$x$')
ylabel('$y$')
zlabel('$z$')
colorbar
title('Surface plot of $Function04(x,y)$','fontsize',13)

subplot(2,1,2)
minz = min(min(zz));
maxz = max(max(zz));
v=linspace(minz, maxz, 20);
[C,h]=contour(xx,yy,zz,v);
xlabel('$x$')
ylabel('$y$')
zlabel('$z$')
colorbar
title('Contour lines of $Function04(x,y)$','fontsize',13) 

function z = Function04(x,y)
s=(x.^2+y.^2)/4000;
p=cos(x).*cos(y/sqrt(2));
z = s - p + 1;
z=z.*exp(-0.02*(x.^2+y.^2));
end
