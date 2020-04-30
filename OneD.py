import DFA
import random
import matplotlib.pyplot as plt
import matplotlib.colors as mplc

size = 40

#states = ['a','b']
#alphabet = ['aa','ab','ba','bb']
#delta = dict()
#delta['a'] = dict()
#delta['b'] = dict()
#delta['a']['aa'] = 'b'
#delta['a']['ab'] = 'a'
#delta['a']['ba'] = 'a'
#delta['a']['bb'] = 'b'
#delta['b']['aa'] = 'a'
#delta['b']['ab'] = 'b'
#delta['b']['ba'] = 'b'
#delta['b']['bb'] = 'a'
#final_states = []

# triangles
#states = ['a','b']
#alphabet = ['aa','ab','ba','bb']
#delta = dict()
#delta['a'] = dict()
#delta['b'] = dict()
#delta['a']['aa'] = 'a'
#delta['a']['ab'] = 'b'
#delta['a']['ba'] = 'b'
#delta['a']['bb'] = 'a'
#delta['b']['aa'] = 'a'
#delta['b']['ab'] = 'a'
#delta['b']['ba'] = 'a'
#delta['b']['bb'] = 'a'
#final_states = []

# triangles
states = ['a','b']
alphabet = ['aa','ab','ba','bb']
delta = dict()
delta['a'] = dict()
delta['b'] = dict()
delta['a']['aa'] = 'a'
delta['a']['ab'] = 'b'
delta['a']['ba'] = 'b'
delta['a']['bb'] = 'a'
delta['b']['aa'] = 'b'
delta['b']['ab'] = 'a'
delta['b']['ba'] = 'b'
delta['b']['bb'] = 'a'
final_states = []

grid = list()
for i in range(size) :
    init = 'a'
    if random.random() > 1 or i == size/2-1 or i == size/2-1:
        init = 'b'
    next_DFA = DFA.DFA(states, alphabet, delta, init, final_states)
    grid.append(next_DFA)
        

def step_grid() : 
    chars = list()
    for i,dfa in enumerate(grid):
       chars.append(grid[(i-1)%size].current + grid[(i+1)%size].current)
    for i,dfa in enumerate(grid) :
       dfa.step(chars[i])

def print_grid() :
    print(''.join(list_grid()))

def list_grid() :
    return[dfa.current for dfa in grid]
    
def reset_grid() :
    for dfa in grid:
        dfa.reset()

im = list()
print_grid()
im.append(list_grid())
for i in range(150) : 
    step_grid()
    print_grid()
    im.append(list_grid())


s = list()
for i in range(len(im)) :
    s.append([])
    for j in range(size) :
        c = im[i][j]
        if c == 'a' :
            v = 0.1
        elif c == 'b' :
            v = 0.9
        s[i].append(v)
plt.imshow(s, interpolation='none', norm=mplc.Normalize(vmin=0.,vmax=1.))
plt.xticks([])
plt.yticks([])
plt.savefig('O2.png')
plt.close()
