from Array import Array
class Array2D:
    def __init__(self,m,n):
        self._nrow=m
        self._ncol=n
        self._RowArr=Array(m)
        for i in range(self._nrow):
            workArr=Array(n)
            workArr.clear(0)
            self._RowArr.setitem(workArr,i)
            pass
        pass
    def nrow(self):
        return self._nrow
    def ncol(self):
        return self._ncol
    def getitem2D(self,r,c):
        #print r
        arr=self._RowArr.getitem(r)
        return arr.getitem(c)
    def setitem2D(self,r,c,val):
        arr=self._RowArr.getitem(r)
        arr.setitem(val,c)
        pass
    def clear(self,val):
        for i in range(self._nrow):
            arr=self._RowArr.getitem(i)
            for j in range(self._ncol):
                arr.setitem(0,j)
                
                

        
                    