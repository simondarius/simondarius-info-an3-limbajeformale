##problema 1
class FiniteAutomaton:
    def __init__(self):
       
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.initial_state = 'q0'
        self.final_states = {'q3'}
        
        
        self.alphabet = {'0', '1'}
        
      
        self.transitions = {
            'q0': {'0': 'q1', '1': 'q2'},
            'q1': {'0': 'q3', '1': 'q2'},
            'q2': {'0': 'q1', '1': 'q3'},
            'q3': {}  
        }
    
    def process_input(self, input_string):
        current_state = self.initial_state
        
        
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False, f"Invalid symbol {symbol}"
            
           
            if symbol not in self.transitions[current_state]:
                return False, f"No transition from state {current_state} with symbol {symbol}"
            
            current_state = self.transitions[current_state][symbol]
        
     
        return current_state in self.final_states, current_state


def print_transition_table(automaton):
    print("\nTransition Table:")
    print("State | 0 | 1")
    print("-" * 20)
    for state in automaton.states:
        transitions = automaton.transitions[state]
        zero_trans = transitions.get('0', '-')
        one_trans = transitions.get('1', '-')
        print(f"{state:5} | {zero_trans} | {one_trans}")


def test_automaton():
    fa = FiniteAutomaton()
    print_transition_table(fa)
    
    test_cases = ['01', '11', '001', '101', '111', '000']
    print("\nTesting various inputs:")
    for test in test_cases:
        accepted, end_state = fa.process_input(test)
        print(f"Input: {test:5} -> {'Accepted' if accepted else 'Rejected'} (Ended in state {end_state})")


#test_automaton()

##Problema 2

class CatAutomaton():
    def __init__(self):
        self.alphabet={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
        
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.initial_state = 'q0'
        self.final_states = {'q3'}
        self.transitions = {
    'q0': {
        'c': 'q1',
        'a': 'q0', 'b': 'q0', 'd': 'q0', 'e': 'q0', 'f': 'q0', 
        'g': 'q0', 'h': 'q0', 'i': 'q0', 'j': 'q0', 'k': 'q0', 
        'l': 'q0', 'm': 'q0', 'n': 'q0', 'o': 'q0', 'p': 'q0', 
        'q': 'q0', 'r': 'q0', 's': 'q0', 't': 'q0', 'u': 'q0', 
        'v': 'q0', 'w': 'q0', 'x': 'q0', 'y': 'q0', 'z': 'q0'
    },
    'q1': {
        'a': 'q2',
        'c': 'q1',
        'b': 'q0', 'd': 'q0', 'e': 'q0', 'f': 'q0', 'g': 'q0', 
        'h': 'q0', 'i': 'q0', 'j': 'q0', 'k': 'q0', 'l': 'q0', 
        'm': 'q0', 'n': 'q0', 'o': 'q0', 'p': 'q0', 'q': 'q0', 
        'r': 'q0', 's': 'q0', 't': 'q0', 'u': 'q0', 'v': 'q0', 
        'w': 'q0', 'x': 'q0', 'y': 'q0', 'z': 'q0'
    },
    'q2': {
        't': 'q3',
        'c': 'q1',
        'a': 'q0', 'b': 'q0', 'd': 'q0', 'e': 'q0', 'f': 'q0', 
        'g': 'q0', 'h': 'q0', 'i': 'q0', 'j': 'q0', 'k': 'q0', 
        'l': 'q0', 'm': 'q0', 'n': 'q0', 'o': 'q0', 'p': 'q0', 
        'q': 'q0', 'r': 'q0', 's': 'q0', 'u': 'q0', 'v': 'q0', 
        'w': 'q0', 'x': 'q0', 'y': 'q0', 'z': 'q0'
    },
    'q3': {
        'a': 'q3', 'b': 'q3', 'd': 'q3', 'e': 'q3', 'f': 'q3',
        'g': 'q3', 'h': 'q3', 'i': 'q3', 'j': 'q3', 'k': 'q3',
        'l': 'q3', 'm': 'q3', 'n': 'q3', 'o': 'q3', 'p': 'q3',
        'q': 'q3', 'r': 'q3', 's': 'q3', 't': 'q3', 'u': 'q3',
        'v': 'q3', 'w': 'q3', 'x': 'q3', 'y': 'q3', 'z': 'q3'
    }
}
    def process_input(self,input):
        current_state=self.initial_state
        for symbol in input:
           if symbol not in self.alphabet:
                return False, f"Invalid symbol {symbol}"
            
           if symbol not in self.transitions[current_state]:
                return False, f"No transition from state {current_state} with symbol {symbol}"
           
           current_state = self.transitions[current_state][symbol]
        
        return current_state in self.final_states, current_state

def test_ex2():
    ca=CatAutomaton()
    cases=['cat','dcat','none']
    for test in cases:
        accepted, end_state = ca.process_input(test)
        print(f"Input: {test:5} -> {'Accepted' if accepted else 'Rejected'} (Ended in state {end_state})")

#test_ex2()

class AutomatonL:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.alphabet = {'a', 'b', 'c', 'd'}
        self.initial_state = 'q0'
        self.final_states = {'q3'}
        
        self.transitions = {
            'q0': {'a': 'q1', 'b': 'q0', 'c': 'q0', 'd': 'q0'},
            'q1': {'a': 'q1', 'b': 'q2', 'c': 'q1', 'd': 'q1'},
            'q2': {'a': 'q2', 'b': 'q2', 'c': 'q2', 'd': 'q3'},
            'q3': {'a': 'q3', 'b': 'q3', 'c': 'q3', 'd': 'q3'}
        }

    def check_word(self, word):
        if not all(c in self.alphabet for c in word):
            return False
            
        current_state = self.initial_state
        for symbol in word:
            if symbol not in self.transitions[current_state]:
                return False
            current_state = self.transitions[current_state][symbol]
            
        return current_state in self.final_states

    def print_transition_table(self):
        print("\nTransition Table:")
        print("δ |  a  |  b  |  c  |  d  |")
        print("-" * 25)
        for state in sorted(self.states):
            transitions = self.transitions[state]
            print(f"{state} | {transitions['a']:^3} | {transitions['b']:^3} | {transitions['c']:^3} | {transitions['d']:^3} |")

def test_ex3():
    fa = AutomatonL()
    
    print("Formal Definition of the Automaton:")
    print(f"Q = {fa.states}")
    print(f"Σ = {fa.alphabet}")
    print(f"q0 = {fa.initial_state}")
    print(f"F = {fa.final_states}")
    
    fa.print_transition_table()
    
    test_words = ['abbcc', 'aaa', 'bbbaac']
    print("\nTesting specific words:")
    for word in test_words:
        result = fa.check_word(word)
        print(f"Word '{word}' is {'accepted' if result else 'rejected'}")


#test_ex3()

import re

class InvoiceValidator:
    def __init__(self):
        self.patterns = {
            'client': r'^Client: ([A-Z][a-z]+ [A-Z][a-z]+)\nCUI: (RO\d{8,10})\nAdresa: (.+)$',
            'product': r'^Produs: (.+)\nCantitate: (\d+)\nPret: (\d+\.?\d*) RON\nTVA: (19|9|5)%$',
            'date': r'^Data: (0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(202[0-9])$'
        }
        self.errors = []

    def validate_file(self, file_content):
        self.errors = []
        sections = file_content.strip().split('\n\n')
        
        if len(sections) < 3:
            self.errors.append("Factura trebuie să conțină cel puțin secțiunile: Data, Client, și un Produs")
            return False

        is_valid = True
        is_valid &= self.validate_date(sections[0])
        is_valid &= self.validate_client(sections[1])
        
        for product_section in sections[2:]:
            is_valid &= self.validate_product(product_section)
            
        return is_valid

    def validate_date(self, date_section):
        if not re.match(self.patterns['date'], date_section):
            self.errors.append("Format dată invalid. Formatul corect este: DD.MM.YYYY")
            return False
        return True

    def validate_client(self, client_section):
        if not re.match(self.patterns['client'], client_section, re.MULTILINE):
            self.errors.append("Format client invalid. Formatul corect este:\nClient: Nume Prenume\nCUI: ROXXXXXXXX\nAdresa: Strada, Număr, Oraș")
            return False
        return True

    def validate_product(self, product_section):
        if not re.match(self.patterns['product'], product_section, re.MULTILINE):
            self.errors.append("Format produs invalid. Formatul corect este:\nProdus: Nume Produs\nCantitate: X\nPret: X.XX RON\nTVA: 19%")
            return False
        return True

def test_ex4():
    validator = InvoiceValidator()
    
    try:
        file_path = input("Introduceți calea către fișierul facturii: ")
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        if validator.validate_file(content):
            print("\nFactura este validă!")
        else:
            print("\nFactura conține următoarele erori:")
            for error in validator.errors:
                print(f"- {error}")
                
    except FileNotFoundError:
        print("Eroare: Fișierul nu a fost găsit!")
    except Exception as e:
        print(f"Eroare neașteptată: {str(e)}")


test_ex4()