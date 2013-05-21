'''
Created on 21-May-2013

@author: aman
'''
from Array2D import Array2D
class maze2D:
    def __init__(self,f,row,col):
        #read the file put into 2D mazerr1
        self._maze=Array2D(row,col)
        f=open(f,'r')
        
        for r in range(self._maze.nrow()):
            line=f.readline()
            c=0
            for cell in line:
                if cell != '\n':
                    print (cell,r,c)
                    self._maze.setitem2D(r,c,cell)
                    c+=1
                pass
            pass
    def show_maze(self):
        for i in range(self._maze.nrow()):
            print '\n'
            for j in range(self._maze.ncol()):
                print self._maze.getitem2D(i,j),
        
    
maze=maze2D("c:\\users\\aman\\workspace\\maze\\data.txt",6,6)
maze.show_maze()