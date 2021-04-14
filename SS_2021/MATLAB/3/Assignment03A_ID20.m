preamble

s = load('Assignment03.mat');
e = 1e-16;


[sinA, cosA] = matsincos(s.A, e)
[sinB, cosB] = matsincos(s.B, e)
[sinAplusB, cosAplusB] = matsincos(s.A+s.B, e);

all([iszero(s.A*s.B-s.B*s.A), iszero(sinA^2 + cosA^2 - eye(5)), iszero(sinAplusB - sinA*cosB - cosA*sinB), iszero(cosAplusB - cosA*cosB + sinA*sinB), iszero(expm(i*s.A) - cosA - i*sinA)])



%%
function [sinX, cosX] = matsincos(X, varargin) % local function
try
    [x, y] = size(X);
catch myerror
    disp('Input is not a numerical square matrix!')
end

if (~isnumeric(X)) | (x ~= y)
    disp('Input is not a numerical square matrix!')
    sinX = [];
    cosX = [];
    return
    end
    
if nargin == 1
    e = 1e-14;
else
    e = varargin{1};
end

sinX=X;
Y=X;
n=0;
while norm(Y)>e
    n=n+1;
    Y=(-1)*Y*X^2/(2*n*(2*n+1));
    sinX=sinX+Y;
end


cosX=eye(size(X));
Y=eye(size(X));
n=0;
while norm(Y)>e
    n=n+1;
    Y=(-1)*Y*X^2/(2*n*(2*n-1));
    cosX=cosX+Y;
end
return
end

%%
function r=iszero(x,msig) % local function
% input x: numerical scalar, vector or matrix
% output r: logical scalar
if nargin==1
    msig=13; % default value if argument is missing
end
if isnumeric(x)
    r=(max(abs(round(x(:),msig)))==0); % check whether x identical to 0 within rounding errors
else
    r=false;
    warning(' input is not numeric, function iszero returns false')
end
return % return control to calling script/function
end

