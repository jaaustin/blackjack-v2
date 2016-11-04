import blackjack
from pylab import *
from random import *
import numpy as np

Q1 = [] # NumPy array of correct size
Q2 = [] # NumPy array of correct size
ET1 = [] 
ET2 = []
newQ1=[]
newQ2=[]

for i in range(361):
    Q1.append(0.00001*random())
    Q2.append(0.00001*random())
    ET1.append(0)
    ET2.append(0)
    newQ1.append(0)
    newQ2.append(0)

#print (Q1)
#print (Q2)

# Q initial is Q[0]
# Q stick is Q[s], or Q[1] to Q [180]
# Q hit is Q[s+180], or Q[181] to Q[360]

def learn(alpha, eps, gamma, decay, numTrainingEpisodes):
    returnSum = 0.0
    for episodeNum in range(numTrainingEpisodes):
        G = 0
        s = 0
        a = 1
        results = blackjack.sample(s,a)
        sprime=results[1]
        s=sprime
        #print("First turn:",results)
        while s != False:
            if random()<=eps:
                #print("Random chance of exploration!")
                a=randint(0,1)
                #print("Randomly selected an action of,",a)
            else:
                #print("Compared stick and hit:",Q1[s]+Q2[s],Q1[s+180]+Q2[s+180])
                if (Q1[s]+Q2[s])>(Q1[s+180]+Q2[s+180]):
                      a=0
                      #print("Chose stick as the action")
                else:
                      a=1
                      #print("Chose hit as the action")
            results=blackjack.sample(s,a)
            sprime=results[1]
            #print("This turn:",results)
            if randint(0,1)==1:
                #print ("Chose to update Q1 for this state and action:",s,a)
                if Q1[sprime]>Q1[sprime+180]:
                    amax=0
                    #print("Argmax for Q1 with sprime was stick")
                else:
                    amax=1
                    #print("Argmax for Q1 with sprime was hit")
                #print ("R in the update is",results[0])
                delta = (results[0]+gamma*Q2[sprime+amax*180]-Q1[s+180*a])
                #print(ET1[s+180*a])
                ET1[s+180*a]=1
                for x in range(361):
                    newQ1[x]=Q1[x]+alpha*delta*ET1[x]
                #newQ1 = Q1[s+180*a]+alpha*(results[0]+gamma*Q2[sprime+amax*180]-Q1[s+180*a])
                #print ("Q1 for this state and action has been updated from",Q1[s+180*a],"to",newQ1)
                #Q1[s+180*a]=newQ1
                ET1[:]=[x*gamma*decay for x in ET1]
                Q1[:]=[x for x in newQ1]
            else:
                #print("Chose to update Q2 for this state and action",s,a)
                if Q2[sprime]>Q2[sprime+180]:
                    amax=0
                    #print("Argmax for Q2 with sprime was stick")
                else:
                    amax=1
                    #print("Argmax for Q2 with sprime was hit")
                #print ("R in the update is",results[0])
                delta = (results[0]+gamma*Q1[sprime+amax*180]-Q2[s+180*a])
                #print(ET2[s+180*a])
                ET2[s+180*a]=1
                for x in range(361):
                    newQ2[x]=Q2[x]+alpha*delta*ET2[x]
                #newQ2 = Q2[s+180*a]+alpha*(results[0]+gamma*Q1[sprime+amax*180]-Q2[s+180*a])
                #print ("Q2 for this state and action has been updated from",Q2[s+180*a],"to",newQ2)
                #Q2[s+180*a]=newQ2
                ET2[:]=[x*gamma*decay for x in ET2]
                Q2[:]=[x for x in newQ2]
            s=sprime
        G=results[0]
        # Fill in Q1 and Q2
        #print("Episode: ", episodeNum, "Return: ", G)
        #^this was in the original code
        returnSum = returnSum + G
        if episodeNum % 10000 == 0 and episodeNum != 0:
            print("Average return so far: ", returnSum/episodeNum)

def policy(s):
    if (Q1[s]+Q2[s])>=(Q1[s+180]+Q2[s+180]):
        return 0
    else:
        return 1 

def evaluate(numEvaluationEpisodes):
    returnSum = 0.0
    for episodeNum in range(numEvaluationEpisodes):
        G = 0
        s = 0
        a = 1
        results = blackjack.sample(s,a)
        s=results[1]
        while results[1] != False:
            a=policy(s)
            results=blackjack.sample(s,a)
            s=results[1]
        G=results[0]
        # Use deterministic policy from Q1 and Q2 to run a number of
        # episodes without updates. Return average return of episodes.
        returnSum = returnSum + G
    return returnSum / numEvaluationEpisodes
