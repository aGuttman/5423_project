import DFA
import random
import itertools
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
#states = ['a','b']
#alphabet = ['aa','ab','ba','bb']
#delta = dict()
#delta['a'] = dict()
#delta['b'] = dict()
#delta['a']['aa'] = 'a'
#delta['a']['ab'] = 'b'
#delta['a']['ba'] = 'b'
#delta['a']['bb'] = 'a'
#delta['b']['aa'] = 'b'
#delta['b']['ab'] = 'a'
#delta['b']['ba'] = 'b'
#delta['b']['bb'] = 'a'
#final_states = []
def do(esses) :

    states = ['a','b']
    alphabet = ['aa','ab','ba','bb']
    delta = dict()
    delta['a'] = dict()
    delta['b'] = dict()
    delta['a']['aa'] = esses[0]
    delta['a']['ab'] = esses[1]
    delta['a']['ba'] = esses[2]
    delta['a']['bb'] = esses[3]
    delta['b']['aa'] = esses[4]
    delta['b']['ab'] = esses[5]
    delta['b']['ba'] = esses[6]
    delta['b']['bb'] = esses[7]
    final_states = []


    size = 41
    grid = list()
    for i in range(size) :
        init = 'a'
        if random.random() > 1 or i == size/2 or i == size/2 + 1:
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
        return ''.join(list_grid())

    def list_grid() :
        return[dfa.current for dfa in grid]
        
    def reset_grid() :
        for dfa in grid:
            dfa.reset()

    def rotl(ss) : 
        return ss[1:] + [ss[0]]
    def rotr(ss) : 
        return [ss[-1]] + ss[:-1]


    im = list()
    print_grid()
    im.append(list_grid())
    for i in range(80) : 
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
    #plt.imshow(s, interpolation='none', norm=mplc.Normalize(vmin=0.,vmax=1.))
    #plt.xticks([])
    #plt.yticks([])
    #plt.savefig('odfig8/O_'+ esses + '.png')
    #plt.close()
    
    res = 'other'
    if  s[-1] == s[-2] :
        res = 'constant'
    elif  s[-1] == s[-3] :
        res = 'repeat2'
    elif s[-1] == s[-4] :
        res = 'repeat3'
    elif s[-1] == rotl(s[-2]) or s[-1] == rotr(s[-2]):  
        res = 'shift_bs'
    elif s[-1] == s[-5] :
        res = 'repeat4'
    elif s[-1] == rotl(s[-3]) or s[-1] == rotr(s[-3]):  
        res = 'shift_bbs'
    elif s[-1] == rotl(rotl(s[-2])) or s[-1] == rotr(rotr(s[-2])):  
        res = 'shift_bss'
    elif s[-1] == rotl(rotl(s[-3])) or s[-1] == rotr(rotr(s[-3])):  
        res = 'shift_bbss'
    elif s[-1] == s[-6] :
        res = 'repeat5'
    elif s[-1] == s[-7] :
        res = 'repeat6'
    elif s[-1] == s[-8] :
        res = 'repeat7'
    elif s[-1] == s[-9] :
        res = 'repeat8'
    elif s[-1] == s[-10] :
        res = 'repeat9'

    else:
        res = 'other'

    plt.imshow(s, interpolation='none', norm=mplc.Normalize(vmin=0.,vmax=1.))
    plt.xticks([])
    plt.yticks([])
    plt.savefig('odfig43/'+res+'/O_'+ esses + '.png', bbox_inches='tight')
    plt.margins
    plt.close()

    return res
        

ans = dict()
results = dict()
deltas = [''.join(y) for y in itertools.product(*['ab' for x in range(8)])]

for d in deltas[:] :
    res = do(d)
    ans[res] = ans.get(res,0) + 1
    if res in results : 
        results[res].append(d)
    else :
        results[res] = []


