function armchairCnt(n,L,string)
bond = 1.41;
a=2.46;
%n = 10;


d = a * n * sqrt(3) / pi;

%L = 26;

h = bond*cos(pi/6);

Teta = 2*pi/n;
teta = asin(bond/d);

TT=[0:Teta:2*pi];
TT1=TT+3*teta;
Zc=0;
k=1;
for i=1:n
    for j=1:2
        Data(k,1)=d/2*cos(TT(i)+(-1)^j*teta);
        Data(k,2)=d/2*sin(TT(i)+(-1)^j*teta);
        Data(k,3)=Zc;
        k=k+1;
    end
    for j=1:2
        Data(k,1)=d/2*cos(TT1(i)+(-1)^j*teta);
        Data(k,2)=d/2*sin(TT1(i)+(-1)^j*teta);
        Data(k,3)=Zc+h;
        k=k+1;
    end
end

l1=max(Data(:,3))-min(Data(:,3));
hig = 2*h;
nR = ceil(L/(l1+h))-1;

finalData=Data;

for i=1:nR
    matrix = Data;
    matrix(:,3)=matrix(:,3)+hig;
    finalData=[finalData;matrix];
    hig = hig+2*h;
end



mm=length(finalData(:,1));
fid = fopen(string,'wt');
fprintf(fid,'%3.1d \n',mm);
fprintf(fid,'C   %8.6f   %8.6f   %8.6f\n',finalData.');
fclose(fid);




end