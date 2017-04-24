clc
clear
close all

% n != 0 and m=0 ==> zigzag
% n == m         ==> armchair
% n !=m          ==> chiral
n=10;
L=25;
string = 'armcharcnt1.xyz' ;
armchairCnt(n,L,string)
string = 'zigzagcnt1.xyz';
zigzagCnt(n,L,string);
x3=0;
string ='zigzagSheet.xyz';
zigzagSheet(n,L,x3,string)
    




