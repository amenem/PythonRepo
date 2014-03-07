import ctypes
class Array:
    def __init__(self,dim):
        arrobj=ctypes.py_object*dim
        self._Arr=arrobj()
        self._size=dim
        self.clear(0)
        pass
    def clear(self,val):
        for i in range(self.len()):
            self._Arr[i]=val
            pass
        pass
    def len(self):
        return self._size
    def getitem(self,idx):
        #print ("idx is ",idx,"self.len() is ",self.len())
        if idx>=0 and idx<self.len():
        #assert idx >=0 and idx<self.len(),"index beyond range"
           return self._Arr[idx]
        print "index beyond ranger"
        
    def setitem(self,val,idx):
        assert idx >=0 and idx<self.len(),"index beyond range"
        self._Arr[idx]=val
        pass
    pass





        
