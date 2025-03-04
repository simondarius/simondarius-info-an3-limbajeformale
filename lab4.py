class NFA:
    def __init__(self):
        self.transitions = {
            ('q0', 'a'): ['q1'],
            ('q1', 'b'): ['q1', 'q2'],
            ('q1', 'ε'): ['q2'],
            ('q2', 'a'): ['q3'],
            ('q2', 'b'): ['q3'],
            ('q3', 'ε'): ['q4']
        }
        
        self.start_state = 'q0'
        self.accept_states = {'q4'}
    
    def epsilon_closure(self, states):
        closure = set(states)
        stack = list(states)
        
        while stack:
            state = stack.pop()
            
            epsilon_transitions = self.transitions.get((state, 'ε'), [])
            
            for eps_state in epsilon_transitions:
                if eps_state not in closure:
                    closure.add(eps_state)
                    stack.append(eps_state)
        
        return closure
    
    def process_input(self, input_string):
        current_states = self.epsilon_closure({self.start_state})
        
        for symbol in input_string:
            next_states = set()
            
            for state in current_states:
                state_transitions = self.transitions.get((state, symbol), [])
                
                next_states.update(state_transitions)
            
            current_states = self.epsilon_closure(next_states)
            
            if not current_states:
                return False
        
        return any(state in self.accept_states for state in current_states)

def probl1():
    nfa = NFA()
    
    test_strings = [
        'ab',
        'aab',
        'abab',
        'a',
        'b',
        '',
        'aaab'
    ]
    
    for string in test_strings:
        print(f"String '{string}': {nfa.process_input(string)}")

#probl1()
class MooreMachine:
    def __init__(self):
        self.states = {
            'S1': 'O1',
            'S2': 'O2'
        }
        
        self.transitions = {
            ('S1', 'A'): 'S1',
            ('S1', 'B'): 'S2',
            ('S2', 'A'): 'S1',
            ('S2', 'B'): 'S2'
        }
        
        self.current_state = 'S1'
    
    def transition(self, input_symbol):
        next_state = self.transitions.get((self.current_state, input_symbol))
        
        if next_state is None:
            raise ValueError(f"Invalid transition from {self.current_state} with input {input_symbol}")
        
        self.current_state = next_state
        return self.states[self.current_state]
    
    def reset(self):
        self.current_state = 'S1'

def probl2():
    machine = MooreMachine()
    
    test_sequences = [
        ['A', 'B', 'A'],
        ['B', 'A', 'B'],
        ['A', 'A', 'B']
    ]
    
    for sequence in test_sequences:
        machine.reset()
        print(f"Sequence: {sequence}")
        
        current_output = machine.states[machine.current_state]
        print(f"Initial state: {machine.current_state}, Output: {current_output}")
        
        for input_symbol in sequence:
            current_output = machine.transition(input_symbol)
            print(f"Input: {input_symbol}, New State: {machine.current_state}, Output: {current_output}")
        
        print()
probl2()
class MealyMachine:
    def __init__(self):
        self.transitions = {
            ('Q1', 'X'): ('Q2', 'O1'),
            ('Q1', 'Y'): ('Q1', 'O1'),
            ('Q2', 'X'): ('Q1', 'O2'),
            ('Q2', 'Y'): ('Q2', 'O2')
        }
        
        self.current_state = 'Q1'
    
    def transition(self, input_symbol):
        transition = self.transitions.get((self.current_state, input_symbol))
        
        if transition is None:
            raise ValueError(f"Invalid transition from {self.current_state} with input {input_symbol}")
        
        next_state, output = transition
        self.current_state = next_state
        return output
    
    def reset(self):
        self.current_state = 'Q1'

def probl3():
    machine = MealyMachine()
    
    test_sequences = [
        ['X', 'Y', 'X'],
        ['Y', 'X', 'Y'],
        ['X', 'X', 'Y']
    ]
    
    for sequence in test_sequences:
        machine.reset()
        print(f"Sequence: {sequence}")
        print(f"Initial state: {machine.current_state}")
        
        for input_symbol in sequence:
            output = machine.transition(input_symbol)
            print(f"Input: {input_symbol}, New State: {machine.current_state}, Output: {output}")
        
        print()

probl3()