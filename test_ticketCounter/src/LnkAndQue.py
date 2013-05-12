'''
Created on 11 May 2013

@author: aman.chourasia
'''

class Lnk:
    def __init__(self,obj):
        self._obj=obj
        self._next=None
        pass
    pass
class Queue:
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0
        pass
    def enqueue(self,obj):
        new_node=Lnk(obj)
        if self._head is None:
            self._head=new_node
            pass
        else:
            self._tail._next=new_node
            pass
        self._tail=new_node        
        self._size+=1    
        pass
    def dequeue(self):
        if self._head is self._tail:
            self._tail=None
            pass
        out_node=self._head
        self._head=self._head._next
        self._size-=1
        return out_node._obj
    def size(self):
        return self._size
        
            