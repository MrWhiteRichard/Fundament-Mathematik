preamble

%% Define equation 
syms y(x)
Dy=diff(y);
Dy2=diff(y,2);
Dy3=diff(y,3);
a=2; b=1; c=4; d=3
eq=a*x^4*Dy3+b*x^3*Dy2+c*x^2*Dy+d*x*y;
eqlatex="$x^2y''+"+string(a)+"xy'+"+string(b)+"y=0$";

[eqs,vars]=reduceDifferentialOrder(eq,y(x));
[M,F]=massMatrixForm(eqs,vars);
f=M\F;
fh=odeFunction(f,vars)
x1=0; 
x2=10; 

yini=(2/25)*x^2-(3/5)*x;
Dyini=simplify(diff(yini));
Dy2ini = simplify(diff(yini,2));
yinit=matlabFunction([-yini;-Dyini;-Dy2ini]);  

bv=[0;2;1]
bcres=@(y1,y2,bv) [y1(1)-bv(1);y2(1)-bv(2);y2(2)-bv(3)];

xinit=linspace(x1,x2,201);
solinit=bvpinit(xinit,yinit);
solnum=bvp4c(fh,@(y1,y2) bcres(y1,y2,bv),solinit)
xs=solnum.x;
ys=solnum.y(1,:);
figure(1)
clf
hold on
hnum=plot(xs,ys,'b');
ys1=solnum.y(2,:); % first derivative of y
ys2=solnum.y(3,:); % second derivative of y
ys3=solnum.yp(3,:); % third derivative of y
% proof
lhs=a*xs.^4.*ys3 + b*xs.^3.*ys2 + c*xs.^2.*ys + d*xs.*ys; % subsitute solution into ODE
hproof=plot(xs,lhs,'k--');
box on
grid on
xlabel('$x$')
ylabel('$y(x)$')
xlim([x1 x2])
htit=title(join(titstr),'fontsize',16);
yl=get(gca,'ylim');
set(htit,'position',get(htit,'position')+[0 0.01*diff(yl) 0]); % shift up title

