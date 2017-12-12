# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 09:17:27 2017

@author: Administrator
"""
import numpy as np
class matlab(object):
    def __init__(self):
        self.action_space = ['x1+', 'x1-', 'x2+', 'x2-']
        self.n_actions = len(self.action_space)
        self.n_features = 2
        self.x1=1
        self.x2=1
        self.minima=0
    def reset(self):
        self.x1=1
        self.x2=1
        return np.array([self.x1,self.x2])
    def step(self,action):
        bx1=self.x1
        bx2=self.x2
        if action==0:
            self.x1+=0.01
        elif action==1:
            self.x1-=0.01
        elif action==2:
            self.x2+=0.01
        elif action==3:
            self.x2-=0.01
        if self.x1+self.x2>6:
            reward=-1
            done=True
            print('fail------x1:%s,x2：%s'%(self.x1,self.x2))
        elif (self.x1<=0)|(self.x2<=0):
            reward=-1
            done=True
            print('fail------x1:%s,x2：%s'%(self.x1,self.x2))
        elif (2/self.x1+4/self.x2+5)<(2/bx1+4/bx2+5):
            reward=1
            done=False
            self.minima=2/self.x1+4/self.x2+5
            print('succeed------x1:%s,x2：%s'%(self.x1,self.x2))
        else:
            reward=0
            done=False
        print(2/self.x1+4/self.x2+5)
        s_=np.array([self.x1,self.x2])
        return s_,reward,done
        
    