class DFA() : 
    
    def __init__(self, Q, Sigma, delta, q0, F) :
        self.states = Q
        self.alphabet = Sigma
        # delta[state][char] = newstate
        self.delta = delta
        self.start = q0
        self.final = F
        self.steps = 0
        
        try :
            self.check()
        except :
            print("dfa check failed")
        self.current = q0

    def check(self) :
        assert self.start in self.states
        for s in self.final :
            assert s in self.states

        for s in self.states : 
            assert s in self.delta
        for d in self.delta :
            assert d in self.states
            for c in self.alphabet :
                assert c in self.delta[d]
            for c in self.delta[d] :
                assert c in self.alphabet
                assert self.delta[d][c] in self.states

    def step(self, char) :
        self.current = self.delta[self.current][char]
        self.steps += 1
        return self.current

    def accept(self) :
        return self.current in self.final

    def reset(self) :
        self.steps = 0
        self.current = self.start

    def run(self, word) :
        self.reset()
        for c in word:
            self.step(c)
        return self.accept()

dfa_even_delta = dict()
dfa_even_delta['q0'] = dict()
dfa_even_delta['q1'] = dict()
dfa_even_delta['q0']['a'] = 'q1'
dfa_even_delta['q0']['b'] = 'q0'
dfa_even_delta['q1']['a'] = 'q0'
dfa_even_delta['q1']['b'] = 'q1'

dfa_even = DFA(['q0','q1'], ['a','b'], dfa_even_delta, 'q0',['q0'])

