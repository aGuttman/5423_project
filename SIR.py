import DFA
import random
import matplotlib.pyplot as plt
import matplotlib.colors as mplc

class Grid() :
    def __init__(self, Xsize, Ysize) :
        self.data = [ [None for j in range(Ysize)] for i in range(Xsize) ]

    def get(self,i,j) :
        return self.data[i % Xsize][j % Ysize]
    
    def set(self, i, j, val) :
        self.data[i % Xsize][j % Ysize] = val
        


states = ['s','i','r']
alphabet = [0,1,2,3,4,5,6,7,8]

#SIR 
delta = dict()
delta['s'] = dict()
delta['i'] = dict()
delta['r'] = dict()
delta['s'][0] = 's'
delta['s'][1] = 'i'
delta['s'][2] = 'i'
delta['s'][3] = 'i'
delta['s'][4] = 'i'
delta['s'][5] = 'i'
delta['s'][6] = 'i'
delta['s'][7] = 'i'
delta['s'][8] = 'i'
delta['i'][0] = 'r'
delta['i'][1] = 'r'
delta['i'][2] = 'r'
delta['i'][3] = 'r'
delta['i'][4] = 'r'
delta['i'][5] = 'r'
delta['i'][6] = 'r'
delta['i'][7] = 'r'
delta['i'][8] = 'r'
delta['r'][0] = 'r'
delta['r'][1] = 'r'
delta['r'][2] = 'r'
delta['r'][3] = 'r'
delta['r'][4] = 'r'
delta['r'][5] = 'r'
delta['r'][6] = 'r'
delta['r'][7] = 'r'
delta['r'][8] = 'r'


final_states = []

Xsize = 10
Ysize = 10
grid = Grid(Xsize,Ysize)

for i in range(Xsize) :
    for j in range(Ysize) :
        r = random.random()
        if r < 0.5 :
            init = 'r'
        else :
            init = 's'
        if (i,j) == (5,5) or  (i,j) == (4,5) or  (i,j) == (5,4) or  (i,j) == (6,5) or  (i,j) == (5,6) :
            init = 's'
        if (i,j) == (5,5) :
            init = 'i'
        next_DFA = DFA.DFA(states, alphabet, delta, init, final_states)
        grid.set( i, j, next_DFA)

#next_DFA = DFA.DFA(states, alphabet, delta, 'i', final_states)
#grid.set(random.randint(0,9), random.randint(0,9), next_DFA)

        

def neighbor_input(i,j) :
    adjacent = [  (-1, 0),  (0, -1), (0,1), (1,0)]
    nargs = [ (i+x, j+y) for (x,y) in adjacent]
    neighbors = [ grid.get(*n).current for n in nargs]
    return sum( n == 'i' for n in neighbors)



def step_grid() : 
    charg = Grid(Xsize,Ysize)
    for i in range(Xsize) :
        for j in range(Ysize) :
           char = neighbor_input(i,j)
           charg.set(i,j,char)
    for i in range(Xsize) :
        for j in range(Ysize) :
           grid.get(i,j).step(charg.get(i,j))

def print_grid() :
    s = ''
    for i in range(Xsize) :
        for j in range(Ysize) :
            s += grid.get(i,j).current
        s += '\n'
    sout = s.replace('a','X').replace('b','.')
    print(sout)

fn = 'a'
def save_grid() :
    global fn
    s = list()
    for i in range(Xsize) :
        s.append([])
        for j in range(Ysize) :
            c = grid.get(i,j).current
            if c == 'i' :
                v = 0.6
            elif c == 's' :
                v = 0.25
            elif c == 'r' : 
                v = 0.1
            else :
                print('uh oh')
            s[i].append(v)
    plt.imshow(s, interpolation='none', norm=mplc.Normalize(vmin=0.,vmax=1.))
    plt.xticks([])
    plt.yticks([])
    plt.savefig(fn+'.png')
    plt.close()
    print(s)
    fn = chr(ord(fn) + 1)
    
def reset_grid() :
    for i in range(Xsize) :
        for j in range(Ysize) :
            grid.get(i,j).reset()

print_grid()
save_grid()
for i in range(50) : 
    #raw_input()
    step_grid()
    #print_grid()
    if i == 0:
        save_grid()
        
print_grid()
save_grid()
