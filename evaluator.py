import DoubleQ
from pylab import *
from random import *

def alpharun(eps,gamma,training,lowerbound,steps,repeats):
    maxreturn=-1
    maxalpha=0
    for i in range (10):
        alpha=lowerbound+i*steps
        print("Alpha is:",alpha)
        print("Epsilon is:", eps)
        print("Gamma is:",gamma)
        returnSumaverage=0
        for k in range(repeats):
            DoubleQ.Q1=[]
            DoubleQ.Q2=[]
            for i in range(361):
                DoubleQ.Q1.append(0.0001*random())
                DoubleQ.Q2.append(0.0001*random())
            DoubleQ.learn(alpha,eps,gamma,training)
            returnSum = DoubleQ.evaluate(10000000)
            print("return Sum of trial ",k+1," is: ",returnSum)
            newreturnSumaverage = returnSumaverage + returnSum
            returnSumaverage = newreturnSumaverage
        if (returnSumaverage/repeats)>maxreturn:
            maxreturn=returnSumaverage/repeats
            maxalpha=alpha
        print (repeats," trial average returnSum over 10000000 episodes after ",training," training episodes is:",returnSumaverage/repeats)
    print("Largest return was ", maxreturn, " using an alpha of ", maxalpha)

def gammarun(alpha,eps,training,lowerbound,steps,repeats):
    maxreturn=-1
    maxgamma=0
    for i in range (10):
        gamma=lowerbound+i*steps
        print("Alpha is:",alpha)
        print("Epsilon is:", eps)
        print("Gamma is:",gamma)
        returnSumaverage=0
        for k in range(repeats):
            DoubleQ.Q1=[]
            DoubleQ.Q2=[]
            for i in range(361):
                DoubleQ.Q1.append(0.0001*random())
                DoubleQ.Q2.append(0.0001*random())
            DoubleQ.learn(alpha,eps,gamma,training)
            returnSum = DoubleQ.evaluate(10000000)
            print("return Sum of trial ",k+1," is: ",returnSum)
            newreturnSumaverage = returnSumaverage + returnSum
            returnSumaverage = newreturnSumaverage
        if (returnSumaverage/repeats)>maxreturn:
            maxreturn=returnSumaverage/repeats
            maxgamma=gamma
        print (repeats," trial average returnSum over 10000000 episodes after ",training," training episodes is:",returnSumaverage/repeats)
    print("Largest return was ", maxreturn, " using a gamma of ", maxgamma)

def epsrun(alpha,gamma,training,lowerbound,steps,repeats):
    maxreturn=-1
    maxeps=0
    for i in range (100):
        eps=lowerbound+i*steps
        print("Alpha is:",alpha)
        print("Epsilon is:", eps)
        print("Gamma is:",gamma)
        returnSumaverage=0
        for k in range(repeats):
            DoubleQ.Q1=[]
            DoubleQ.Q2=[]
            for i in range(361):
                DoubleQ.Q1.append(0.0001*random())
                DoubleQ.Q2.append(0.0001*random())
            DoubleQ.learn(alpha,eps,gamma,training)
            returnSum = DoubleQ.evaluate(10000000)
            print("return Sum of trial ",k+1," is: ",returnSum)
            newreturnSumaverage = returnSumaverage + returnSum
            returnSumaverage = newreturnSumaverage
        if (returnSumaverage/repeats)>maxreturn:
            maxreturn=returnSumaverage/repeats
            maxeps=eps
        print (repeats," trial average returnSum over 10000000 episodes after ",training," training episodes is:",returnSumaverage/repeats)
    print("Largest return was ", maxreturn, " using an epsilon of ", maxeps)
