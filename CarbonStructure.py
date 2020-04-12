import numpy as np 
import matplotlib.pyplot as plt

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




    def cnt(self):
        pass

    def unit(self):
        pass 

    def draw(self,Points):
        for i in range(len(Points)):
            plt.plot(Points[i][0],Points[i][1],'ro')
        plt.axis('equal')
        plt.show()

    def save_xyz(self,name=''):
        pass
    
    def rotate(self,point=np.array([5,4]),theta=np.pi/2):
        R = [[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]]
        R = np.array(R)
        return R.dot(point)
    

cnt = Carbon(n=6,m=5)
points = cnt.sheet(30,30)
cnt.draw(points)