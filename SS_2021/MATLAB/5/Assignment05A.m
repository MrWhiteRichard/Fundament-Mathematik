%% Solution of systems of linear equations
preamble
format short
load linear_systems % the file must be in the same directory as the script
for k=1:4
    sol=mysolve(A{k},b{k});
    disp(['>>> Solution of system ',num2str(k)])
    if isempty(sol)
        disp('System has no solution')
    else
        disp(sol)
        % Check the solution
        c=A{k}*sol-b{k};
        if iszero(c)
            disp('Solution is correct')
        else
            disp('Solution is not correct')
        end
    end
end
return

function x=mysolve(A,b) % local function
%% solve the system of linear equations A*x=b  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Single solution: return a numerical column vector x
% Infinitely many solutions: return a symbolic column vector x with the general solution
% No solution: return the empty vector
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
x=[];
return
end

function r=iszero(x) % local function
% input: numerical scalar, vector or matrix
% output: logical r
if isnumeric(x)
    r=(max(abs(round(x(:),13)))==0); % check whether x identical to 0 within rounding errors
else % symbolic x
    r=isempty(symvar(x)) & all(abs(x)<1e-13); 
end
return % return control to calling script/function
end
