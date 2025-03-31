class MealyAutomaton:
    def __init__(self):
       
        self.current_state = "S0"
        
        
        self.transitions = {
            ("S0", (0, 0)): ("S0", 0),
            ("S0", (0, 1)): ("S1", 1),
            ("S0", (1, 0)): ("S0", 0),
            ("S0", (1, 1)): ("S1", 1),
            ("S1", (0, 0)): ("S1", 1),
            ("S1", (0, 1)): ("S1", 1),
            ("S1", (1, 0)): ("S0", 0),
            ("S1", (1, 1)): ("S0", 0)
        }
    
    def process_input(self, input_signal):
        
        next_state, output = self.transitions[(self.current_state, input_signal)]
        
        self.current_state = next_state
        
        return output
    
    def get_state(self):
        return self.current_state


def test_mealy():
    automaton = MealyAutomaton()
    
    
    test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1), (0, 0)]
    
    print("Mealy Automaton Test:")
    print("---------------------")
    for input_signal in test_inputs:
        output = automaton.process_input(input_signal)
        print(f"State: {automaton.get_state()}, Input: {input_signal}, Output: {output}")
    
class MooreAutomaton:
    def __init__(self):
        
        self.current_state = "S0_0"
        
        
        self.transitions = {
            ("S0_0", (0, 0)): "S0_0",
            ("S0_0", (0, 1)): "S1_1",
            ("S0_0", (1, 0)): "S0_0",
            ("S0_0", (1, 1)): "S1_1",
            ("S1_1", (0, 0)): "S1_1",
            ("S1_1", (0, 1)): "S1_1",
            ("S1_1", (1, 0)): "S0_0",
            ("S1_1", (1, 1)): "S0_0"
        }
        
       
        self.outputs = {
            "S0_0": 0,
            "S1_1": 1
        }
    
    def process_input(self, input_signal):
        
        next_state = self.transitions[(self.current_state, input_signal)]
        
       
        self.current_state = next_state
        
        
        return self.outputs[self.current_state]
    
    def get_state(self):
        return self.current_state
    
    def get_output(self):
        return self.outputs[self.current_state]


def test_moore():
    automaton = MooreAutomaton()
    
    
    test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1), (0, 0)]
    
    print("\nMoore Automaton Test:")
    print("---------------------")
    print(f"Initial State: {automaton.get_state()}, Output: {automaton.get_output()}")
    
    for input_signal in test_inputs:
        automaton.process_input(input_signal)
        print(f"Input: {input_signal}, New State: {automaton.get_state()}, Output: {automaton.get_output()}")


test_mealy()
test_moore()
class NFA_Epsilon:
    def __init__(self):
       
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9'}
        
        
        self.alphabet = {'a', 'b', 'ε'}
        
        
        self.transitions = {
            ('q0', 'ε'): {'q1', 'q2'},
            ('q1', 'b'): {'q3'},
            ('q2', 'a'): {'q9'},
            ('q3', 'ε'): {'q4'},
            ('q4', 'ε'): {'q5', 'q6'},
            ('q5', 'a'): {'q7'},
            ('q6', 'b'): {'q7'},
            ('q7', 'ε'): {'q8'},
            ('q8', 'ε'): {'q4', 'q9'}
        }
        
      
        self.initial_state = 'q0'
       
        self.accepting_states = {'q9'}
    
    def epsilon_closure(self, states):
        
        
        result = set(states)
        stack = list(states)
        
      
        while stack:
            state = stack.pop()
            if (state, 'ε') in self.transitions:
                for next_state in self.transitions[(state, 'ε')]:
                    if next_state not in result:
                        result.add(next_state)
                        stack.append(next_state)
        
        return result
    
    def move(self, states, symbol):
      
        result = set()
        
        for state in states:
            if (state, symbol) in self.transitions:
                result.update(self.transitions[(state, symbol)])
        
        return result
    
    def accepts(self, string):
        
        
        current_states = self.epsilon_closure({self.initial_state})
        
    
        for symbol in string:
            if symbol not in {'a', 'b'}:
                return False 
            
           
            current_states = self.epsilon_closure(self.move(current_states, symbol))
            
            
            if not current_states:
                return False
        
      
        return any(state in self.accepting_states for state in current_states)


def test_nfa():
    nfa = NFA_Epsilon()
    
    test_strings = ["a", "b", "ba", "bb", "baa", "bab", "bba", "bbb", "baaa"]
    
    print("Testing NFA-ε for regular expression b(a+b)(a+b)*+a:")
    print("----------------------------------------------------")
    
    for s in test_strings:
        result = nfa.accepts(s)
        print(f"String '{s}': {'Accepted' if result else 'Rejected'}")


test_nfa()