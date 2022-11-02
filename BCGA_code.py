

import numpy as np
import random
import matplotlib.pyplot as plt

def que(x):

    return x**4+2*(x**3)-30*x+20
print(que(254))


# 100<x<=300

p_size= 100
g_size=8
x_min=0
x_max=200

initial_p=["{0:08b}".format(np.random.randint(100,200)) for i in range(p_size)]


d=[]
for i in range(p_size):
    d.append(int(initial_p[i],2))
    
    
def fitness(p1):
    f_value=[]
    x=[x_min+((x_max-x_min)//((2**8)-1) *d[i] ) for i in range(p_size)]
    
    f_value.append(que(x[i] )for i in range(p_size))
    p_new=list(zip(f_value,p1))
    
    return p_new

print(fitness(initial_p))

def tournament(p2):
    t_size=8
    
    n_gen=[]
    
    
    for i in range(len(p2)):
       
        temp=random.choices(p2,k=8)
            
        temp.sort(reverse=True)
        n_gen.append(temp[0])
        
    return n_gen





def crossover(p3):
    crossover_p=0.95
    np.random.shuffle(p3)
    f_gene=p3[:len(p3)//2]
    m_gene=p3[len(p3)//2 : ]
    print(len(p3))
    
    
    child=[]
    for i in range(len(p3)//2):
        c_site=np.random.randint(0,g_size-1)
        p1=f_gene[i]
        p2=m_gene[i]
        
        f_fragment=[p1[:c_site],p1[c_site:]]
        m_fragment=[p2[:c_site],p2[c_site:]]
        
        if random.random()<crossover_p:
            c1=f_fragment[0]+m_fragment[1]
            child.append(int(c1,2))
            c2=f_fragment[1]+m_fragment[0]
            child.append(int(c2,2))
        else: 
            c1=p1
            child.append(int(c1,2))
            c2=p2
            child.append(int(c2,2))
            
    return child  





def mutation(p4):
    p_mutation= 0.2
    m_population=[]
    for i in range(len(p4)):
        if random.random() < p_mutation:
            m_site=np.random.randint(0,7)
            temp="{0:08b}".format(p4[i])
            if temp[m_site]== 0:
                m_gene=temp[:m_site]+'1'+temp[m_site+1:]
                m_population.append(int(m_gene,2))
            else:
                m_gene=temp[:m_site]+'0'+temp[m_site+1:]
                m_population.append(int(m_gene,2))
        else:            
            m_population.append(p4[i])
    return m_population       
    
soln=[] 
itr=100   
while i <= itr:
    gen_t=tournament(initial_p)
    gen_c=crossover(gen_t)
    gen_m=mutation(gen_c)    
    i=i+1
    if i==100: 
        soln=gen_m
    else:
        initial_p=gen_m
soln.sort(reverse=True)        
for i in range(p_size):
    print('x=', soln[i] ,'f(x)=',que(soln[i]))
        
        
    
x=[soln[i] for i in range(100)]
y=[que(soln[i]) for i in range(100)]    
plt.xlabel("x_axis")
plt.ylabel("y_axis")  
plt.title("graph")
for i in range(100):
   plt.plot(x,y) 
plt.show()
   
    
        
    



  
        

    
    
        
        
    
    



