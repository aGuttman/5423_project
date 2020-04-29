import DFA

size = 10

states = ['a','b']
alphabet = ['aa','ab','ba','bb']
delta = dict()
delta['a'] = dict()
delta['b'] = dict()
delta['a']['aa'] = 'b'
delta['a']['ab'] = 'a'
delta['a']['ba'] = 'a'
delta['a']['bb'] = 'b'
delta['b']['aa'] = 'a'
delta['b']['ab'] = 'b'
delta['b']['ba'] = 'b'
delta['b']['bb'] = 'a'
final_states = []

grid = list()
for i in range(size) :
    init = 'a'
    next_DFA = DFA.DFA(states, alphabet, delta, init, final_states)
    grid.append(next_DFA)
        

def step_grid() : 
    chars = list()
    for i,dfa in enumerate(grid):
       chars.append(grid[(i-1)%size].current + grid[(i+1)%size].current)
    for i,dfa in enumerate(grid) :
       dfa.step(chars[i])

def print_grid() :
    print ''.join( dfa.current for dfa in grid)
    
def reset_grid() :
    for dfa in grid:
        dfa.reset()


print_grid()
for i in range(20) : 
    step_grid()
    print_grid()


