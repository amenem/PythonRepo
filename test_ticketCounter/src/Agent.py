'''
Created on 11 May 2013

@author: aman.chourasia
'''
class Agent:
    def __init__(self,Id):
        self._agentId=Id
        self._passengerEngaged=None
        self._sts=0
        self._ticker=0
        
    def Id(self):
        return self._agentId
    def isFree(self):
        return self._sts == 0
    def assign(self,passenger):
        self._passengerEngaged=passenger
        self._sts=1
        
        
    def hasServed(self,serviceTime):
        return self._ticker==serviceTime
    def unassign(self):
        servedPassenger=self._passengerEngaged
        self._passengerEngaged=None
        self._sts=0
        self._ticker=0
        return servedPassenger
        
    

        
