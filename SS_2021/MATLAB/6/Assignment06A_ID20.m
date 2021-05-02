preamble
load struct06A S % load structure array S from file struct.mat
% struct.mat must be in the same directory as the script
result=find_match('016',S)
% correct answer: 16    21    28    32
result=find_match(016,S)
% correct answer: error message and empty result
result=find_match('Moha',S)
% correct answer: 2     6
result=find_match('moha',S)
% correct answer: 2     6
result=find_match('0663',S)
% correct answer: 2     4     7    19    20    22    23    25    29
result=find_match('0663',S,'scode')
% correct answer: 2     4     7    19    20    22    23    25    29
result=find_match('0663',S,'Scode')
% correct answer: warning message and empty result
result=find_match('sal',S,'name')
% correct answer: 25    26
result=find_match('016',S,'matnum')
% correct answer: 16    21    28    32
result=find_match('w',S,'gender')
% correct answer: 1     7    21    24    32
result=find_match('a',S,'gender')
% correct answer: empty result
result=find_match('y',S)
% correct answer: 6    19    20    27    31

% input arguments: ********************************************
% key: search string (character array or string)
% struct: structure array
% field: name of the field of struct that is to be searched, 
%        (char array or string);
%        if empty or missing: all fields of struct are searched;
%        if field does not match a field name of struct, 
%        print out a warning and return an empty result;
%        the matching is case insensitive.
%
% *******************************************************
% if any input argument is not of the correct type,     *
% return an empty result and print an error message <<  *
% *******************************************************
%
% output argument: **************************************
% result: vector of indices of the elements of struct 
%         where a match is found
% Example: result=find_match('01',struct,'myfield') returns the 
%          indices of all elements of struct where the string '01' 
%          is found in field 'myfield'
% Example: result=find_match('Ab',struct) returns the indices of
%          all elements of struct where any of the strings 'AB', 
%          'Ab', 'aB', 'ab' is found in any field
function result=find_match(key,struct,field)
    result = [];
    if nargin == 2
        if any([any(~strcmp(class(struct), 'struct')), ~strcmp(class(key), 'char')])
            warning("Wrong input argument type or field does not exist")
            return
        end
        n = length(struct);
        for i=1:n
            fields = fieldnames(struct(i));
            m = length(fields);
            for j=1:m
                 if contains(lower(getfield(struct(i), fields{j})), lower(key))
                    result = [result i];
                 end
            end
        end
        return
    end
    if nargin < 2
        warning("Not enough input arguments")
        return
    end
    if nargin == 3
        if any([any(~strcmp(class(struct), 'struct')), ~strcmp(class(key), 'char'), ~strcmp(class(field), 'char'), all(~strcmp(fieldnames(struct), field))])
            warning("Wrong input argument type or field does not exist")
            return
        end
        n = length(struct);
        for i=1:n
            if contains(lower(getfield(struct(i), field)), lower(key))
                result = [result i];
            end
        end
        return
    end
end

