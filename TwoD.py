import DFA

class Grid() :
    def __init__(self, Xsize, Ysize) :
        self.data = [ [None for j in range(Ysize)] for i in range(Xsize) ]

    def get(self,i,j) :
        return self.data[i % Xsize][j % Ysize]
    
    def set(self, i, j, val) :
        self.data[i % Xsize][j % Ysize] = val
        


states = ['a','b']
alphabet = [0,1,2,3,4,5,6,7,8]

#conway a = alive, b = dead, alphabet = number of alive neighbors
delta = dict()
delta['a'] = dict()
delta['b'] = dict()
delta['a'][0] = 'b'
delta['a'][1] = 'b'
delta['a'][2] = 'a'
delta['a'][3] = 'a'
delta['a'][4] = 'b'
delta['a'][5] = 'b'
delta['a'][6] = 'b'
delta['a'][7] = 'b'
delta['a'][8] = 'b'
delta['b'][0] = 'b'
delta['b'][1] = 'b'
delta['b'][2] = 'b'
delta['b'][3] = 'a'
delta['b'][4] = 'b'
delta['b'][5] = 'b'
delta['b'][6] = 'b'
delta['b'][7] = 'b'
delta['b'][8] = 'b'
final_states = []

Xsize = 10
Ysize = 10
grid = Grid(Xsize,Ysize)

for i in range(Xsize) :
    for j in range(Ysize) :
        init = 'b'
        next_DFA = DFA.DFA(states, alphabet, delta, init, final_states)
        grid.set( i, j, next_DFA)

#basic flier
grid.get(1,2).current = 'a'
grid.get(2,3).current = 'a'
grid.get(3,1).current = 'a'
grid.get(3,2).current = 'a'
grid.get(3,3).current = 'a'

        

def neighbor_input(i,j) :
    adjacent = [ (-1,-1), (-1, 0), (-1, 1), (0, -1), (0,1), (1,-1), (1,0), (1,1)]
    nargs = [ (i+x, j+y) for (x,y) in adjacent]
    neighbors = [ grid.get(*n).current for n in nargs]
    return sum( n == 'a' for n in neighbors)



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
    
def reset_grid() :
    for i in range(Xsize) :
        for j in range(Ysize) :
            grid.get(i,j).reset()

print_grid()
for i in range(20) : 
    step_grid()
    print_grid()

