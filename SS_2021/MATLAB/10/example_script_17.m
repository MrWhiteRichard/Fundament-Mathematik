%% Constrained minimization
preamble
clear
formatSpec='%7.3f'; % default format specification
% demonstrate fmincon
syms X Y
fsym=(Y-X.^2).^2-4*(Y.^2-X);
%fsym=X.^2-Y.^2;
fhan=matlabFunction(fsym);
% contour plot
hx=0.02; % grid in x
hy=0.02; % grid in y
limx=[-2 2];
limy=[-1.5 1.5];
x=limx(1):hx:limx(2);
y=limy(1):hy:limy(2);
nx=length(x);
ny=length(y);
[xx,yy]=meshgrid(x,y);
zz=fhan(xx,yy);
minz=min(zz(:));
maxz=max(zz(:));
ch=linspace(minz,maxz,40);
%% minimize/maximize f given various constraints
% convert f to function handle in x(1) and x(2)
charf=char(matlabFunction(fsym));
charf=strrep(charf,'(X,Y)','(x) ');
charf=strrep(charf,'X','x(:,1)');
charf=strrep(charf,'Y','x(:,2)');
fhan=eval(charf) %
options=optimset('display','iter','maxiter',1000,'tolfun',1e-8,'tolx',1e-8);
ci=[183,50,57]/255;
ncase=7;
for i=5:ncase
    figure(i)
    clf
    plotContour(xx,yy,zz,ch)
    switch i
        case 1
            %% minimize with linear equality constraint: y=x/4-1
            % transform to A*[x y]'=b
            % y=x/4-1 --> -x/4+y=-1 --> [-1/4 1]*[x y]'=-1 --> A=[-1/4 1], b=-1
            k=1/4;
            d=-1;
            consstr='$y=x/4-1$';
            A=[-k 1];
            b=d;
            x0=[0 0.5]; % starting point
            typ='min';
            ctyp="lin";
            [xmin,fval,exitflag,output,lam,grad,hessian]=...
                fmincon(fhan,x0,[],[],A,b,[],[],[],options);
        case 2
            %% minimize with linear inequality constraint: y<=x/3+1
            % transform to A*[x y]'<=b
            % y<=x/3+1 --> y-x/3<=1 -->[-1/3 1]*[x y]'<=1 --> A=[-1/3 1], b=1
            k=1/3;
            d=1;
            consstr='$y\leq x/3+1$';
            A=[-k 1];
            b=d;
            x0=[0 1]; % starting point
            typ='min';
            ctyp="lin";
            [xmin,fval,exitflag,output,lam,grad,hessian]=...
                fmincon(fhan,x0,A,b,[],[],[],[],[],options);
        case 3
            %% maximize with linear inequality constraint and bounds: y>=x/3+1, -2<=x<=0, 0<=y<=1.5
            % transform to A*[x y]'<=b
            % y>=x/3+1 --> x/3-y<=-1 -->[1/3 -1]*[x y]'<=-1 --> A=[1/3 -1], b=-1
            k=1/3;
            d=1;
            consstr='$y\geq x/3+1,\ -2\leq x \leq 0,\ 0\leq y \leq 1.5$';
            A=-[-k 1]; % change sign because of >=
            b=-d;
            LB=[-2 0];
            UB=[0 1.5];
            x0=[-1.5 0.5]; % starting point
            typ='max';
            ctyp="lin";
            [xmin,fval,exitflag,output,lam,grad,hessian]=...
                fmincon(@(x) -fhan(x),x0,A,b,[],[],LB,UB,[],options);
            fval=-fval;
        case 4
            %% minimize with linear equality constraint and bounds:  y=-x-1, x<=0, y<=0
            % transform to A*[x y]'=b
            % y=-x-1 --> x+y=-1 --> A=[1 1], b=-1
            k=-1;d=-1;
            consstr=['$y=-x-1,\ x\leq0,\ y\leq0$'];
            A=[-k 1];
            b=d;
            LB=[-inf -inf]; % lower boundary
            UB=[0 0]; % upper boundary
            x0=[-0.5 0.5]; % starting point
            typ='min';
            ctyp="lin";
            [xmin,fval,exitflag,output,lam,grad,hessian]=...
                fmincon(fhan,x0,[],[],A,b,LB,UB,[],options);
        case 5
            %% maximize with nonlinear equality constraint: (x-0.2)^2/1.25+(y-0.2)^2/1.5=1
            consstr='$(x-0.2)^2/1.25+(y-0.2)^2/1.5=1$';
            cons=(X-0.2)^2/1.25+(Y-0.2)^2/1.5-1; % symbolic expression of constraint
            x0=[1 0]; % starting point
            typ='max';
            ctyp="nlin";
            [xmin,fval,exitflag,output,lam,grad,hessian]=...
                fmincon(@(x) -fhan(x),x0,[],[],[],[],[],[],@(x) nlcon(x,{[],cons}),options);
            fval=-fval;
        case 6
            %% minimize with nonlinear inequality constraint: x^2/0.5+y^2/1.25<=0.6
            consstr='$x^2/0.5+y^2/1.25\leq 0.6$';
            cons=X^2/0.5+Y^2/1.25-0.6; % symbolic expression of constraint
            LB=[-inf -inf];
            UB=[inf inf];
            x0=[0 0.5]; % starting point
            [xmin,fval,exitflag,output,lam,grad,hessian]=...
                fmincon(@(x) fhan(x),x0,[],[],[],[],LB,UB,@(x) nlcon(x,{cons,[]}),options);
            typ='min';
            ctyp="nlin";
        case 7
            %% minimize with nonlinear equality constraint and bounds: y=-x^2/4, x<=0, y<=0
            consstr='$y=-x^2/4,\ x\leq0,\ y\leq0$';
            cons=Y+X^2/4; % symbolic expression of constraint
            x0=[0 0]; % starting point
            LB=[-inf -inf];
            UB=[0 0];
            [xmin,fval,exitflag,output,lam,grad,hessian]=...
                fmincon(@(x) fhan(x),x0,[],[],[],[],LB,UB,@(x) nlcon(x,{[],cons}),options);
            typ='min';
            ctyp="nlin";
    end
    %
    if  ctyp=="lin" % linear constraint
        hr(i)=refline(k,d);
        set(hr(i),'color',ci,'linewidth',1.5);
        minstr=[',\ $x_\mathrm{',typ,'}=',num2str(xmin(1),'%6.3f'),'/',num2str(xmin(2),'%6.3f'),'$'];
    else % non-linear constraint
        hr(i)=fimplicit(cons,'color',ci,'linewidth',1.5); % plot constraint curve
        v=string(symvar(cons));
        c=strrep(string(cons),v(1),'x');
        c=strrep(c,'-','=');
        minstr=[',\ $x_\mathrm{',typ,'}=',num2str(xmin(1),'%6.3f'),'/',num2str(xmin(2),'%6.3f'),'$'];
    end
    axis equal
    xlim(limx)
    ylim(limy)
    legstr{i}=[consstr,minstr];
    hleg=legend(hr(i), legstr{i},'interpreter','latex','position',[0.2  0.02  0.6  0.1],'fontsize',16);
    hleg.AutoUpdate='off';
    % contour line through constrained minimum/maximum
    hc=contour(xx,yy,zz,[fval fval],'--','color',ci,'linewidth',1);
    hp1=plot(xmin(1),xmin(2),'+','color',ci,'markersize',8);
    hp2=plot(xmin(1),xmin(2),'o','color',ci,'markersize',8);
    title(['Constrained ',upper(typ(1)),typ(2:3),'imum \boldmath$\oplus$'],'fontsize',16,'color',ci)
    keyboard
end
%
%%
function [Cineq,Ceq]=nlcon(x,Cons)
Cineq=[];Ceq=[];
for i=1:2
    cons=Cons{i};
    if ~isempty(cons)
        v=string(symvar(cons));
        cons=strrep(string(cons),v(1),'x(1)');
        cons=strrep(cons,v(2),'x(2)');
        if i==1,Cineq=eval(cons);end
        if i==2,Ceq=eval(cons);end
    end
end
end


function plotContour(xx,yy,zz,ch)
contour(xx,yy,zz,ch)
hold on
colorbar
xlabel('$x$')
ylabel('$y$')
axis equal
grid on
xl=xlim(gca);yl=ylim(gca);
xline(0,'k:');
yline(0,'k:');
drawnow
end



