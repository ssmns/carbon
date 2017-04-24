function zigzagSheet(n,L,x3,string)
bond = 1.41;

h = bond*sin(pi/6);
v = 2*bond*cos(pi/6)




for i=1:n
    Data2(i,1)=(2*i-1)*v/2;
    %Data2(i,2)=
    Data2(i,3)=x3;
end


for i=1:n+1
    Data1(i,1)=(i-1)*v;
    %Data1(i,2)=
    Data1(i,3)=x3;
end


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
        Data1(:,2)=SS(i);
        finalData=[finalData;Data1];
    else
        Data2(:,2)=SS(i);
        finalData=[finalData;Data2];
    end
end

mm=length(finalData(:,1));
fid = fopen(string,'wt');
fprintf(fid,'%3.1d \n',mm);
fprintf(fid,'C   %8.6f   %8.6f   %8.6f\n',finalData.');
fclose(fid);
   






end