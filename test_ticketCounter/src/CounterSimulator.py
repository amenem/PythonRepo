'''
Created on 11 May 2013

@author: aman.chourasia
'''
from LnkAndQue import Queue
from random import random
from Agent import Agent
from Passenger import Passenger
import ctypes
class TicketSimulator:
    def __init__(self,numAgents,serviceTime,inbetweenTime,numMinutes):
        Arrobject=ctypes.py_object*numAgents
        self._AgentArr=Arrobject()
        for i in range(numAgents):
            self._AgentArr[i]=Agent(i)
            
        self._serviceTime=serviceTime
        self._prob=1.0/inbetweenTime
        self._numMinutes=numMinutes
        self._passengerQ=Queue()
        self._numServedPassenger=0
        self._passengerId=0
        self._numAgents=numAgents
        
    
    def run(self):
        for curTime in range(1,self._numMinutes+1):
            for i in range(self._numAgents):
                if self._AgentArr[i]._sts == 1:
                    self._AgentArr[i]._ticker+=1
            self._handleStartService(curTime)
            self._handleAssignment(curTime)
            self._handleFinishService(curTime)
#            self._handleAssignment(curTime)
            
        
    def _handleStartService(self,curTime):
        if self._prob<=random():
            self._passengerId+=1
            newPassenger=Passenger(self._passengerId)
            self._passengerQ.enqueue(newPassenger)
            
        
    def _handleAssignment(self,curTime):
        for i in range(self._numAgents):
            if self._AgentArr[i].isFree():
                if self._passengerQ.size()>0:
                    passengerToBeServed=self._passengerQ.dequeue()
                    self._AgentArr[i].assign(passengerToBeServed)
                    print ('TIME : ',curTime,' Passenger:',passengerToBeServed._passengerId,' is being served by the Agent:',i)
            
        
    def _handleFinishService(self,curTime):
        for i in range(self._numAgents):
            if self._AgentArr[i].hasServed(self._serviceTime):
                servedPassenger=self._AgentArr[i].unassign()
                print('TIME : ',curTime,' Passenger:',servedPassenger._passengerId,'has been served by the agent:',i)
                self._numServedPassenger+=1
                
            
        
    
   

d1=TicketSimulator(2,3,2,10000)
d1.run()
d2=TicketSimulator(3,4,2,10000)
d2.run()
print""
print('Agents used:',d1._numAgents)
print('passenger who are still not served',d1._passengerId-d1._numServedPassenger)
print('passenger served',d1._numServedPassenger)
print('Agents used:',d2._numAgents)
print('passenger who are still not served',d2._passengerId-d2._numServedPassenger)
print('passenger served',d2._numServedPassenger)   
        
      
        
        
            
            
            
            
