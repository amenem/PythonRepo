from Array2D import Array2D
class maze2D:
    def __init__(self,f,row,col):
        #read the file put into 2D maze
        self._sol=Array2D(row,col)
        self._sol.clear('0')
        self._ref=Array2D(row,col)
        self._ref.clear(0)
        self._maze=Array2D(row,col)
        self._ctr=0
        f=open(f,'r')
        for r in range(self._maze.nrow()):
            c=0
            line=f.readline()
            for cell in line:
                if cell !='\n':
                    self._maze.setitem2D(r,c,int(cell))
                    c+=1
    def foundpath(self,x,y):
        #maze.show_maze()       
        if x<0 or x>self._maze.nrow()-1 or y<0 or y>self._maze.ncol()-1:
            return False
        #print ("x",x,"y",y)
        #print ("ref:",self._ref.getitem2D(x,y))         
        if self._maze.getitem2D(x,y)==2:
            self._sol.setitem2D(x,y,'#')
            self._ref.setitem2D(x,y,3)
            return True
        
        if self.issafe(x,y)==True:
            self._sol.setitem2D(x,y,'#')
            self._ref.setitem2D(x,y,3)
            if self.foundpath(x+1,y)==True:
                return True
            if self.foundpath(x-1,y)==True:
                return True
            if self.foundpath(x,y+1)==True:
                return True
            if self.foundpath(x,y-1)==True:
                return True
            self._sol.setitem2D(x,y,0)
            #self.show_maze_sol()
            #print"-----------------"
            return False
        return False
    def issafe(self,x,y):
        #print ("val",self._maze.getitem2D(x,y))
        return (self._maze.getitem2D(x,y)==0 and self._ref.getitem2D(x,y)!=3     ) 
            
        
    def show_maze_sol(self):
        for i in range(self._maze.nrow()):
            print '\n'
            for j in range(self._maze.ncol()):
                print self._sol.getitem2D(i,j),
                pass
            pass
        pass
    def show_maze_ref(self):
        for i in range(self._maze.nrow()):
            print '\n'
            for j in range(self._maze.ncol()):
                print self._ref.getitem2D(i,j),
    def show_maze(self):
        for i in range(self._maze.nrow()):
            print '\n'
            for j in range(self._maze.ncol()):
                print self._maze.getitem2D(i,j),
        
            

maze=maze2D("c:\\users\\aman\\workspace\\maze\\data.txt",5,8)
maze.foundpath(0,0)
#maze.show_maze_ref()
print("\n###############")
maze.show_maze_sol()


            
        
        
                    
            
        

        
        
        
    
    