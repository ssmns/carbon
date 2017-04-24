function zigzagCnt(n,L,string)
% clear
bond = 1.41;
a=2.46;
% n = 10;


d = a * n / pi;

% L = 26;

h = bond*cos(pi/6);

Teta = 2*pi/n;
teta = Teta/2;%asin(bond/d);

TT=[0:Teta:2*pi];
TT1=TT+3*teta;
Zc=0;
k=1;
for i=1:n
        Data1(k,1)=d/2*cos(TT(i));
        Data1(k,2)=d/2*sin(TT(i));
        Data2(k,1)=d/2*cos(TT(i)+teta);
        Data2(k,2)=d/2*sin(TT(i)+teta);
        k=k+1;
end
% 
l1=[1 1 2 2];
LL=[];
nn=ceil(L/bond);
for i=1:nn
    LL=[LL,l1];

    for j=1:length(LL)
        if (mod(j,2)==0)
            MM(j)=bond;
        else 
            MM(j)=bond/2;
        end
    end
    
    MM(1)=0;
    for j=1:length(MM)
        SS(j)=sum(MM(1:j));
    end
    if (SS(end)>L)
        break
    end
end

xx=(round(SS)>L);
for i=length(xx):-1:1
    if (xx(i)>0)
        SS(i)=[];
        LL(i)=[];
    end
end

finalData=[];
for i=1:length(SS)
    if (LL(i)==1)
        Data1(:,3)=SS(i);
        finalData=[finalData;Data1];
    else
        Data2(:,3)=SS(i);
        finalData=[finalData;Data2];
    end
end

mm=length(finalData(:,1));
fid = fopen(string,'wt');
fprintf(fid,'%3.1d \n',mm);
fprintf(fid,'C   %8.6f   %8.6f   %8.6f\n',finalData.');
fclose(fid);

end