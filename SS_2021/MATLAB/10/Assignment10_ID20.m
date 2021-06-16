%%
preamble 

%% 
opts=optimoptions('fmincon','display','final','Algorithm','sqp');
load flowdata V m
fun = @(x) ((m-x)*inv(V)*(m-x).');

[xmin,fval,exitflag,output,lam,grad,hessian] = fmincon(fun,m,[],[],[],[],[],[],@(x) conss(x),opts);
            
T = table(["g1" "g2" "g3" "c1" "c2" "c3" "s1" "s2" "s3"]', m', xmin', 'VariableNames', {'variable', 'measured', 'reconciled'});
disp(T)
fprintf('Q(xmin) = %f\n', fval)

function [cineq,ceq] = conss(x)
ceq = [x(1)-x(2)-x(3) x(7)-x(8)-x(9) x(7)-x(1)*x(4) x(8)-x(2)*x(5) x(9)-x(3)*x(6)];     % x(1)=g1, x(2)=g2, x(3)=g3, x(4)=c1, x(5)=c2, x(6)=c3, x(7)=s1, x(8)=s2, x(9)=s3
cineq = [];
end