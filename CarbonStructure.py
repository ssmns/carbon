import numpy as np 
import matplotlib.pyplot as plt
import mpl_toolkits
from mpl_toolkits.mplot3d import Axes3D

class Carbon:
    def __init__(self,n,m=0,bond=1.41,unit='An'):
        #  n != 0 and m=0 ==> zigzag
        #  n == m         ==> armchair
        #  n !=m          ==> chiral
        
        if n <= 0  :
            print('Error! n be non-zero value and possitive value!')
        else:
            self.bond = bond  # carbon-carbond bond         
            self.m = m
            self.n = n
            self.unitfile = 'An'
            self.cell_w = self.bond * 2 * np.sin(np.pi/3)
            self.cell_h = self.bond * 2 +2* self.bond * np.cos(np.pi/3)

       
        
    def cell(self,transfer=[0,0]):
        width = self.cell_w
        heigth = self.cell_h
        x0 = transfer[0]
        y0 = transfer[1]
        Points = [[x0+0      ,y0+0],
                  [x0+0      ,y0+self.bond],
                  [x0+width/2,y0+heigth/2],
                  [x0+width/2,y0+heigth - np.cos(np.pi/3)]]
        Points = np.array(Points)
        
        return Points
        
    def sheet(self,width=25,heigth=25):
        self.width = width
        self.heigth = heigth
        Points =[]
        if self.m == 0 and self.n != 0:
            print( 'zigzag sheet created!' )
            nx = int(width/self.cell_w)
            ny = int(heigth/self.cell_h)

            for i in range(nx):
                dx = i * self.cell_w
                for j in range(ny):
                    dy = j * self.cell_h 
                    transfer=[dx,dy]
                    Points.extend(self.cell(transfer=transfer))
            
            return Points        


        elif self.m !=0 and self.n !=0:
            if self.m==self.n:
                print( 'armchair sheet created!' )
                theta = np.arctan(1/(2*np.cos(np.pi/6)))
            else:
                print( 'chiral (%i,%i) sheet created!' %(self.n,self.m))
                theta = np.arctan(self.m/(self.n*2*np.cos(np.pi/6)))
            
            newW = 1.5* width*np.sin(theta)+1.5*heigth*np.cos(theta)
            newH =1.5* width*np.cos(theta)+1.5* heigth*np.sin(theta)

            nx = int(newW/self.cell_w)
            ny = int(newH/self.cell_h)

            for i in range(nx):
                dx =  i * self.cell_w
                for j in range(ny):
                    dy = -1.5*heigth*np.sin(theta) +j * self.cell_h 
                    transfer=[dx,dy]
                    Points.extend(self.cell(transfer=transfer))
            index =[]
            for i in range(len(Points)):
                Points[i] = self.rotate(Points[i],theta)
                
                if (Points[i][0] > width  or Points[i][1] > heigth  or Points[i][0] < 0 or Points[i][1] < 0  ):
                    index.append(i)
            index.sort(reverse=True)
            for i in index:
                del Points[i]

            return Points
          
        else:
            print('Error, please check Input values')



    
    def cnt(self,points):
        # d = 78.3*np.sqrt((self.n+self.m)**2-self.m*self.n)
        R = (self.width +0.25 * self.bond) / 2 / np.pi 
        points3d =[]
        for i in points:
            points3d.append(np.array([i[0],i[1],-R]))

        # fig = plt.figure()
        # ax = fig.add_subplot(111, projection='3d')

        for i in range(len(points3d)):
            theta = points3d[i][0]/R
            points3d[i][0] = R*np.sin(theta)
            points3d[i][2] = -R*np.cos(theta)
            # ax.scatter(points3d[i][0], points3d[i][1], points3d[i][2],marker='x',color='red')
        
        # plt.show()
        return points3d

        

    def unit(self):
        pass 

    def draw(self,Points,option='ro'):
        for i in range(len(Points)):
            plt.plot(Points[i][0],Points[i][1],option)
        plt.axis('equal')
        plt.show()

    def save_xyz(self,points,name=''):
        f = open(name+'.xyz','+w')
        f.write('%i\n\n' %(len(points)))
        for i in points:
            if len(i) ==2:
                f.write('1\t %f %f %f \n'%(i[0],i[1],0))
            else:
                f.write('1\t %f %f %f \n'%(i[0],i[1],i[2]))

        f.close()
    
    def rotate(self,point=np.array([5,4]),theta=np.pi/2):
        R = [[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]]
        R = np.array(R)
        return R.dot(point)
    

cnt = Carbon(n=6,m=5)
points = cnt.sheet(30,30)
points3d = cnt.cnt(points)
cnt.save_xyz(points3d,'data')
# cnt.draw(points)