##problema 1
class BeverageMachine:
    def __init__(self):
        self.INITIAL_STATE = 'q0'
        self.COFFEE_STATE = 'q1'
        self.TEA_STATE = 'q2'
        self.CAPPUCCINO_STATE = 'q3'
        self.FINAL_STATE = 'q4'
        
        self.current_state = self.INITIAL_STATE
        
        self.transition_function = {
            (self.INITIAL_STATE, 'C'): self.COFFEE_STATE,
            (self.INITIAL_STATE, 'T'): self.TEA_STATE,
            (self.INITIAL_STATE, 'A'): self.CAPPUCCINO_STATE,
            (self.INITIAL_STATE, 'H'): self.FINAL_STATE,
            
            (self.COFFEE_STATE, 'OK'): self.FINAL_STATE,
            (self.TEA_STATE, 'OK'): self.FINAL_STATE,
            (self.CAPPUCCINO_STATE, 'OK'): self.FINAL_STATE,
            (self.FINAL_STATE, 'OK'): self.INITIAL_STATE
        }
        
        self.beverage_names = {
            'C': 'Coffee',
            'T': 'Tea', 
            'A': 'Cappuccino', 
            'H': 'Hot Chocolate'
        }
    
    def transition(self, input_symbol):
        try:
            next_state = self.transition_function.get((self.current_state, input_symbol))
            
            if next_state is not None:
                self.current_state = next_state
                
                if self.current_state == self.FINAL_STATE and input_symbol in self.beverage_names:
                    print(f"Preparing {self.beverage_names[input_symbol]}...")
                
                return True
            else:
                print(f"Invalid transition from state {self.current_state} with input {input_symbol}")
                return False
        
        except Exception as e:
            print(f"Error during transition: {e}")
            return False
    
    def reset(self):
        self.current_state = self.INITIAL_STATE
    
    def get_current_state(self):
        return self.current_state

def probl1():
    machine = BeverageMachine()
    
    print("Simulare automat cafea")
    print("------------------------")
    
    print("\nScenariu 1: Selectare si OK cafea")
    machine.transition('C')
    machine.transition('OK')
    print(f"Current State: {machine.get_current_state()}")
    
    print("\nScenariu 2: Selectare si OK ceai")
    machine.reset()
    machine.transition('T')
    machine.transition('OK')
    print(f"Current State: {machine.get_current_state()}")
    
    print("\nScenariu 3: Testare tranzitie invalida")
    machine.reset()
    machine.transition('T')
    machine.transition('A')
    
    print("\nScenariu 4: Complet")
    machine.reset()
    machine.transition('A')
    machine.transition('OK')
    machine.transition('OK')
    machine.transition('H')
    machine.transition('OK')
    print(f"Stare Finala: {machine.get_current_state()}")

#probl1()

class ParkingLot:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.available_spots = total_spots
        self.occupied_spots = set()
        
        self.STATES = {
            'empty': 0,
            'partially_filled': 1,
            'full': 2
        }
        self.current_state = self.STATES['empty']
    
    def park(self, spot_number):
        if spot_number < 1 or spot_number > self.total_spots:
            print(f"Invalid spot number. Choose a spot between 1 and {self.total_spots}")
            return False
        
        if spot_number in self.occupied_spots:
            print(f"Spot {spot_number} is already occupied")
            return False
        
        self.occupied_spots.add(spot_number)
        self.available_spots -= 1
        
        self._update_state()
        print(f"Vehicle parked at spot {spot_number}")
        return True
    
    def leave(self, spot_number):
        if spot_number < 1 or spot_number > self.total_spots:
            print(f"Invalid spot number. Choose a spot between 1 and {self.total_spots}")
            return False
        
        if spot_number not in self.occupied_spots:
            print(f"Spot {spot_number} is already empty")
            return False
        
        self.occupied_spots.remove(spot_number)
        self.available_spots += 1
        
        self._update_state()
        print(f"Vehicle left from spot {spot_number}")
        return True
    
    def _update_state(self):
        if self.available_spots == self.total_spots:
            self.current_state = self.STATES['empty']
        elif self.available_spots == 0:
            self.current_state = self.STATES['full']
        else:
            self.current_state = self.STATES['partially_filled']
    
    def get_status(self):
        print(f"Total spots: {self.total_spots}")
        print(f"Available spots: {self.available_spots}")
        print(f"Occupied spots: {sorted(self.occupied_spots)}")
        print(f"Current state: {list(self.STATES.keys())[list(self.STATES.values()).index(self.current_state)]}")
    
    def is_spot_available(self, spot_number):
        return spot_number not in self.occupied_spots

def probl2():
    parking_lot = ParkingLot(5)
    
    print("Parking Lot Simulation")
    print("---------------------")
    
    parking_lot.get_status()
    
    print("\nParking vehicles")
    parking_lot.park(1)
    parking_lot.park(3)
    parking_lot.park(5)
    parking_lot.get_status()
    
    print("\nTrying to park in an occupied spot")
    parking_lot.park(3)
    
    print("\nLeaving vehicles")
    parking_lot.leave(1)
    parking_lot.leave(3)
    parking_lot.get_status()
    
    print("\nFilling the parking lot")
    parking_lot.park(1)
    parking_lot.park(2)
    parking_lot.park(3)
    parking_lot.park(4)
    parking_lot.get_status()
    
    print("\nTrying to park in a full parking lot")
    parking_lot.park(5)

#probl2()
class NFA:
    def __init__(self):
        self.initial_state = "q0"
        self.current_states = {self.initial_state}  
        
        self.transitions = {
            ("q0", 0): {"q0", "q1", "q2"},
            ("q0", 1): {"q1", "q2"},
            ("q0", 2): {"q2"},
            ("q1", 1): {"q1", "q2"},
            ("q1", 2): {"q2"},
            ("q2", 2): {"q2"}
        }

    def print_states(self):
        print(f"Current states: {self.current_states}")

    def input(self, symbol):
        next_states = set()  
        
        for state in self.current_states:
            if (state, symbol) in self.transitions:
                next_states.update(self.transitions[(state, symbol)])

        if next_states:
            self.current_states = next_states  
        else:
            print(f"Invalid input {symbol} for states {self.current_states}")

def probl3():
    nfa = NFA()
    print("NFA simulation")
    print("---------------")
    print("input=0")
    nfa.input(0)
    nfa.print_states()
    print("input=1")
    nfa.input(1)
    nfa.print_states()
    print("input=2")
    nfa.input(2)
    nfa.print_states()

probl3()

